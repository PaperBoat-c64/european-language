# Prompt — Translate Contextually

Used in Steps 3–4. Produces the whole-text translation and the sentence-aligned pairs.

## When to use

After segmentation. Also on request ("translate this and explain why").

## Required inputs

- `{{SEGMENTED_SOURCE}}` — paragraphs and sentences with IDs
- `{{TEXT_LANGUAGE}}` / `{{EXPLANATION_LANGUAGE}}`
- `{{GENRE}}`, `{{REGISTER}}`
- `{{GLOSSARY}}` — optional running term decisions

## Prompt

```text
You are translating an authentic {{TEXT_LANGUAGE}} text into {{EXPLANATION_LANGUAGE}} for a learner.

Genre: {{GENRE}}
Register: {{REGISTER}}
Established glosses (reuse unless context demands otherwise): {{GLOSSARY}}

Source, segmented:
"""
{{SEGMENTED_SOURCE}}
"""

Produce:

A. A whole-text translation, paragraph-aligned with the source. Natural {{EXPLANATION_LANGUAGE}}, same register, no added commentary, no omitted sentences.

B. A one-to-one sentence alignment. For each sentence ID:
   - the original, copied exactly (do not fix spelling or punctuation);
   - the natural translation;
   - only where useful, a literal gloss that shows the source construction;
   - a note only for ambiguity, register, or a construction the translation cannot carry.

Translation rules:
1. Propositional meaning first, then illocution, then register, then imagery. Never sacrifice meaning for word order.
2. Do not translate idioms word-for-word. Translate their function; put the image in a note if it matters.
3. Preserve tense/aspect, modality, negation, hedges, and stance.
4. Keep names, numbers, dates, and quotations as they are.
5. Do not merge or split sentences in the aligned view.
6. Preserve the source's apostrophes, quotation marks, and every accent/`¿¡`/`ß`/`æøå`/`ç`/`ñ` inside quoted text.
7. If a sentence is genuinely ambiguous, choose the supported reading and flag the alternative. Do not silently pick.
8. If the source contains an error, translate what it says and flag the error; do not correct it.
9. Do not use the explanation language's cultural defaults to replace the source's.

Also return:
- a short list of translation decisions that a learner would not infer (why this sense, why this register);
- anything you could not preserve, stated plainly.

Output:
## Whole-text translation
{paragraphs}

## Aligned translation
**s01-01**
Original: …
Translation: …
Literal (optional): …
Note (optional): …

## Decisions
- …

## Losses
- …
```

## Output contract

Every input sentence ID appears exactly once in the aligned section. The whole-text translation covers every source paragraph. Notes are sparse.

## Self-check

- [ ] Count(sentences) == Count(aligned pairs).
- [ ] No source sentence missing or duplicated.
- [ ] Idioms not literal in the main translation.
- [ ] Register matches.
- [ ] No added facts or commentary inside the translation.
- [ ] Ambiguities flagged, not hidden.
- [ ] Unicode and accents intact.
