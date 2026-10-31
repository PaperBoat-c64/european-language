---
name: european-language-studio
description: Turns an authentic European-language text (English, French, Spanish, German, Italian, Portuguese, Dutch, Swedish, Norwegian, or Danish) into a rich interactive study packet — an Apple-Music-styled HTML page with tabs for reading, word-annotated text, vocabulary cards, expressions, grammar, exercises, and flashcards, plus a DOCX study document and the underlying JSON. Use when the user pastes, uploads, or points to a text in one of these languages and asks to study it, read it closely, translate it with explanations, annotate vocabulary, learn expressions, explain grammar, make exercises or flashcards, or generate a study web page / study document.
---

# European Language Studio

Turn an authentic European-language text into a self-contained study packet: an interactive HTML page (color-coded annotated reading, vocabulary cards, expressions, grammar, exercises, flashcards) and a matching DOCX study document. The learner reads the original; the packet makes it legible and drills it.

## Non-negotiables

1. **Source fidelity.** Quote the source verbatim in `sentences[].text`. Never delete, reorder, merge, correct, modernize, or sanitize it. Keep paragraph order, punctuation, capitalization, sentence boundaries, and every accent/`ß`/`æ`/`ø`/`å`/`ç`/`ñ`. If a typo or oddity is in the source, keep it and flag it in `notes` — do not silently fix it.
2. **No invention.** Never fabricate definitions, frequency data, CEFR levels, etymology, regional use, or grammar rules. If a claim cannot be grounded in the text plus reliable knowledge, omit it or mark `confidence: "low"` and `needsVerification: true`.
3. **Context over dictionary.** Every gloss answers "what does it mean *here*". For multi-sense words, say why this sense applies in this sentence.
4. **Layer meanings.** For idioms and slang, report literal meaning, contextual meaning, and connotation separately. Never translate an idiom word-for-word as if it were literal.
5. **No padding.** Extract only what is worth learning for this text and level. If there is no high-value slang or idiom, say so explicitly rather than inventing items.
6. **Flag uncertainty as content.** Low-confidence items stay in the packet with their flags; silent confidence is a defect.

## Step 0 — Parameters (decide, don't interrogate)

Determine these from the request; do not run a questionnaire.

| Parameter | Source | Default |
|---|---|---|
| `textLanguage` | The text itself | Detect silently; if genuinely mixed, ask once which is primary |
| `explanationLanguage` | User's language | **English**; follow the user if they write in another language |
| Learner level | User statement | **Default-adaptive** (below) |
| Output mode | User request | `study` (always HTML + DOCX) |
| Genre | The text | `other` |

**Default-adaptive level policy** (when level is unspecified): do not ask "what is your level?" and do not stall. Instead:

- Gloss everything non-obvious for a B1 reader, but keep notes tight.
- Explain grammar only where the text actually hinges on it (tense choice, word order, agreement, pronoun reference).
- Give every item a `priority` so a stronger reader can skip the basics, and every analysis item a `confidence`.
- If the user later reveals a level, adjust depth on the next pass; do not silently regenerate prior output.

Ask at most one clarifying question per run, and only when ambiguity would corrupt the output (primary language of a mixed text; whether a text is meant to be treated as prose or verse). Otherwise proceed and state assumptions in one line.

## Step 1 — Workflow

Run these in order. Each step names the file to read when it is needed — do not preload everything.

1. **Analyze** — language, genre, register, difficulty signals, teaching targets. Read `prompts/analyze-text.md`; load `languages/<code>.md` for the detected language.
2. **Preserve & segment** — split into paragraphs and sentences; assign stable IDs `s<paragraph>-<sentence>` (e.g. `s01-03`). Follow the Segmentation section of `languages/<code>.md`.
3. **Translate whole** — natural, context-aware full translation into the explanation language. Read `references/translation-principles.md` and `prompts/translate-contextually.md`.
4. **Align** — per-sentence original + translation, with a literal rendering only where it clarifies.
5. **Annotate vocabulary** — surface form, lemma, POS, contextual sense, morphology, collocations, examples, pitfalls, priority, confidence. Read `references/annotation-schema.md` and `prompts/annotate-vocabulary.md`.
6. **Extract expressions** — collocations, phrasal verbs, idioms, colloquialisms, slang, valency patterns, grammatical fixed expressions. Read `references/idioms-and-slang.md` and `prompts/extract-expressions.md`.
7. **Explain grammar** — only structures that matter for understanding or production here. Read `prompts/explain-grammar.md`.
8. **Exercises** — grounded in this text's actual teaching points. Read `prompts/generate-exercises.md`.
9. **Build the document** — assemble the JSON conforming to `schemas/learning-document.schema.json`. Read `prompts/build-document.md`.
10. **Render & QA** — write the JSON to disk, render HTML + DOCX with `scripts/render_packet.py`, run every check in `references/quality-assurance.md`, fix the failing stage only.

For very short texts (a sentence or two) merge steps 2–4 and 6–7. For long texts, batch by paragraph blocks (below).

## Language files

Load exactly one, matching `textLanguage`:

- `languages/english.md` · `languages/french.md` · `languages/spanish.md` · `languages/german.md`
- `languages/italian.md` · `languages/portuguese.md` · `languages/dutch.md`
- `languages/swedish.md` · `languages/norwegian.md` · `languages/danish.md`

They carry language-specific morphology, agreement, word-order, register, and segmentation rules. Never apply one language's grammar rules to another.

## The learning document (JSON)

The packet is one object conforming to `schemas/learning-document.schema.json` (single self-contained schema). Structure:

- `meta` — title, `textLanguage`, `explanationLanguage`, genre, register, level strategy.
- `source` — the verbatim text plus `characterCount`, `sentenceCount`, `integrity`.
- `sentences[]` — each with `id`, `paragraph`, verbatim `text`, natural `translation`, optional `literal`, and reference arrays `vocabularyRefs` / `expressionRefs` / `grammarRefs`.
- `vocabulary[]` — `surface`, `lemma`, `pos`, `meaningInContext`, `morphology`, `gender`, `pronunciation` (IPA), `collocations`, `examples`, `commonErrors`, `confusions`, `priority`, `confidence`, `needsVerification`, `sentenceRefs`.
- `expressions[]` — `text`, `type`, `literalMeaning`, `meaningInContext`, `register`, `region`, `regionCertainty`, `sensitivity`, `usageNotes`, `examples`, `alternatives`, `sentenceRefs`.
- `grammar[]` — `title`, `explanation`, `pattern`, `examples`, `pitfalls`, `sentenceRefs`.
- `exercises[]` — `type`, `prompt`, `options`, `answer` (key/model/rubric), `explanation`, `difficulty`, related refs.
- `qa` — the eleven checks with honest status.

Word-level color comes for free: the renderer assigns each vocabulary item a color from the palette (by reading order) and highlights every occurrence of its `surface` inside its sentences. The `surface` field must therefore be an exact substring of the sentence — the renderer relies on it.

## Rendering (HTML + DOCX)

Write the JSON to `<slug>.json`, then render:

```bash
python3 scripts/render_packet.py --data <slug>.json --output-dir . --stem <slug>
```

This writes `<slug>.html` (self-contained interactive page — no network, no build step) and `<slug>.docx` (a linear study document with the same content). The DOCX uses `python-docx` when installed and falls back to a minimal raw-XML document otherwise. See `references/output-formats.md`.

The HTML has seven tabs: **Reading** (clean side-by-side), **Annotated** (color-coded words; tap/hover for the full entry), **Vocabulary** (searchable, sortable cards), **Expressions**, **Grammar**, **Exercises** (reveal answers), and **Cards** (flip flashcards + Anki TSV export).

## Batching and ID stability

For long texts (roughly >60 sentences or >1,500 words), process in paragraph-aligned batches:

- Batch boundaries fall between paragraphs, never inside a sentence.
- IDs derive from absolute paragraph/sentence position, so they never shift between batches. Never renumber after the fact.
- Keep one shared terminology note across batches: if a word is glossed one way in batch 1, reuse it in batch 5 unless context genuinely differs (then say why).
- Merge batches in document order; run QA on the merged document.
- State batch boundaries in the output.

## File output

Every run writes three files into the working directory (or the `outputDir` the user names):

- `<slug>.json` — the learning document (the single source of truth).
- `<slug>.html` — the interactive page.
- `<slug>.docx` — the study document.

`<slug>` is a short lowercase slug from the title or first line (e.g. `le-petit-jardin`), reused across files and across sessions for the same text. After writing, tell the user the absolute paths. If the user explicitly wants terminal-only JSON (no rendering), follow that; otherwise render HTML + DOCX by default.

## Quality gate

Before delivering, run the eleven checks in `references/quality-assurance.md`: source integrity, alignment, lemma/form correctness, contextual sense, grammar accuracy, expression classification, register/region claims, redundancy, unsupported level/frequency claims, schema conformance (via `scripts/validate_document.py`), exercise answerability.

Fix only the failing stage, then re-run the affected checks. Report the QA result honestly: name anything marked `unverified` rather than implying it passed. If validation is impossible (e.g. the source was supplied only as an image), say what could not be verified.

```bash
python3 scripts/validate_document.py <slug>.json
```

## Copyright and length

Work from the text the user supplies. Do not reconstruct from memory book passages or articles the user has not provided. For long copyrighted works, quote only the passages under study and keep analysis proportionate.

## What this skill must not do

- Produce a translation without the aligned original.
- Present a "literal" gloss as the natural translation.
- Invent a CEFR level, frequency count, or "most common" claim.
- Assign a regional label to slang without evidence; when unsure, mark `regionCertainty: "unverified"`.
- Flatten a literary, ironic, or vulgar passage into neutral prose without saying so.
- Rewrite the source into "better" language.
- Ship a page or DOCX whose JSON fails `scripts/validate_document.py`.
