#!/usr/bin/env python3
"""
Blind-grade eval outputs with an LLM judge, then summarise by condition.

The judge only ever sees: the judge rules, the case checklist, and one output.
It never sees which condition (baseline / v1 / v2) produced it.

Usage:
  python3 evals/judge.py --results /tmp/ux-eval-results --clean-config /tmp/cc-clean --jobs 4
"""
import argparse, json, os, pathlib, re, subprocess
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent
TEXT_EXT = {".md", ".html", ".htm", ".css", ".js", ".jsx", ".tsx", ".ts", ".txt", ".json"}
MAX_CHARS = 120_000

RULES = """You are grading a design output against a fixed checklist. You don't know which system produced it. Be strict and literal.

Rules:
- Score each check 1 (clearly and specifically present) or 0 (missing, wrong, or only vaguely gestured at, e.g. "consider error states" with no actual error state).
- For code, judge what the code actually does, not what comments claim.
- Do not reward length, polish or tone. Only the checks count.
- Give short evidence (<=15 words or a line reference) for every 1.
- Do not use any tools. Do not create files. Answer in text only.

Output exactly this table, then the total line:

| # | Check | Score | Evidence |
|---|---|---|---|

TOTAL: <passed>/<total>
"""


def checks_by_case():
    text = (ROOT / "cases.md").read_text()
    out = {}
    for block in re.split(r"\n## (?=E\d)", text)[1:]:
        cid = block.split(" ", 1)[0]
        m = re.search(r"\*\*Checks \((\d+)\)\*\*.*?\n(1\..*?)(?:\n---|\Z)", block, re.S)
        out[cid] = (int(m.group(1)), m.group(2).strip())
    return out


def collect_output(folder: pathlib.Path) -> str:
    parts = []
    resp = folder / "response.md"
    if resp.exists():
        parts.append("=== CHAT RESPONSE ===\n" + resp.read_text())
    for f in sorted(folder.rglob("*")):
        if f.is_file() and f.name not in ("response.md", "acme-ds.css") and f.suffix.lower() in TEXT_EXT and "judge" not in f.name:
            parts.append(f"=== FILE: {f.relative_to(folder)} ===\n" + f.read_text(errors="replace"))
    # Claude Code sometimes saves deliverables to its session scratchpad instead of the cwd.
    for f in sorted(pathlib.Path("/tmp/claude-0").glob(f"*{folder.name}*/**/scratchpad/*")):
        if f.is_file() and f.suffix.lower() in TEXT_EXT:
            parts.append(f"=== FILE (scratchpad): {f.name} ===\n" + f.read_text(errors="replace"))
    s = "\n\n".join(parts)
    return s[:MAX_CHARS] + ("\n[TRUNCATED]" if len(s) > MAX_CHARS else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", default="/tmp/ux-eval-results")
    ap.add_argument("--clean-config", default=None)
    ap.add_argument("--model", default=None)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--only", default=None, help="comma list of codes to (re)grade")
    a = ap.parse_args()

    results = pathlib.Path(a.results)
    key = json.loads((results.parent / (results.name + "_KEY_do_not_open_until_graded.json")).read_text())
    case_of = {k["code"]: k["case"] for k in key}  # condition is NOT passed to the judge
    checks = checks_by_case()
    judge_dir = results.parent / (results.name + "_judge_cwd")
    judge_dir.mkdir(exist_ok=True)
    env = dict(os.environ)
    if a.clean_config:
        env["CLAUDE_CONFIG_DIR"] = a.clean_config

    def grade(code):
        cid = case_of[code]
        total, checklist = checks[cid]
        prompt = f"{RULES}\nCHECKLIST ({total} checks):\n{checklist}\n\nOUTPUT TO GRADE:\n{collect_output(results / code)}"
        cmd = ["claude", "-p", prompt, "--output-format", "text", "--setting-sources", "project"]
        if a.model:
            cmd += ["--model", a.model]
        res = subprocess.run(cmd, cwd=judge_dir, capture_output=True, text=True, env=env, timeout=1200)
        txt = res.stdout or res.stderr
        (results / code / "judge.md").write_text(txt)
        m = re.findall(r"TOTAL:\s*(\d+)\s*/\s*(\d+)", txt)
        score = int(m[-1][0]) if m else None
        print(f"{code} {cid}: {score}/{total}", flush=True)
        return code, score, total

    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        todo = a.only.split(",") if a.only else list(case_of)
        graded = list(ex.map(grade, todo))
    if a.only:
        return

    # Unblind only after all grading is done.
    rows = []
    cond_of = {k["code"]: k["condition"] for k in key}
    for code, score, total in graded:
        rows.append({"code": code, "case": case_of[code], "condition": cond_of[code], "score": score, "max": total})
    (results.parent / (results.name + "_scores.json")).write_text(json.dumps(rows, indent=2))

    conds = [c for c in ["baseline", "v1", "v2", "v2.1", "v3", "v3.1", "v4", "v4.1"] if any(r["condition"] == c for r in rows)]
    cases = sorted({r["case"] for r in rows})
    def agg(rs):
        rs = [r for r in rs if r["score"] is not None]
        return (sum(r["score"] for r in rs), sum(r["max"] for r in rs)) if rs else (0, 0)
    lines = ["| Case | " + " | ".join(conds) + " |", "|---|" + "---|" * len(conds)]
    for c in cases:
        cells = []
        for cond in conds:
            s, m = agg([r for r in rows if r["case"] == c and r["condition"] == cond])
            cells.append(f"{s}/{m} ({round(100*s/m) if m else 0}%)")
        lines.append(f"| {c} | " + " | ".join(cells) + " |")
    cells = []
    for cond in conds:
        s, m = agg([r for r in rows if r["condition"] == cond])
        cells.append(f"**{s}/{m} ({round(100*s/m) if m else 0}%)**")
    lines.append("| **Overall** | " + " | ".join(cells) + " |")
    table = "\n".join(lines)
    (results.parent / (results.name + "_summary.md")).write_text(table + "\n")
    print("\n" + table)


if __name__ == "__main__":
    main()
