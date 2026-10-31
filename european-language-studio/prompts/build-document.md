# Prompt — Build Document

Used in Step 9. Assembles the finished learning document JSON from the outputs of steps 1–8.

## When to use

Always, after grammar/exercises, before rendering.

## Required inputs

- The verbatim source
- Sentences with IDs and translations (step 2–4)
- Vocabulary records (step 5)
- Expression records (step 6)
- Grammar records (step 7)
- Exercise records (step 8)
- The QA results (step 10, filled in after assembly)

## Prompt

```text
Assemble a complete learning document as one JSON object conforming to
schemas/learning-document.schema.json (schemaVersion "2.0").

Inputs:
Source (verbatim):
"""
{{SOURCE}}
"""

Sentences: {{SENTENCES}}
Vocabulary: {{VOCABULARY}}
Expressions: {{EXPRESSIONS}}
Grammar: {{GRAMMAR}}
Exercises: {{EXERCISES}}
Text language: {{TEXT_LANGUAGE}}
Explanation language: {{EXPLANATION_LANGUAGE}}

Build the object with these top-level keys, in this order:
schemaVersion, meta, source, sentences, vocabulary, expressions, grammar, exercises, qa.

Rules:
1. meta.title — a short title from the first line; textLanguage and explanationLanguage as given; genre; register; mode "study"; createdAt (ISO-8601); level.strategy "default-adaptive" (or "user-specified" with declared level).
2. source — text exactly as supplied; characterCount and sentenceCount computed; integrity "preserved" (or "whitespace-normalized" with normalizationNotes).
3. sentences — every sentence from step 2, in reading order, with id (s<para>-<sent>), paragraph, verbatim text, natural translation, optional literal, and vocabularyRefs / expressionRefs / grammarRefs pointing at the records whose surface occurs in that sentence.
4. vocabulary / expressions / grammar / exercises — the records from steps 5–8, ids sequential in reading order.
5. Cross-references must resolve: every ref points at an existing id. Every vocabulary.surface and expression.text is an exact substring of at least one referenced sentence.
6. qa — leave checks as an empty array; it is filled by the quality-review step before final delivery.

Emit ONLY the JSON object. No markdown fences, no prose.
```

## Output contract

One valid JSON object. `scripts/validate_document.py` must report PASS.

## Self-check

- [ ] All top-level keys present and in schema order.
- [ ] No dangling references.
- [ ] Every `surface` / `text` verbatim in its sentence.
- [ ] Sentence concatenation equals the source (ignoring whitespace).
- [ ] Valid JSON — no trailing commas, no comments.
