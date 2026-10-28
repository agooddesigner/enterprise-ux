#!/usr/bin/env python3
"""
Run the enterprise-ux eval cases in Claude Code (headless) under 3 conditions:
  baseline = no skill, v1 = old skill, v2 = current skill.

Outputs go to evals/results/<blind-code>/ with a separate key file, so grading is blind.

Usage (from the repo root):
  python3 evals/run_claude_code.py --v1 path/to/v1/enterprise-ux --runs 2 --model sonnet

Before running:
  * Temporarily move any personal design skills out of ~/.claude/skills (e.g. frontend-design,
    impeccable, ui-ux-pro-max) — otherwise they leak into every condition, including baseline.
  * Check flags against `claude --help` on your version; they were verified against docs in Oct 2026.
"""
import argparse, json, os, random, re, shutil, string, subprocess, sys, pathlib
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent
V2_SKILL = ROOT.parent / "plugins/enterprise-ux/skills/enterprise-ux"


def load_cases():
    text = (ROOT / "cases.md").read_text()
    cases = {}
    files = {}
    for block in re.split(r"\n## (?=E\d)", text)[1:]:
        cid = block.split(" ", 1)[0]
        m = re.search(r"\*\*Prompt\*\*.*?```\n(.*?)```", block, re.S)
        if not m:
            sys.exit(f"Could not parse prompt for {cid}")
        prompt = m.group(1).strip()
        if "<paste HTML here>" in prompt:
            html = (ROOT / "fixtures/audit-target.html").read_text()
            html = html[html.index("<html>"):]  # drop the answer-key comment
            prompt = prompt.replace("<paste HTML here>", html)
        cases[cid] = prompt
        fm = re.search(r"\*\*Files:\*\*\s*(.+)", block)
        files[cid] = [f.strip() for f in fm.group(1).split(",")] if fm else []
    return cases, files


def code():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--v1", required=True, help="folder of the v1 skill (contains SKILL.md)")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--model", default=None)
    ap.add_argument("--cases", default=None, help="comma list, e.g. E1,E6")
    ap.add_argument("--out", default="/tmp/ux-eval-results", help="results folder, outside the repo")
    ap.add_argument("--conditions", default="baseline,v1,v2")
    ap.add_argument("--label-v2", default="v2", help="name recorded for the current skill, e.g. v2.1")
    ap.add_argument("--label-v1", default="v1", help="name recorded for the older skill, e.g. v3")
    ap.add_argument("--jobs", type=int, default=1, help="parallel sessions")
    ap.add_argument("--clean-config", default=None, help="empty dir used as CLAUDE_CONFIG_DIR so personal skills/plugins don't leak in")
    a = ap.parse_args()

    conds = {"baseline": None, "v1": pathlib.Path(a.v1).resolve(), "v2": V2_SKILL}
    for name, p in conds.items():
        if p and not (p / "SKILL.md").exists():
            sys.exit(f"{name}: no SKILL.md in {p}")

    conds = {k: v for k, v in conds.items() if k in a.conditions.split(",")}
    cases, files = load_cases()
    if a.cases:
        cases = {k: v for k, v in cases.items() if k in a.cases.split(",")}

    # Work OUTSIDE the repo so sessions can't read cases.md (the rubric) or the fixture's answer key.
    out_root = pathlib.Path(a.out).resolve()
    out_root.mkdir(parents=True, exist_ok=True)
    jobs = [(cid, cond, r) for cid in cases for cond in conds for r in range(1, a.runs + 1)]
    random.shuffle(jobs)  # interleave so time-of-day/model drift doesn't favour one condition

    env = dict(os.environ)
    if a.clean_config:
        env["CLAUDE_CONFIG_DIR"] = a.clean_config

    def one(job):
        i, (cid, cond, run) = job
        c = code()
        work = out_root / c
        work.mkdir()
        if conds[cond]:
            shutil.copytree(conds[cond], work / ".claude/skills/enterprise-ux")
        for f in files.get(cid, []):
            shutil.copy(ROOT / f, work / pathlib.Path(f).name)
        cmd = ["claude", "-p", cases[cid], "--output-format", "text",
               "--permission-mode", "acceptEdits", "--setting-sources", "project"]
        if a.model:
            cmd += ["--model", a.model]
        print(f"[{i}/{len(jobs)}] start {cid} -> {c}", flush=True)
        try:
            res = subprocess.run(cmd, cwd=work, capture_output=True, text=True, env=env, timeout=1800)
            out = res.stdout or res.stderr
        except subprocess.TimeoutExpired:
            out = "RUN TIMED OUT after 30 min"
        (work / "response.md").write_text(out)
        for f in pathlib.Path("/tmp/claude-0").glob(f"*{c}*/**/scratchpad/*"):
            if f.is_file():
                shutil.copy(f, work / f.name)
        # remove the skill copy so graders can't see which condition it was
        shutil.rmtree(work / ".claude", ignore_errors=True)
        print(f"[{i}/{len(jobs)}] done  {cid} -> {c}", flush=True)
        return {"code": c, "case": cid, "condition": a.label_v2 if cond == "v2" else (a.label_v1 if cond == "v1" else cond), "run": run}

    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        key = list(ex.map(one, enumerate(jobs, 1)))

    (out_root.parent / (out_root.name + "_KEY_do_not_open_until_graded.json")).write_text(json.dumps(key, indent=2))
    print(f"\nDone. Grade each folder in {out_root} blind, then open the key file.")


if __name__ == "__main__":
    main()
