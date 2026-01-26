#!/usr/bin/env python3
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLORS_DIR = ROOT / "colors"
COLORS_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    palettes_path = ROOT / "lua" / "bearded" / "palettes" / "generated.lua"
    if not palettes_path.exists():
        raise SystemExit("palettes missing; run scripts/export-palettes.py first")

    # Parse generated.lua slugs by simple scan to avoid requiring Lua
    slugs = []
    for line in palettes_path.read_text().splitlines():
        line = line.strip()
        if line.startswith('["') and '"]' in line and "=" in line:
            slug = line.split('"')[1]
            slugs.append(slug)

    base = """local ok, bearded = pcall(require, "bearded")
if not ok then
  return
end
bearded.load("%s")
"""

    for slug in slugs:
        target = COLORS_DIR / f"bearded-{slug}.lua"
        target.write_text(base % slug, encoding="utf-8")

    # Root colorscheme remains 'bearded'
    print(f"Wrote {len(slugs)} colorscheme files to {COLORS_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
