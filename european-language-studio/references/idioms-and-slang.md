# Idioms and Slang — Taxonomy and Tests

How to decide whether a phrase is an expression worth annotating, and what to record about it.

## Table of contents
1. [Taxonomy](#taxonomy)
2. [Decision procedure](#decision-procedure)
3. [Inclusion and exclusion](#inclusion-and-exclusion)
4. [Register and sensitivity](#register-and-sensitivity)
5. [Region](#region)

## Taxonomy

Use exactly these types:

| type | definition | example |
|---|---|---|
| `collocation` | a conventional word pairing that is not freely substitutable | *make a decision* (not "do a decision") |
| `phrasal-verb` | verb + particle(s) with a meaning not predictable from the parts | *give up*, *look after* |
| `idiom` | a frozen expression whose meaning is non-compositional | *to kick the bucket* |
| `colloquialism` | informal spoken register, regionally broad | *gonna*, *c'est pas mal* |
| `slang` | in-group, strongly informal, often regional or generation-specific | *bloke*, *fric* |
| `valency` | a pattern where the verb/adjective selects a specific preposition or case | *depend on*, *sich auf etw. freuen* |
| `grammatical-expression` | a construction whose grammar carries the meaning | *avoir à*, *es gibt*, *there's no -ing* |

A single phrase may fit more than one; pick the most specific that applies.

## Decision procedure

For each candidate, run these tests and record which it passes:

1. **Non-compositionality test** — can the learner derive the meaning from the parts? If not, it's an idiom (or phrasal verb).
2. **Substitution test** — if you replace one word with a near-synonym, does it sound foreign or wrong? If so, it's a collocation.
3. **Register/social test** — would using it in the wrong context cause a social error? If so, record register and sensitivity.
4. **Valency test** — does production require knowing this specific preposition/case/particle? If so, it's a valency item.
5. **Regional test** — is the phrase tied to a region or community? If so, record region + certainty.

## Inclusion and exclusion

**Include** only if at least one test genuinely passes. **Exclude**:

- ordinary syntax (transparent word order, regular agreement);
- transparent compounds whose meaning is the sum of parts;
- one-off poetic or rhetorical images (a writer's invention, not a fixed expression);
- items already covered as vocabulary records (do not duplicate);
- items added only to reach a count.

If nothing qualifies, say exactly:

> No high-value fixed expressions or slang found in this text worth separate treatment.

and give one sentence explaining why. **Do not fabricate items to fill the section.**

## Register and sensitivity

- `register`: `formal | neutral | informal | colloquial | vulgar | literary | archaic | mixed`.
- `sensitivity`: `none | mild | offensive | slur`. Set this for vulgar/offensive items, and add a `usageNotes` line on who may use it and where it is not acceptable.
- Never soften a slur's meaning, but do not teach its use. Mark `sensitivity: slur` and explain what it means only so the learner can recognize it.

## Region

- `region` is `[]` unless there is evidence. `regionCertainty` is `verified | probable | unverified`.
- Regional variants are real (European vs. Brazilian Portuguese; European vs. Quebec French; Iberian vs. Latin-American Spanish; Dutch vs. Belgian/Flemish; Bokmål vs. Nynorsk preference). Record the variant actually in the text.
- Never claim an expression is "used everywhere", "very common", or "universal" without evidence.
