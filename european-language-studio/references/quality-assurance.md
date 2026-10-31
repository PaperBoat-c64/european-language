# Quality Assurance — The 11 Checks

Run all of these before delivering. The validator (`scripts/validate_document.py`) automates C01–C07 mechanically; C08–C11 need your judgment.

## Table of contents
1. [The checks](#the-checks)
2. [How to run](#how-to-run)
3. [Fixing failures](#fixing-failures)

## The checks

| id | check | what it catches |
|---|---|---|
| C01 | **Source fidelity** | the `source.text` matches the user's input verbatim; no silent edits |
| C02 | **Sentence integrity** | concatenating all sentences (paragraph by paragraph) reconstructs the source |
| C03 | **Surface integrity** | every `vocabulary.surface` and `expression.text` is a verbatim substring of its referenced sentence |
| C04 | **Cross-reference resolution** | every `sentenceRefs` / `vocabularyRefs` / `expressionRefs` / `grammarRefs` points at an existing ID |
| C05 | **ID uniqueness + format** | IDs unique per collection and match `^v\d{3,4}$`, `^s\d{2,4}-\d{2,4}$`, `^e\d{3,4}$`, `^g\d{3,4}$`, `^x\d{3,4}$` |
| C06 | **Schema conformance** | the JSON is valid and satisfies `schemas/learning-document.schema.json` |
| C07 | **No dangling / orphan records** | a record whose `sentenceRefs` do not resolve is rejected; a sentence whose refs point nowhere is warned |
| C08 | **No invention** | no fabricated definition, frequency, CEFR level, etymology, region claim, or author/culture fact |
| C09 | **Context over dictionary** | each `meaningInContext` fits *this* sentence, not a generic dictionary sense |
| C10 | **Layer meanings** | idioms have literal vs. contextual meaning separated; morphology only where non-trivial; nothing padded |
| C11 | **Uncertainty flagged** | anything slang/regional/disputed/ambiguous carries `needsVerification` or a note, never presented as certain |

## How to run

```bash
python3 scripts/validate_document.py <packet.json> [--source <original.txt>] [--strict]
```

- exit `0` = PASS
- exit `1` = FAIL (blocking)
- exit `2` = WARN (non-blocking; review manually)

The renderer (`scripts/render_packet.py`) does not re-validate — always validate before rendering.

## Fixing failures

- **C01/C02 fail** → the source was altered. Restore the verbatim text and re-derive sentences from it.
- **C03 fail** → the `surface`/`text` no longer matches the sentence (case, accent, or wording drifted). Copy the substring straight from the sentence.
- **C04/C05/C07 fail** → fix IDs and refs; renumber in reading order if needed.
- **C08–C11 are judgment checks** → walk each record and answer: "where did I get this from? does the text support it?" Delete or flag anything unsupported.

After any fix, re-run the validator and re-render. The HTML and DOCX must be regenerated from the *same* corrected JSON.
