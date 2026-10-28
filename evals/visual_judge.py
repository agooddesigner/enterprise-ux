#!/usr/bin/env python3
"""
Blind visual grading from screenshots. The judge sees only the image (named by blind code)
and a fixed visual rubric — never the condition.

Usage:
  python3 evals/visual_judge.py --shots <folder of <case>-<cond>-<code>.png> --key <key.json> --clean-config /tmp/cc-clean
Writes <shots>/visual_scores.json and prints a summary per condition.
"""
import argparse, json, os, pathlib, re, shutil, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor

RUBRIC = """You are a senior product designer judging the VISUAL quality of one screenshot of an enterprise SaaS screen.
You do not know who made it. Judge only what you see. Be strict: a check passes only if it is clearly true across the screen.

Open the image file named below with the Read tool, then score.

Binary checks (1 = clearly true, 0 = not):
1. Clear hierarchy: the page title and the most important information read first; nothing competes with it
2. Consistent spacing rhythm and aligned edges (cards, columns and text align to a grid)
3. Restrained colour: neutrals + one accent + semantic status colours only; no rainbow, no decorative colour
4. Disciplined type: a small set of sizes/weights used consistently; labels clearly subordinate to values
5. Comfortable contrast: body text and labels are easily readable (no washed-out light-grey text)
6. Clean data visualisation (if charts exist): minimal gridlines, direct/clear labels, muted series with one emphasis; if no charts, numbers are cleanly presented
7. Numbers presented professionally: aligned, consistent decimals/units, scannable
8. Subtle, consistent surfaces: borders/shadows/radii restrained and uniform; no heavy drop shadows, glassmorphism or bubbly over-rounded cards
9. No generic AI-generated tells: no gradient blobs, emoji used as icons, everything centred, random accent colours, or template-looking hero
10. Density fits a professional tool: information-rich without clutter; whitespace is deliberate

Then give PREMIUM: an overall 1–10 rating where 10 = indistinguishable from the best SaaS products (Linear, Stripe, Vercel level), 5 = competent but generic, 1 = amateur.

Output exactly:
| # | Score | Reason (≤12 words) |
|---|---|---|
...
CHECKS: <n>/10
PREMIUM: <1-10>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shots", required=True)
    ap.add_argument("--key", required=True)
    ap.add_argument("--clean-config", default=None)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--cases", default=None)
    a = ap.parse_args()

    shots = pathlib.Path(a.shots)
    key = {k["code"]: k for k in json.loads(pathlib.Path(a.key).read_text())}
    env = dict(os.environ)
    if a.clean_config:
        env["CLAUDE_CONFIG_DIR"] = a.clean_config

    todo = []
    for png in sorted(shots.glob("*.png")):
        if png.name.endswith("-full.png") or "side-by-side" in png.name:
            continue
        code = png.stem.split("-")[-1]
        if code in key and (not a.cases or key[code]["case"] in a.cases.split(",")):
            todo.append((code, png))

    def grade(item):
        code, png = item
        work = pathlib.Path(tempfile.mkdtemp(prefix="vj-"))
        img = work / f"{code}.png"          # blind name: no case/condition in the filename
        shutil.copy(png, img)
        prompt = RUBRIC + f"\nImage file: {img.name}"
        cmd = ["claude", "-p", prompt, "--output-format", "text", "--setting-sources", "project",
               "--allowedTools", "Read"]
        res = subprocess.run(cmd, cwd=work, capture_output=True, text=True, env=env, timeout=900)
        txt = res.stdout or res.stderr
        (shots / f"{code}-visual-judge.md").write_text(txt)
        c = re.findall(r"CHECKS:\s*(\d+)\s*/\s*10", txt)
        p = re.findall(r"PREMIUM:\s*(\d+)", txt)
        shutil.rmtree(work, ignore_errors=True)
        r = {"code": code, "case": key[code]["case"], "condition": key[code]["condition"],
             "checks": int(c[-1]) if c else None, "premium": int(p[-1]) if p else None}
        print(code, r["checks"], r["premium"], flush=True)
        return r

    with ThreadPoolExecutor(max_workers=a.jobs) as ex:
        rows = list(ex.map(grade, todo))
    (shots / "visual_scores.json").write_text(json.dumps(rows, indent=2))

    print("\n| Condition | Visual checks | Premium (avg /10) | n |\n|---|---|---|---|")
    for cond in ("baseline", "v1", "v2", "v2.1", "v3", "v3.1", "v4", "v4.1"):
        rs = [r for r in rows if r["condition"] == cond and r["checks"] is not None]
        if rs:
            print(f"| {cond} | {sum(r['checks'] for r in rs)}/{10*len(rs)} | "
                  f"{sum(r['premium'] for r in rs)/len(rs):.1f} | {len(rs)} |")


if __name__ == "__main__":
    main()
