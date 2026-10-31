# English — Teaching Norm

Load when `textLanguage` is `en`. These rules override generic assumptions; they do not transfer to the other language files.

## 1. Orthography and Unicode

- Standard Latin script; apostrophes `'` (U+0027) and `’` (U+2019) both occur. Preserve whichever the source uses in quoted text; use `'` in generated examples.
- Quotation marks vary by variety and publisher: `“ ”`, `‘ ’`, `" "`. Preserve.
- Dashes: hyphen `-`, en dash `–` (ranges), em dash `—` (parenthetical). Preserve.
- Loanwords retain their diacritics when the source does: `café`, `naïve`, `résumé`, `fiancé`. Do not strip them.
- Do not "correct" deliberate misspellings in dialogue, social posts, or lyrics; flag them as non-standard instead.

## 2. Segmentation

Split at `.` `?` `!` and ellipsis `…`/`...` when it ends a sentence. Do not split after:

- titles and abbreviations: `Mr.`, `Mrs.`, `Ms.`, `Dr.`, `Prof.`, `St.`, `Jr.`, `Sr.`, `vs.`, `etc.`, `e.g.`, `i.e.`, `cf.`, `No.`;
- initials: `J. K. Rowling`;
- decimals and currencies: `3.5`, `$4.99`;
- domain names and file names.

Headlines and slogans may be fragments; keep them as one unit.

## 3. Parts of speech and morphology

Annotate POS **in context**. `run` is a verb in `they run`, a noun in `a long run`, and part of a phrasal verb in `run into`.

Morphology worth noting:

- irregular past/participle: `dug`, `brought`, `went`, `written`;
- irregular plurals: `children`, `criteria`, `phenomena`, `knives`;
- comparatives/superlatives: `better/best`, `further/furthermost`;
- third-person `-s`, `-ing` spelling changes (`stopping`, `making`);
- contractions: `won't` = `will not`, `ain't` (non-standard, register-marked), `y'all` (regional/informal);
- possessive vs. plural: `the neighbors' garden` vs. `the neighbor's garden`.

Do not gloss regular `-ed` or `-s` unless the learner is a beginner and the form is the teaching target.

## 4. Tense, aspect, modality

English marks aspect overtly; learners need the contrast, not the label.

- simple past vs. present perfect: `I lost my keys` (finished, time known) vs. `I've lost my keys` (current relevance);
- past perfect: `had become` — anterior to a past reference point, often with `by` + time;
- progressive: activity in progress, temporary state, or framing;
- futures: `will`, `going to`, present progressive, simple present — each with a different stance;
- modals of deduction: `must have left`, `might have forgotten`, `can't have known`;
- conditionals: `If I had known, I would have…`.

Explain the choice made in the sentence, not the whole system.

## 5. Phrasal verbs

High priority. Record:

- the verb + particle as one unit (`cobble together`, `put off`, `run into`);
- separability (`pick it up` / `pick up the book`, but `run into her`, not `run her into`);
- transitivity and the meaning shift (`turn up` = arrive; `turn down` = reject/refuse; `turn into` = become);
- register: many are neutral, some informal (`fork out`), some formal-ish (`carry out`).

A split phrasal verb's surface may not be contiguous (`kriegst … hin` is German, but English also splits: `pick the kids up`). Record the full unit in `text` and note the observed split.

## 6. Register and colloquial forms

- Contractions are standard in speech and most journalism; their absence signals formality.
- `gonna`, `wanna`, `gotta`, `kinda` are informal transcriptions — mark `informal`, not slang.
- Discourse markers (`well`, `you know`, `I mean`, `still`, `though` at sentence end) carry stance; gloss them functionally.
- British/American lexical differences: `flat/apartment`, `lorry/truck`, `holiday/vacation`, `queue/line`, `autumn/fall`.
- Spelling differences: `-ise/-ize`, `colour/color`, `centre/center`, `travelling/traveling`. Do not silently normalize; note the variety when it matters.

## 7. Collocations and valency

Record strong preferences, not free combinations:

- `make a decision` (not `do`), `take a risk`, `pay attention to`, `depend on`, `consist of`, `be interested in`;
- adjective + noun: `heavy rain`, `strong coffee`, `high hopes`;
- verb + noun: `commit a crime`, `run a business`;
- prepositional patterns: `accuse sb of`, `blame sb for`, `provide sb with`.

## 8. Common learner errors and false friends

- `actually` means "in fact", not "currently" / "at present";
- `eventually` = finally, not "possibly";
- `sensible` = reasonable, not "sensitive";
- `library` = a place that lends books (in several European languages the cognate means "bookshop"); `magazine` = a periodical (in some languages the cognate means "shop/store");
- dropped third-person `-s`; wrong irregular past (`*goed`);
- `since` + present perfect vs. `for` + duration;
- double negation and `any`/`some` in negatives;
- countable/uncountable (`informations`, `advices` are errors).

Note a false friend only when it actually appears or the learner is likely to produce it here.

## 9. Regional and social variation

Do not assign a dialect to a text without evidence. Evidence includes: spelling (`colour`), lexis (`lift`), syntax (`I've just seen him` vs. `I just saw him`), and the source's own statement. AAVE, Scottish, Irish, Australian, and Indian English features may appear in dialogue; label them as variety features with the basis, and mark `regionCertainty` honestly.

## 10. Teaching priorities for English texts

1. Phrasal verbs and prepositional patterns.
2. Tense/aspect choice where the sentence hinges on it.
3. Collocation that makes the difference between correct and natural.
4. Register: contractions, discourse markers, informal vocabulary.
5. Word formation (`un-`, `-ness`, `-ful`, `-less`) when productive in the text.

## 11. Annotation checklist

- [ ] Surface form found verbatim in the sentence.
- [ ] Phrasal verb recorded as one expression, split noted if applicable.
- [ ] Tense/aspect explanation states the contrast, not just the name.
- [ ] Register marked for contractions, slang, and informal lexis.
- [ ] BrE/AmE difference noted only with evidence.
- [ ] No CEFR or frequency claim.
