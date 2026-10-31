#!/usr/bin/env python3
"""Self-check for the european-language-studio skill.

Verifies that every file referenced by SKILL.md exists, that the JSON schema
parses, that palettes are well-formed, and that the renderer/validator are
syntactically valid. Non-destructive; reads only.

Usage:
    python3 check_skill_assets.py            # from anywhere; resolves skill dir
    python3 check_skill_assets.py /path/to/skill
"""

import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
if len(sys.argv) > 1:
    SKILL_DIR = Path(sys.argv[1]).resolve()

LANGUAGES = ["en", "fr", "es", "de", "it", "pt", "nl", "sv", "no", "da"]

LANG_FILENAMES = {
    "en": "english", "fr": "french", "es": "spanish", "de": "german",
    "it": "italian", "pt": "portuguese", "nl": "dutch", "sv": "swedish",
    "no": "norwegian", "da": "danish",
}

errors = []
warnings = []


def note_error(msg):
    errors.append(msg)


def note_warning(msg):
    warnings.append(msg)


def exists(rel, required=True):
    p = SKILL_DIR / rel
    ok = p.is_file()
    if not ok and required:
        note_error(f"missing required file: {rel}")
    return ok


# --- 1. SKILL.md present and has valid frontmatter ---
skill_md = SKILL_DIR / "SKILL.md"
if not skill_md.is_file():
    note_error("missing SKILL.md")
else:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---"):
        note_error("SKILL.md has no YAML frontmatter")
    else:
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            note_error("SKILL.md frontmatter not closed")
        else:
            fm = m.group(1)
            if "name:" not in fm:
                note_error("SKILL.md frontmatter missing `name:`")
            if "description:" not in fm:
                note_error("SKILL.md frontmatter missing `description:`")

# --- 2. Schema parses and has expected pieces ---
schema_rel = "schemas/learning-document.schema.json"
if exists(schema_rel):
    try:
        schema = json.loads((SKILL_DIR / schema_rel).read_text(encoding="utf-8"))
        if schema.get("$schema", "").find("2020-12") == -1:
            note_warning("schema does not declare Draft 2020-12")
        langs = schema.get("$defs", {}).get("meta", {}).get("properties", {}).get("textLanguage", {}).get("enum")
        if langs is None:
            note_error("schema meta.textLanguage has no enum")
        elif set(langs) != set(LANGUAGES):
            note_error(f"schema textLanguage enum mismatch: {sorted(langs)} != {LANGUAGES}")
    except json.JSONDecodeError as e:
        note_error(f"schema is invalid JSON: {e}")

# --- 3. Palettes well-formed ---
for name in ["default", "pastel", "high-contrast"]:
    rel = f"assets/palettes/{name}.json"
    if exists(rel):
        try:
            pal = json.loads((SKILL_DIR / rel).read_text(encoding="utf-8"))
            colors = pal.get("colors")
            if not isinstance(colors, list) or not colors:
                note_error(f"palette {name} has no non-empty colors list")
            else:
                hex_re = re.compile(r"^#[0-9a-fA-F]{6}$")
                if not all(hex_re.match(c) for c in colors):
                    note_error(f"palette {name} has a non-hex color")
        except json.JSONDecodeError as e:
            note_error(f"palette {name} is invalid JSON: {e}")

# --- 4. Template present and placeholders intact ---
tpl_rel = "assets/templates/packet.html"
if exists(tpl_rel):
    tpl = (SKILL_DIR / tpl_rel).read_text(encoding="utf-8")
    for ph in ["{{TITLE}}", "{{PACKET_JSON}}", "{{PALETTE_JSON}}", 'id="packet-data"', 'id="palette-data"']:
        if ph not in tpl:
            note_error(f"template missing placeholder/marker: {ph}")

# --- 5. Scripts present and syntactically valid ---
for rel in ["scripts/render_packet.py", "scripts/validate_document.py"]:
    if exists(rel):
        try:
            compile((SKILL_DIR / rel).read_text(encoding="utf-8"), rel, "exec")
        except SyntaxError as e:
            note_error(f"{rel} has a syntax error: {e}")

# --- 6. All files referenced from SKILL.md exist ---
if skill_md.is_file():
    refs = re.findall(r"(?:prompts|references|scripts|languages)/[\w./-]+\.(?:md|py|json|html)", text)
    for ref in sorted(set(refs)):
        if not (SKILL_DIR / ref).is_file():
            note_error(f"SKILL.md references missing file: {ref}")

# --- 7. Language files present for all 10 ---
for code in LANGUAGES:
    rel = f"languages/{LANG_FILENAMES[code]}.md"
    if not (SKILL_DIR / rel).is_file():
        note_error(f"missing language file: {rel}")

# --- report ---
print(f"Skill dir: {SKILL_DIR}")
if errors:
    print(f"\nFAIL — {len(errors)} error(s):")
    for e in errors:
        print(f"  [error] {e}")
if warnings:
    print(f"\n  {len(warnings)} warning(s):")
    for w in warnings:
        print(f"  [warn] {w}")
if not errors and not warnings:
    print("\nOK — all checks passed.")

sys.exit(1 if errors else 0)
