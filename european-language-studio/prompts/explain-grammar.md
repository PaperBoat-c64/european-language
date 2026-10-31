# Prompt — Explain Grammar

Used in Step 7. Produces grammar records tied to sentences.

## When to use

After expressions, or on request ("explain the grammar here").

## Required inputs

- Segmented source with translations
- `{{TEXT_LANGUAGE}}` and its language rules
- `{{LEARNER_LEVEL}}`
- Existing vocabulary/expression records (to avoid repeating)

## Prompt

```text
You are explaining grammar in a {{TEXT_LANGUAGE}} text to a learner.

Level: {{LEARNER_LEVEL}} (default: B1)
Explanation language: {{EXPLANATION_LANGUAGE}}

Source:
"""
{{SEGMENTED_SOURCE}}
"""

Select 3–6 grammar points that are actually instantiated. A point qualifies if:
- misunderstanding it would cause a misreading of this sentence; or
- it is productive: the learner will need it to write similar sentences; or
- it is a contrast a learner at this level reliably gets wrong (tense/aspect, case, pronoun reference, word order, agreement).

Do not include a point because it is famous, advanced, or exam-listed. Do not include a point that is already fully covered by a vocabulary morphology note.

For each point, output:
- id: g001
- title: the phenomenon in learner terms (e.g. "passato prossimo vs. imperfetto", "the separable-verb bracket", "ser vs. estar")
- explanation: the rule, then how it applies to the quoted sentence. Two short paragraphs maximum.
- pattern: optional schematic, e.g. "essere/avere + participio passato", "subordinate clause → verb-final"
- examples: 1–2 minimal examples built from the text's own vocabulary
- pitfalls: real errors learners make with this structure in this language
- sentenceRefs: existing sentence IDs
- confidence / needsVerification

Rules:
- Every rule must be true for this language. Do not transfer English categories.
- Every explanation must quote or point to the actual sentence.
- If the text shows an unusual or disputed construction, say so rather than inventing a rule.
- No level labels, no frequency claims.
- Prefer one precise paragraph over five vague ones.

Output:
### g001 · {title}
{explanation}
- pattern: `{pattern}`
- examples: …
- pitfalls: …
- sentence refs: s01-02
```

## Output contract

3–6 grammar records, each with sentence references, correct for that language.

## Self-check

- [ ] Each rule is correct for the language.
- [ ] Each rule applies to the quoted span.
- [ ] No English grammatical categories applied where they do not fit.
- [ ] No duplication with vocabulary morphology.
- [ ] Pitfalls are real learner errors.
- [ ] No CEFR/frequency claims.
- [ ] Sentence refs exist.
