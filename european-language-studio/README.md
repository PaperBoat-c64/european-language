# european-language-studio

A Claude Code skill that turns an authentic European-language text into a rich interactive study packet: an Apple-Music-styled HTML page, a DOCX study document, and the underlying JSON.

Serving learners of European (Latin-script) languages:

English · French · Spanish · German · Italian · Portuguese · Dutch · Swedish · Norwegian · Danish

## What it does

Give it a short authentic text (a news paragraph, a story excerpt, a speech, song lyrics, a social post) in any of the ten languages, and it produces:

| file | what it is |
|---|---|
| `<stem>.json` | the full learning document — source, sentence-aligned translation, vocabulary, expressions, grammar, exercises, QA |
| `<stem>.html` | interactive page with 7 tabs: Reading, Annotated, Vocabulary, Expressions, Grammar, Exercises, Cards — plus light/dark/system theme |
| `<stem>.docx` | static study document for printing or offline review |

Explanations default to **English**; set `--language` (or ask) for another language.

## How to use

1. Paste or point to a text in one of the ten languages.
2. Ask to study it — e.g. *"make a study packet from this Spanish article"*.
3. The skill analyzes, segments, translates, annotates vocabulary, extracts expressions, explains grammar, and builds exercises.
4. It validates the JSON, then renders HTML + DOCX, and tells you where the three files are.

## Layout

```
european-language-studio/
├── SKILL.md                     # orchestration + non-negotiables
├── prompts/                     # the 8 step prompts (progressive disclosure)
├── references/                  # annotation schema, translation, idioms, QA, formats
├── languages/                   # per-language norm files (10)
├── schemas/
│   └── learning-document.schema.json
├── scripts/
│   ├── validate_document.py     # mechanical QA (C01–C07)
│   ├── render_packet.py         # JSON → HTML + DOCX
│   └── check_skill_assets.py    # skill self-check
├── assets/
│   ├── templates/packet.html    # the HTML template
│   └── palettes/                # default / pastel / high-contrast
├── examples/                    # validated sample packets
└── tests/
    └── run_tests.py
```

## Architecture

**Data + renderer separation.** Claude produces one JSON document conforming to `schemas/learning-document.schema.json`; deterministic Python renders it. No layout decisions are made inside the JSON — the renderer owns presentation, and word highlighting is computed by exact `surface` substring matching in the template's JavaScript.

## Quality gate

Every packet must pass the 11 checks in `references/quality-assurance.md` (C01–C11). `scripts/validate_document.py` enforces C01–C07 mechanically; C08–C11 are judgment checks.

## Self-check

```bash
python3 scripts/check_skill_assets.py
python3 tests/run_tests.py
```
