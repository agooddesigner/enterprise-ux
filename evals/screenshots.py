#!/usr/bin/env python3
"""
Screenshot every HTML output of an eval run, then build one side-by-side image per case
(No skill | v1 | v2) for the README.

Usage:
  python3 evals/screenshots.py --results evals/results/<run>/outputs --key evals/results/<run>/key.json --out evals/results/<run>/screenshots
Needs: pip install playwright pillow && playwright install chromium
"""
import argparse, json, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

LABEL = {"baseline": "No skill", "v1": "v1", "v2": "v2", "v2.1": "v2.1", "v3": "v3", "v3.1": "v3.1", "v4": "v4", "v4.1": "v4.1"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--key", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--wait", type=int, default=3000, help="ms to wait so simulated loading finishes")
    a = ap.parse_args()

    results, out = pathlib.Path(a.results), pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    key = {k["code"]: k for k in json.loads(pathlib.Path(a.key).read_text())}
    shots = {}  # case -> condition -> path

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for code, k in sorted(key.items()):
            htmls = sorted((results / code).rglob("*.htm*"))
            if not htmls:
                continue
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(htmls[0].resolve().as_uri())
            page.wait_for_timeout(a.wait)
            name = f"{k['case']}-{LABEL[k['condition']].replace(' ', '-').lower()}-{code}"
            page.screenshot(path=str(out / f"{name}.png"))
            page.screenshot(path=str(out / f"{name}-full.png"), full_page=True)
            page.close()
            shots.setdefault(k["case"], {})[k["condition"]] = out / f"{name}.png"
            print("shot", name)
        browser.close()

    # side-by-side per case
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 36)
    except OSError:
        font = ImageFont.load_default()
    for case, by_cond in shots.items():
        conds = [c for c in ("baseline", "v1", "v2", "v2.1", "v3", "v3.1", "v4", "v4.1") if c in by_cond]
        imgs = [Image.open(by_cond[c]) for c in conds]
        w, h = imgs[0].size
        bar = 70
        canvas = Image.new("RGB", (w * len(imgs) + 20 * (len(imgs) - 1), h + bar), "white")
        d = ImageDraw.Draw(canvas)
        for i, (c, im) in enumerate(zip(conds, imgs)):
            x = i * (w + 20)
            canvas.paste(im, (x, bar))
            d.text((x + 16, 16), LABEL[c], fill="black", font=font)
        canvas.save(out / f"{case}-side-by-side.png", optimize=True)
        print("compare", case)


if __name__ == "__main__":
    main()
