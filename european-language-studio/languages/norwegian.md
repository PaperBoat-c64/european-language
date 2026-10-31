# Norwegian — Teaching Norm

Load when `textLanguage` is `no`. Bokmål is the default written standard; Nynorsk is noted where it differs and is never silently mixed in. Norwegian marks gender, number, and definiteness with suffixes and has no person agreement on verbs.

## 1. Orthography and Unicode

- `æ`, `ø`, `å` are distinct letters (the alphabet ends `… x y z æ ø å`). Never replace with `ae`, `oe`, `aa`.
- Two written standards: **Bokmål** (default) and **Nynorsk**. They are written standards, not dialects; keep the source's standard and do not convert forms between them.
- `aa` for `å` appears in older texts and names (`Aasen`, `Smaabyen`); preserve in quoted text.
- Accents are rare and optional (`én` vs. `en`, `fór` vs. `for`); preserve the source's choice, do not add or strip.
- Minimal pairs to respect: `for` (for) / `fór` (went), `en` (a/an) / `én` (one).
- `c`, `q`, `w`, `x`, `z` occur mainly in loanwords and names; do not flag them.
- Quotation marks: `« »` or `" "`; preserve.
- Do not "correct" eye-dialect or dialect spellings in dialogue; flag them as non-standard/dialect instead.

## 2. Segmentation

Split at `.` `?` `!` and `…`. Do not split after:

- `f.eks.`, `dvs.`, `bl.a.`, `osv.`, `jf.`, `ca.`, `nr.`, `dr.`, `st.`, `kl.`;
- ordinals: `den 3. mai`, `2. etasje`;
- decimals and thousands: `3,14`, `1.000,50`; times `kl. 10.30`.

Headlines and slogans may be fragments; keep them as one unit. Norwegian sentences can be long with embedded clauses; prefer the larger unit when uncertain.

## 3. Nouns, gender, number, articles

- Bokmål has a two-gender system (common + neuter) with an optional feminine, or a three-gender system. Default model: masculine/feminine (common) vs. neuter. Feminine nouns may take masculine forms in Bokmål (`en bok` / `ei bok`, `boken` / `boka`). Nynorsk requires three genders. Record the gender actually shown; do not guess.
- Indefinite article: `en` (masc./common), `ei` (fem., optional in Bokmål), `et` (neuter).
- Definiteness is a **suffix**, not a separate article: masc. `-en` (`bilen`), fem. `-a` (`boka`), neut. `-et` (`huset`).
- Indefinite plural: `-er` (most masc./fem., `biler`), `-e` (nouns in `-er`, `lærer → lærere`); neuter often `-er` or zero (`eple → epler`, `hus → hus`).
- Definite plural: `-ene` (`bilene`, `husene`); Nynorsk has parallel forms.
- **Double definiteness**: when a definite noun has a preceding adjective, add the free definite article before the adjective: `den store bilen`, `det store huset`, `de store bilene`. The noun keeps its suffix — a key teaching point.
- Adjective agreement: indefinite singular neuter `-t` (`et stort hus`); `-e` for plural and all definite forms (`store hus`, `den store bilen`).
- Compounds are written as one word and take the gender of the final element (`fjelltur` = `fjell` + `tur`). Split transparent compounds in glosses.

## 4. Verbs

- No person/number agreement: `jeg er, du er, han er, vi er`.
- Infinitive marker `å` (`å lese`).
- Present tense: usually infinitive + `-r` (`leser, snakker`); a few strong monosyllables have special forms (`er, går, står, vet`).
- Preterite: weak `-et` (`snakket`), `-te` (`leste`), `-de` (`levde`); strong with vowel change (`gikk, skrev, tok`). Name the class when annotating.
- Preterite is the narrative past; perfect links past to present — state the contrast when the sentence hinges on it.
- Perfect: `har` + past participle (`har lest`); a closed set of motion/change verbs takes `er` + participle (`er kommet`, `er reist`).
- **s-passive**: add `-s` to the infinitive/present (`bøker selges her`, `det sies at`). Distinguish from reflexive/deponent `-s` verbs (`vi sees`, `å synes`). Name the type; do not gloss every `-s` as "is being …".
- Modals: `kan` (can/may), `må` (must), `skal` (shall/will, plan), `vil` (will/want), `bør` (ought to). `får` = gets / is allowed to; permission is `får`/`kan`, not `må`.
- Modals take the bare infinitive (`jeg kan lese`, not `å lese`).
- Futurity is often just present + time adverbial (`jeg kommer i morgen`); do not force an English future label.
- Imperative = bare stem (`les!`, `kom!`).

## 5. Word order (and pronouns where relevant)

- Main clause: finite verb second (V2). Inversion when a non-subject element opens the clause: `I går kjøpte jeg en bok`.
- Subordinate clause: sentence adverbs (`ikke, alltid, aldri, ofte, sjelden, kanskje, bare, jo, vel, da`) precede the finite verb — the **BIFF rule** (the mnemonic for this set). `Jeg vet ikke hvorfor han ikke kommer.` Contrast main-clause `Han kommer ikke.`
- Negation `ikke`: after the finite verb in main clauses, before it in subordinate clauses.
- Yes/no questions: verb first. Wh-questions: wh-word first, verb second.
- Personal pronouns: `jeg` (I), `du` (you sg.), `han` (he), `hun` (she), `den` (it, masc./fem.), `det` (it, neuter), `vi` (we), `dere` (you pl.), `de` (they), `dem` (them). `De` (capitalized) = formal you (rare).
- `den`/`det` also serve as the pre-adjectival definite article and as expletive subject (`det regner`).
- Reflexive pronoun `seg` for third persons (`han vasker seg`); `seg selv` = himself/herself/itself.
- Possessives: `min/mitt/mine`, `din/ditt/dine`, `sin/sitt/sine`. `sin` refers back to the subject (`han tok sin bok` = his own; `hans bok` = another man's).

## 6. Prepositions and valency

Record as valency, not idiom:

- `på` (on/at — surfaces and many places: `på skolen`, `på butikken`); `i` (in — enclosed places, towns, countries: `i Norge`, `i Oslo`); `av` (of/by); `til` (to); `for` (for); `om` (about/around/in + time: `om sommeren`); `med` (with); `gjennom` (through).
- `hos` = at someone's place / with a person (`hos oss` = at our place); do not confuse with `på`/`i`.
- Time: `i` + year/month/season (`i 2025`, `i januar`), `på` + day (`på mandag`), `om` + general period (`om morgenen`).
- Verb government: `vente på`, `tenke på`, `le etter`, `se på`, `høre på`, `snakke om`, `spørre om`, `komme fra`, `bo i/på`, `glede seg til`.
- Adjective government: `redd for`, `glad i` (fond of), `glad for` (happy about), `stolt av`, `interessert i`, `avhengig av`.

## 7. Register and colloquial forms

- `du` vs. `De`: `De` (capitalized) is formal, now rare and mostly institutional or older usage; default to `du`. Note `De` only when it appears.
- Informal tone is common in public writing; do not over-mark as slang.
- Spoken/colloquial reductions in dialogue: `'kke` (ikke), `'a`/`'an` (han/hun), `åssen` (hvordan), `skjønner` (understand). Mark `informal`, not error.
- Discourse markers: `jo` (after all / as you know), `vel` (surely), `da` (then — many functions), `nok` (probably), `altså` (that is / so). Gloss functionally; do not translate `jo` as English "yes" out of context.
- Swear and intensity words (`faen`, `jævla`, `sinnsykt`) — mark sensitivity; do not recommend productive use.

## 8. Regional variation

- Bokmål vs. Nynorsk are the two written standards; Nynorsk is most established in western Norway. A text is normally in one standard — identify it and stay consistent.
- Dialectal variation is large (pronunciation and lexicon). Written dialect in dialogue is intentional; label it as dialect with evidence, do not "correct" it.
- Label only with evidence: `eg` (I, Nynorsk/dialect) vs. `jeg`; `ikkje` (not, Nynorsk) vs. `ikke`; `golv` (floor, Nynorsk) vs. `gulv`.
- These examples are illustrations, not a region assignment; apply them only when the source supports them.
- Label region/standard only with evidence from the source or a cited dictionary; otherwise `regionCertainty: "unverified"`. Do not call Nynorsk a "dialect".

## 9. Common learner errors and false friends

- `rolig` = calm/quiet. Not Swedish `rolig` = funny; "funny" is `morsom`.
- `rar` = weird/odd. Not English "rare" (= `sjelden`); not Swedish `rar` = kind/nice.
- `artig` = fun/amusing. Danish `artig` = polite/well-behaved — do not transfer.
- `bra` = good. Not the English garment "bra" (= `BH`).
- `glass` = glass (material/drinking vessel: `et glass`); ice cream is `is`/`iskrem`. Swedish `glass` = ice cream — do not transfer.
- `by` = town/city; English "by" = `ved`/`hos`.
- `fart` = speed; English "fart" = `fjert`/`promp`.
- `full` = drunk; "full" (of food) = `mett`.
- `men` = but; English "men" = `menn`.
- `bare` = only/just; English "bare" = `naken`.
- `gift` = married (adjective) or poison (noun) — read from context.
- `middag` = dinner (main meal), not "midday".
- `aktuell` = current/relevant, not "actual" (`faktisk`).
- `eventuelt` = possibly, not "eventually" (`til slutt`).
- Learner errors: dropping V2 inversion; placing `ikke` after the verb in subordinate clauses; `sin` vs. `hans/hennes`; mixing `i`/`på` for places; omitting double definiteness (`*store bilen` instead of `den store bilen`); wrong `har`/`er` auxiliary.

## 10. Teaching priorities for Norwegian texts

1. Definiteness: suffix article and double definiteness.
2. V2 inversion and subordinate-clause adverb position (BIFF).
3. Gender of nouns and adjective agreement.
4. `har` vs. `er` perfect auxiliary and the s-passive.
5. Preposition choice (`i`/`på`, verb government).
6. False friends that block comprehension (rolig, rar, glass, fart).

## 11. Annotation checklist

- [ ] Gender, number, and definiteness noted for annotated nouns; double definiteness explained when an adjective precedes.
- [ ] Verb tense identified; strong/weak preterite class and auxiliary (`har`/`er`) stated.
- [ ] s-passive type named, not glossed as generic passive.
- [ ] Word order explained: V2 or subordinate-clause adverb position.
- [ ] `æ`/`ø`/`å` preserved; Bokmål/Nynorsk standard identified and kept consistent.
- [ ] `sin` vs. `hans/hennes` clarified if it appears.
- [ ] Regional/standard label only with evidence; otherwise unverified.
- [ ] No CEFR or frequency claim.
