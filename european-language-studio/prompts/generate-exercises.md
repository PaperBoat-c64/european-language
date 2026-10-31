# Prompt — Generate Exercises

Used in Step 8. Exercises test what the packet taught, using this text.

## When to use

After grammar notes, or on request ("quiz me", "make exercises").

## Required inputs

- Segmented source with translations
- Vocabulary, expression, and grammar records with IDs
- `{{LEARNER_LEVEL}}`
- `{{EXERCISE_TYPES}}` — optional constraint

## Prompt

```text
You are creating exercises for a learner who has just studied this {{TEXT_LANGUAGE}} text.

Level: {{LEARNER_LEVEL}} (default: B1)
Explanation language: {{EXPLANATION_LANGUAGE}}

Taught items:
{{VOCABULARY_AND_EXPRESSIONS_AND_GRAMMAR}}

Source:
"""
{{SEGMENTED_SOURCE}}
"""

Choose exercise types appropriate to the level. Available types:
meaning | cloze | collocation | rewrite | grammar-discrimination | translation | imitation | speaking-scenario | recall-card

Requirements:
- Produce 5–10 items depending on text length.
- Use at least three different types when the material supports it.
- Every item must reference the item(s) it tests (v003 / e001 / g002 / sentence ID).
- Every item must have a checkable answer or an explicit rubric.
- Do not test something not taught in the packet.
- Do not reuse the packet's example sentence verbatim as the exercise sentence.
- For cloze, mark the blank as {{blank}}; remove exactly one target unit and preserve the rest of the sentence; the blank must be inferable from context.
- For multiple choice, all distractors must be plausible and only one correct; say why each distractor is wrong in the explanation.
- For open production, give 2–3 rubric criteria.

For each item:
- id: x001
- type
- prompt
- options (if any)
- answer: key (closed) or model + rubric (open)
- explanation
- related refs
- difficulty: easy | medium | hard

Then provide an answer key section, separated from the questions.

Do not create trick questions or ambiguous items. If an item has two defensible answers, redesign it or accept both explicitly.
```

## Output contract

Exercise records + answer key. Each answer checkable; each item mapped to a taught record.

## Self-check

- [ ] Every prompt is unambiguous.
- [ ] Exactly one correct answer for closed items (or both accepted explicitly).
- [ ] Open items have rubrics with ≥2 criteria.
- [ ] Answer key present and separated.
- [ ] Every item references an existing taught item.
- [ ] No exercise tests untaught material.
- [ ] Distractors are plausible and explained.
- [ ] Difficulty spread is reasonable.
