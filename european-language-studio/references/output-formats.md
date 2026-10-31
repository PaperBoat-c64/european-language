# Output Formats

The skill produces three files from one learning document: `.json`, `.html`, `.docx`.

## Table of contents
1. [The three files](#the-three-files)
2. [HTML structure](#html-structure)
3. [DOCX structure](#docx-structure)
4. [JSON shape](#json-shape)
5. [Rendering command](#rendering-command)

## The three files

| file | purpose | produced by |
|---|---|---|
| `<stem>.json` | the machine-readable learning document (the source of truth) | you, in Step 9 |
| `<stem>.html` | interactive web page, Apple-Music-styled | `scripts/render_packet.py` |
| `<stem>.docx` | static study document for printing/offline | `scripts/render_packet.py` |

`<stem>` is a short filename from the text (e.g. `la-noche`, `les-miserables-excerpt`).

## HTML structure

Seven tabs, rendered from the JSON by `scripts/render_packet.py` + `assets/templates/packet.html`:

1. **Reading** — the plain source text.
2. **Annotated** — the source with vocabulary `surface` occurrences highlighted; each token's color is assigned from the palette by reading order and matched by exact substring.
3. **Vocabulary** — one card per record (meaning, morphology, collocations, examples, errors/confusions, region).
4. **Expressions** — expression records with literal vs. contextual meaning, register, region, sensitivity.
5. **Grammar** — grammar records with pattern and examples.
6. **Exercises** — exercise records with a separate answer key.
7. **Cards** — flashcards derived automatically from vocabulary + expressions (front = surface/text, back = meaning).

The page also carries a theme toggle (light / dark / system). No word-level segment data is needed — highlighting is computed from `surface` substrings.

## DOCX structure

A static document with the same content in linear form:

- Title + meta table (language, level, genre, register, date).
- Source text (full).
- Sentence-aligned translation (table: original / translation / literal / note).
- Vocabulary table + detail blocks.
- Expressions.
- Grammar.
- Exercises + answer key.

Generated with `python-docx`; if that library is unavailable, `render_packet.py` falls back to a minimal OOXML writer so a valid `.docx` is always produced.

## JSON shape

One object, top-level keys in this order: `schemaVersion`, `meta`, `source`, `sentences`, `vocabulary`, `expressions`, `grammar`, `exercises`, `qa`. The exact contract is `schemas/learning-document.schema.json`.

Key invariants:
- `meta.textLanguage` is one of `en fr es de it pt nl sv no da`.
- `meta.explanationLanguage` is the explanation language (default `en`).
- `source.text` is the verbatim input.
- `sentences[].id` is `s<para>-<sent>`; cross-references point at vocabulary/expression/grammar IDs.
- `qa` holds the quality-check results (empty array until the QA step fills it).

## Rendering command

```bash
python3 scripts/render_packet.py \
  --data <stem>.json \
  --output-dir <dir> \
  --stem <stem> \
  --palette default \
  --html --docx
```

Palettes: `default` (default.json), `pastel` (pastel.json), `high-contrast` (high-contrast.json).
