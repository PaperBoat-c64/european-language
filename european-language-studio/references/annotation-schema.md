# Annotation Schema — Vocabulary

This file defines the meaning of each vocabulary field in the learning document. The machine-readable contract is `schemas/learning-document.schema.json`; this file explains *how to fill each field correctly*.

## Table of contents
1. [Selection policy](#selection-policy)
2. [Field-by-field](#field-by-field)
3. [The surface contract](#the-surface-contract)
4. [Morphology](#morphology)
5. [Priority and confidence](#priority-and-confidence)

## Selection policy

Target 5–20 items per text, proportional to length and difficulty. For a short 5–8 sentence text, 6–10 items is right.

Select an item only when at least one of these holds, in this order of importance:

1. **Sense shift** — the meaning here differs from the most obvious dictionary sense (e.g. *still* as "nevertheless" vs. "motionless").
2. **Opaque form** — the inflected form cannot be derived from the lemma (e.g. *went* from *go*, *fuimos* from *ser/ir*).
3. **False friend / error magnet** — a word a learner of this language reliably misreads (e.g. *actual* for Spanish/English learners, *sensible* in French).
4. **Grammar matters here** — the word's valency, agreement, case, gender, or separable prefix is what makes the sentence work.
5. **Useful + learnable** — a productive word in a clear context.

Do **not** select:
- function words unless the whole text turns on one;
- proper nouns unless they carry cultural information the learner needs;
- transparent regular inflections (a regular plural is not a lexeme);
- anything already treated as an expression.

## Field-by-field

| field | meaning | rules |
|---|---|---|
| `id` | `v001`… in reading order | sequential, no gaps, no reuse |
| `surface` | exact substring of its sentence, inflection + clitics included | see [surface contract](#the-surface-contract) |
| `lemma` | dictionary citation form | infinitive for verbs, masculine singular nominative for adjectives/nouns |
| `pos` | part of speech in *this* sentence | n., v., adj., adv., prep., pron., det., conj., interj. |
| `meaningInContext` | one sense, one sentence, in the explanation language | exactly one sense; must fit *this* sentence, not a dictionary entry |
| `morphology` | description + features, only if non-trivial | see [morphology](#morphology) |
| `gender` | gendered noun's gender | omit if not applicable |
| `pronunciation` | IPA | only when it disambiguates; never guess |
| `collocations` | 2–4 natural partners | real collocations, not translations |
| `examples` | 1–2 original sentences + translations | natural; not a copy of the source sentence unless the source is the model |
| `commonErrors` | real, frequent learner mistakes | only if true for this word |
| `confusions` | words learners mix it up with | e.g. *borrow/lend*, *saber/conocer* |
| `sentenceRefs` | IDs of sentences where `surface` occurs | every occurrence gets a ref; at least one |
| `priority` | `high` / `medium` / `low` | at most one third `high` |
| `confidence` | `high` / `medium` / `low` | how sure you are of the analysis, not the learner's difficulty |
| `needsVerification` | boolean | true iff slang, regional, disputed, or damaged source |
| `tags` | optional short labels | e.g. `["false-friend"]`, `["cognate"]` |

## The surface contract

The `surface` field drives word highlighting in the rendered HTML. It **must** match the sentence text byte-for-byte (same glyphs, same case, same apostrophes/accents).

Rules:
- Copy the inflection exactly as it appears, including elision apostrophes (`l'`, `d'`, `s'`), accent marks, `ß`, `æ/ø/å`, `ç`, `ñ`, `¿/¡`.
- If an elision makes the surface `l'` + rest, use the full graphic word (`l'histoire`) and ensure that span appears literally in the sentence.
- For a multi-word surface, the whole span must appear contiguously in the sentence.
- Do not normalize case. If the sentence capitalizes the word at sentence start, the surface is capitalized.
- When the same lemma appears twice in different inflections, decide whether to record one item (preferred, surface = first occurrence, morphology covers the other) or two items (only if the senses differ).

## Morphology

Include morphology only where the learner cannot derive it. Otherwise leave it out — an empty block is better than a dictionary dump.

When you do include it, state the *features* that matter for production:
- **Verbs**: infinitive → this form (tense/aspect/mood/person/number); irregular stem; the auxiliary for compound tenses (Fr/It *avoir/essere*); separable vs. inseparable prefix (De/Nl).
- **Nouns/adjectives**: gender, number, case (De), the plural form if irregular, adjective position/agreement.
- **Pronouns**: case/role (subject, direct object, indirect object, reflexive, disjunctive).

Examples:
- `morphology: "3rd-person singular preterite of 'ir' (to go); irregular — shares form with 'ser'"`.
- `morphology: "separable verb 'aufstehen'; in this sentence the prefix 'auf' is in final position (verb bracket)"`.

## Priority and confidence

- **Priority** ranks teaching importance. Assign relative to the other items, not absolute. `high` = central to understanding this text or highly productive; `low` = worth a card but not a lesson.
- **Confidence** ranks your certainty in the *analysis* (sense, form, register). Mark `low` when the source is ambiguous or you lack context, and set `needsVerification: true`.
- Never invent a frequency band, CEFR level, or etymology to justify either.
