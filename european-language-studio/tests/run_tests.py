#!/usr/bin/env python3
"""End-to-end smoke test for european-language-studio.

Runs:
  1. scripts/check_skill_assets.py   — skill completeness
  2. scripts/validate_document.py    — over every example packet
  3. scripts/render_packet.py        — HTML + DOCX for every example packet

Usage:
    python3 tests/run_tests.py
"""

import subprocess
import sys
import tempfile
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
EXAMPLES = SKILL_DIR / "examples"

failures = []


def run(cmd, cwd=None):
    print(f"\n$ {' '.join(str(c) for c in cmd)}")
    r = subprocess.run([str(c) for c in cmd], cwd=str(cwd or SKILL_DIR),
                       capture_output=True, text=True)
    if r.stdout:
        print(r.stdout)
    if r.stderr:
        print(r.stderr)
    return r


# 1. skill self-check
r = run([sys.executable, "scripts/check_skill_assets.py"])
if r.returncode != 0:
    failures.append("check_skill_assets")

# 2. examples
examples = sorted(EXAMPLES.glob("*.json")) if EXAMPLES.is_dir() else []
if not examples:
    print("\nNo example packets found in examples/ — skipping validate/render.")
else:
    for ex in examples:
        r = run([sys.executable, "scripts/validate_document.py", ex, "--strict"])
        if r.returncode not in (0, 2):  # strict warnings (2) are acceptable in smoke test
            failures.append(f"validate:{ex.name}")

        with tempfile.TemporaryDirectory() as tmp:
            r = run([
                sys.executable, "scripts/render_packet.py",
                "--data", ex,
                "--output-dir", tmp,
                "--stem", ex.stem,
                "--palette", "default",
                "--html", "--docx",
            ])
            if r.returncode != 0:
                failures.append(f"render:{ex.name}")
                continue
            html = Path(tmp) / f"{ex.stem}.html"
            docx = Path(tmp) / f"{ex.stem}.docx"
            if not html.is_file():
                failures.append(f"render:{ex.name} (no .html)")
            if not docx.is_file():
                failures.append(f"render:{ex.name} (no .docx)")

print("\n" + "=" * 60)
if failures:
    print(f"FAIL — {len(failures)} failure(s):")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("PASS — all smoke tests succeeded.")
