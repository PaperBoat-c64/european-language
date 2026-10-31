# Prompt — Extract Expressions

Used in Step 6. Produces expression records per `references/idioms-and-slang.md`.

## When to use

After vocabulary selection, or on request ("what idioms are in here?").

## Required inputs

- Segmented source with translations
- `{{TEXT_LANGUAGE}}` and language rules
- Optional: learner level, existing vocabulary records (to avoid duplication)

## Prompt

```text
You are extracting fixed expressions from a {{TEXT_LANGUAGE}} text for a learner.

Explanation language: {{EXPLANATION_LANGUAGE}}
Already-glossed vocabulary (do not duplicate): {{VOCAB_IDS_OR_TERMS}}

Text:
"""
{{SEGMENTED_SOURCE}}
"""

Apply the taxonomy and tests in references/idioms-and-slang.md:
collocation | phrasal-verb | idiom | colloquialism | slang | valency | grammatical-expression

For each candidate, run the decision procedure and record which test it passed.
Include an item only if at least one holds:
- non-compositional meaning a learner would misread;
- a collocation strong enough that a synonym sounds foreign;
- register or region that would cause a social error;
- a valency pattern needed for correct production.

Do NOT include:
- ordinary syntax or transparent compounds;
- one-off poetic images;
- items that duplicate a vocabulary record;
- items added to reach a count.

For each expression, output:
- id: e001 (reading order)
- text: verbatim span, same inflection as the source
- type: one of the taxonomy values
- literalMeaning: required for idioms/slang where it differs; else optional
- meaningInContext: functional meaning in {{EXPLANATION_LANGUAGE}}
- register: formal | neutral | informal | colloquial | vulgar | literary | archaic | mixed
- region: [] unless evidenced; regionCertainty: verified | probable | unverified
- sensitivity: none | mild | offensive | slur
- usageNotes: constraints, who may use it, regional caveats
- examples: 1–2 original sentences + translation
- alternatives: equivalent or similar expressions
- priority: high | medium | low
- confidence: high | medium | low
- needsVerification: true iff regional/slang/disputed
- sentenceRefs: existing IDs

If nothing qualifies, say exactly:
"No high-value fixed expressions or slang found in this text worth separate treatment." and give one sentence explaining why.
Do not fabricate items to fill the section.

Never claim an expression is "used everywhere", "very common", or "universal" without evidence.
```

## Output contract

Expression records + a one-line extraction verdict. Counts proportionate to text length (roughly 2–8 for a 5–10 sentence text).

## Self-check

- [ ] Every `text` occurs verbatim in the source.
- [ ] Type passes the taxonomy tests.
- [ ] Idioms/slang have literal vs. contextual meaning separated.
- [ ] Every item has a register.
- [ ] Regional claims have evidence or are marked unverified.
- [ ] Sensitivity set for vulgar/offensive items.
- [ ] No duplicates with vocabulary records.
- [ ] Empty section stated explicitly, not padded.
