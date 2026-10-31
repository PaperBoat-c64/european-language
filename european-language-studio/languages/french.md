# French — Teaching Norm

Load when `textLanguage` is `fr`. French is an inflected language with grammatical gender, verb agreement, and a large gap between written and spoken forms. Do not apply English tense labels mechanically.

## 1. Orthography and Unicode

- Accents are lexical and grammatical, not decoration: `é`/`è`/`ê`, `à`, `ù`, `ç`, `ô`, `î`, `ï`, `ë`, `œ` (`cœur`, `sœur`), `æ` (rare).
- Minimal pairs matter: `ou` (or) / `où` (where); `a` (has) / `à` (to); `la` / `là`; `sur` / `sûr`; `du` / `dû`.
- Apostrophes: elision uses `'` or `’`. **Preserve the source's glyph** in quoted text. Common elisions: `l'`, `d'`, `j'`, `qu'`, `n'`, `c'`, `s'`, `m'`, `t'`.
- French typography places a space before `; : ! ?` and inside `« »`. Preserve the source's spacing; do not silently convert to English conventions.
- Hyphens are grammatical in inversions and compounds: `a-t-il`, `est-ce`, `c'est-à-dire`, `peut-être` (adverb) vs. `peut être` (can be).
- Do not strip accents when writing generated examples.

## 2. Segmentation

Split at `.` `?` `!` and `…`. Do not split after:

- `M.`, `Mme`, `Mlle`, `Dr`, `Pr`, `St`, `Ste`, `etc.`, `cf.`, `p. ex.`, `c.-à-d.`, `av. J.-C.`;
- numbers: `1,5`, `3 000`, `10 h 30`;
- initials.

Dialogue may use `—` (tiret) or `« »`; keep speaker turns intact and do not merge them.

## 3. Nouns, gender, number, articles

- Every noun has gender; record it for annotated nouns (`le`/`la`, often visible in the article).
- Plural usually `-s`, but: `-al → -aux` (`journal → journaux`), `-eau → -eaux`, `-ou → -ous` except `bijoux, cailloux, choux, genoux, hiboux, joujoux, poux`; irregular `œil → yeux`.
- Articles: definite `le/la/les`, indefinite `un/une/des`, partitive `du/de la/de l'/des`. The partitive is a teaching point (`du pain`, `de l'eau`) and has no English equivalent.
- Contractions: `à + le = au`, `à + les = aux`, `de + le = du`, `de + les = des`.
- `des` → `de` before an adjective preceding a plural noun (`de grands jardins`), with exceptions — note only if it appears.
- Gender is not inferable from meaning; do not guess. If the article is absent and gender is unknown, mark `needsVerification`.

## 4. Verbs

- Three groups: `-er` (regular, productive), `-ir` (many regular with `-iss-`), and irregular (`-re`, `-oir`, etc.).
- Auxiliaries: `avoir` for most verbs; `être` for pronominal verbs and a closed set of motion/change verbs (`aller, venir, arriver, partir, entrer, sortir, monter, descendre, naître, mourir, rester, tomber, retourner`, plus derivatives).
- Past participle agreement:
  - with `être`: agree with subject (`elle est partie`);
  - with `avoir`: agree with a **preceding direct object** only (`les fleurs que j'ai cueillies`);
  - pronominal verbs: agree with subject when the reflexive pronoun is the direct object (`elle s'est lavée`), not when it is indirect (`elle s'est lavé les mains`).
- Tenses: `passé composé` (completed event), `imparfait` (background, habit, description), `plus-que-parfait` (anterior past), `passé simple` (literary), `futur simple`/`futur antérieur`, `conditionnel`, `subjonctif` after triggers (`il faut que`, `bien que`, `avant que`, `pour que`, doubt/emotion).
- `depuis` + present for an action continuing now (`je discute depuis…`), where English uses present perfect.
- `venir de + inf` = recent past; `être en train de + inf` = progressive.
- Imperative with object pronouns: affirmative orders them after with hyphens (`donne-le-moi`), negative before (`ne me le donne pas`).

## 5. Pronouns and clitics

- Order: `me/te/se/nous/vous` → `le/la/les` → `lui/leur` → `y` → `en`. `Il me le donne`, `Je lui en parle`, `Il y en a`.
- `on` = informal "we", generic "one", or "people"; verb is third-person singular. Translate by function ("we", "people", "you"), never as the English preposition "on".
- `y` replaces `à + place/thing`; `en` replaces `de + noun` or a partitive quantity (`j'en ai deux`).
- Disjunctive pronouns after prepositions: `chez moi`, `avec elle`, `penser à lui`.
- `le`/`la`/`les` as direct objects vs. `lui`/`leur` as indirect — a frequent learner error.
- Possessives agree with the possessed noun, not the possessor: `sa mère` can be "his" or "her" mother.

## 6. Elision, liaison, and spoken features

- Elision is obligatory before vowel/silent `h` for `le, la, je, me, te, se, ne, de, que, ce` (`l'ami`, `j'ai`, `qu'il`).
- Liaison is obligatory in some contexts (`les_amis`, `vous_avez`), optional in others, and forbidden after `et`. Do not mark liaison unless it is a teaching point; if you do, describe the context.
- Spoken French drops `ne` (`je sais pas`), uses `on` for `nous`, and reduces `il y a` to `y a`. Mark `informal`/`colloquial`; do not treat as errors.
- `tu`/`vous`: `tu` for peers/family/informal; `vous` for strangers, hierarchy, plural. The choice is social, not grammatical. Note it when the text turns on it.

## 7. Prepositions and valency

Fixed patterns to record as `valency`, not idiom:

- `penser à`, `s'occuper de`, `dépendre de`, `avoir besoin de`, `jouer à` (sport/game) / `jouer de` (instrument), `commencer à`, `essayer de`, `réussir à`, `être en train de`, `à cause de` / `grâce à`.
- Countries: `en France`, `au Québec`, `aux États-Unis`, `à Paris`.
- No preposition before a bare date (`le 3 mai`).

## 8. Register and regional variation

- Formal written: `nous`, full `ne`, `l'on`, literary `passé simple`.
- Neutral: standard written/spoken.
- Informal/colloquial: `ne`-drop, `on` for `nous`, `ouais`, `ça`, verlan (`meuf`, `keuf` — mark `slang`, region France, currency limited).
- Regions differ in lexicon and pronunciation: Québec (`char` = car, `magasiner` = to shop, `c'est correct` = fine), Belgium (`septante`, `nonante`), Switzerland (`septante`, `huitante`, `nonante`), Africa (varied institutional vocabulary). Label only with evidence; when unsure, `regionCertainty: "unverified"`.
- Do not call Québec usage "wrong French". Do not generalize Parisian slang to all French.

## 9. Common learner errors and false friends

- `actuellement` = currently, not "actually"; `éventuellement` = possibly, not "eventually".
- French `sensible` = sensitive; English "sensible" is French `raisonnable`.
- `librairie` = bookshop; `bibliothèque` = library.
- `demander` = to ask (not "to demand" = `exiger`).
- `visiter` a place vs. `rendre visite à` a person.
- `il y a` ≠ "there is" in all uses (also "ago": `il y a deux ans`).
- Omitting `de`/`à`, wrong auxiliary, missing participle agreement.
- Translating `on` as "we" when it is generic.
- Forgetting the partitive or using `des` where `de` is required.

## 10. Teaching priorities for French texts

1. Tense contrast (`passé composé` / `imparfait`) where the sentence depends on it.
2. Pronominal verbs and participle agreement.
3. Pronoun order and `y`/`en`.
4. Prepositional valency.
5. Register: `tu`/`vous`, `ne`-drop, `on`.

## 11. Annotation checklist

- [ ] Gender given for annotated nouns.
- [ ] Verb tense/mood/person identified; auxiliary and agreement trigger stated.
- [ ] Elision/contraction explained when it obscures the lemma (`du` → `de + le`).
- [ ] Register marked; `ne`-drop not treated as an error.
- [ ] Regional label only with evidence; otherwise unverified.
- [ ] Apostrophe glyph preserved from source.
- [ ] No CEFR or frequency claim.
