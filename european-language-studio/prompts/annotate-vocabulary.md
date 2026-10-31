# Prompt — Annotate Vocabulary

Used in Step 5. Produces vocabulary records per `references/annotation-schema.md`.

## When to use

After alignment, or on request ("gloss the hard words").

## Required inputs

- `{{SEGMENTED_SOURCE}}` with translations
- `{{TEXT_LANGUAGE}}` and its `languages/<code>.md`
- `{{LEARNER_LEVEL}}` (default adaptive)
- `{{EXISTING_GLOSSARY}}` — avoid duplicates

## Prompt

```text
You are annotating vocabulary for a {{TEXT_LANGUAGE}} learner reading this text.

Level: {{LEARNER_LEVEL}} (if unknown, target a B1 reader and rank by priority)
Explanation language: {{EXPLANATION_LANGUAGE}}

Text with IDs and translations:
"""
{{SEGMENTED_SOURCE}}
"""

Language rules to follow: {{LANGUAGE_RULES_SUMMARY}}

Select 5–20 items worth learning. Selection criteria (in order):
1. The meaning in context differs from the most obvious dictionary sense.
2. The form is irregular or opaque from the lemma.
3. The word is a false friend or a common learner error.
4. The word's grammar matters in this sentence (valency, agreement, case, separable prefix).
5. The word is useful and appears in a learnable context.

Do not select: function words unless the text turns on them; proper nouns unless they carry cultural information; transparent regular forms; words already explained as expressions.

For each item, output:
- id: v001 (sequential, reading order)
- surface: exact substring of its sentence, including inflection and clitics (this field drives word highlighting — it MUST match the sentence verbatim)
- lemma: dictionary citation form
- pos: part of speech in this sentence
- meaningInContext: one sentence, in {{EXPLANATION_LANGUAGE}}, selecting ONE sense
- morphology: description + features (only if non-trivial)
- gender: for gendered nouns
- pronunciation: IPA only when it disambiguates; do not guess
- collocations: 2–4 natural partners
- examples: 1–2 original sentences + translations
- commonErrors / confusions: only real ones
- sentenceRefs: existing sentence IDs
- priority: high | medium | low
- confidence: high | medium | low
- needsVerification: true iff slang/regional/disputed/damaged source
- tags: optional

Rules:
- Never fabricate a definition, frequency, CEFR level, or etymology.
- Do not call an inflected form a new lexeme.
- Do not pad: if only 7 items are worth teaching, return 7.
- Explain morphology only where the learner cannot derive it.
- Every example must be natural and must not copy the source sentence unless the source is the model.

Output a Markdown table plus one detail block per item.
```

## Output contract

Vocabulary records with all required fields. Every `surface` verifiably occurs in its sentence. At most one third marked `high`.

## Self-check

- [ ] `surface` found in the sentence (exact, same glyphs).
- [ ] `lemma` is a citation form.
- [ ] `meaningInContext` picks one sense and fits this sentence.
- [ ] Morphology only where non-trivial; agreement/auxiliary/case trigger stated.
- [ ] No dictionary dumps.
- [ ] No fabricated frequency/CEFR.
- [ ] Priorities distributed; no duplicate lexemes.
