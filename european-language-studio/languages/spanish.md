# Spanish — Teaching Norm

Load when `textLanguage` is `es`. Spanish marks gender, number, person, tense, mood, and clitic pronouns richly; regional variation is substantial and must not be smoothed away.

## 1. Orthography and Unicode

- `ñ` is a distinct letter (`año` ≠ `ano`). Never replace with `n`.
- Accents mark stress and distinguish homophones: `sí` (yes) / `si` (if), `él` / `el`, `tú` / `tu`, `más` / `mas`, `qué` / `que`, `cómo` / `como`, `dónde` / `donde`.
- `¿` and `¡` open questions and exclamations. Their absence in quoted source is a source feature (or an error) — preserve it, do not silently add or remove.
- `ü` marks a pronounced `u` after `g`: `pingüino`, `vergüenza`.
- Quotation marks: `«»` (peninsular preference), `“ ”` (American), or `" "`. Preserve.
- Apostrophes are not standard in Spanish; they appear in dialect writing or loanwords. Preserve if present.
- Do not strip accents in generated text.

## 2. Segmentation

Split at `.` `?` `!` and `…`. Do not split after:

- `Sr.`, `Sra.`, `Srta.`, `Dr.`, `Dra.`, `Prof.`, `Ud.`, `Uds.`, `etc.`, `p. ej.`, `EE. UU.`, `n.º`, `D.`;
- decimals and thousands: `3,14`, `1.000,50`;
- initials.

Note: Spanish sentences can be long with embedded clauses; prefer the larger unit when the boundary is uncertain.

## 3. Nouns, adjectives, articles

- Gender: masculine/feminine, usually visible in the article; exceptions and ambiguity exist (`el agua` is feminine but takes `el` for stress reasons; `la mano` is feminine).
- Number: `-s` after vowel, `-es` after consonant; irregular stress shift (`joven → jóvenes`), invariant forms (`el lunes`, `la crisis`).
- Adjectives agree in gender and number: `tazas torcidas`, `un jarrón torcido`.
- Articles: `el/la/los/las`, `un/una/unos/unas`; neuter `lo` for abstract/adjectival nouns (`lo importante`).
- `lo` + adjective = "the … thing/aspect": `lo importante era volver` = "the important thing was to come back". This is not a masculine article.
- Contractions: `a + el = al`, `de + el = del` (not with proper nouns: `de El Escorial`).

## 4. Verbs

- Person/number endings are obligatory; subject pronouns are usually omitted.
- Tenses: present, preterite (`hablé`), imperfect (`hablaba`), future, conditional, perfect (`he hablado`), pluperfect (`había hablado`), progressive (`estoy hablando`).
- Preterite vs. imperfect: completed event vs. background/habit/description. The choice often carries discourse structure.
- Subjunctive: triggered by doubt, emotion, evaluation, commands, and conjunctions (`que`, `antes de que`, `para que`, `a menos que`, `cuando` + future). Present and imperfect subjunctive both occur; identify the trigger.
- `se` types — distinguish carefully:
  - reflexive: `se lava`;
  - reciprocal: `se escriben`;
  - passive/impersonal: `se vende`, `se dice`;
  - accidental: `se me cayó` ("it fell on me") — indirect object marks the affected person;
  - lexical/pronominal: `irse`, `quedarse`, `apuntarse`.
- Clitics: order indirect → direct (`me lo dio`), and attached to infinitives/gerunds/positive imperatives (`dímelo`, `dárselo`).
- `gustar`-type verbs take an indirect object: `me gusta`, `le interesan`, `nos falta`.
- `deber` + inf = obligation; `deber de` + inf = probability. Do not collapse them.
- `ir a` + inf = future intention; `acabar de` + inf = recent past.

## 5. ser / estar / haber / tener

- `ser`: identity, origin, profession, inherent characteristics, time.
- `estar`: location, temporary state, result of change, progressive.
- Some adjectives change meaning: `ser listo` (clever) / `estar listo` (ready); `ser aburrido` (boring) / `estar aburrido` (bored).
- `hay` vs. `estar`: existence/indefinite (`hay un banco`) vs. location/definite (`el banco está allí`).
- `tener` for possession and age (`tengo treinta años`), not `ser`.

## 6. por / para and other contrasts

- `por`: cause, exchange, duration, movement through, agent.
- `para`: purpose, destination, recipient, deadline, opinion.
- Do not reduce them to one English preposition; explain the relation in the sentence.
- `para colmo`, `por si acaso`, `por poco` are fixed units — classify as expressions, not preposition choices.

## 7. Register and colloquial features

- `tú` (informal singular), `usted` (formal), `vosotros` (informal plural, Spain), `ustedes` (plural, Spain formal / Latin America general).
- Spoken reductions: `pa'` (`para`), `na'` (`nada`), dropped intervocalic `d` in participles (`cansao`, `hablao`) — mark as colloquial/dialect, not standard.
- Discourse markers: `pues`, `bueno`, `o sea`, `es que`, `mira`, `venga` — gloss functionally.
- Slang is highly regional and fast-moving. Label region and mark `needsVerification` unless the item is well established.

## 8. Regional variation

- Spain vs. Latin America: `vosotros`/`ustedes`; `coger` (Spain: take) is vulgar in parts of Latin America; `ordenador`/`computadora`; `coche`/`carro`/`auto`; `piso`/`departamento`/`apartamento`.
- Rioplatense: `vos` + distinct endings (`vos tenés`, `vos podés`), `che`, `boludo` (register-sensitive).
- Mexico/Central America: `ustedes` plural, `¿mande?`, `ahorita`.
- Caribbean: `s`-aspiration, `tú`/`usted` social nuances.
- Do not label a word "Latin American" when it is specific to one country. When unsure, say `region: []`, `regionCertainty: "unverified"`.

## 9. Common learner errors and false friends

- `embarazada` = pregnant, not "embarrassed" (`avergonzada`).
- `largo` = long; `large` in English ≠ `largo`.
- `actualmente` = currently, not "actually".
- `realizar` = to carry out, not always "to realize" (`darse cuenta`).
- `asistir a` = to attend, not "to assist".
- `pretender` = to intend/claim, not "to pretend" (`fingir`).
- `ser`/`estar` and `por`/`para` misuse; wrong subjunctive trigger; missing personal `a` (`Veo a María`); `que` vs. `de que` (`me di cuenta de que`).
- Confusing preterite and imperfect in narrative.

## 10. Teaching priorities for Spanish texts

1. Preterite/imperfect and the discourse function of the choice.
2. `se` type identification (especially accidental `se`).
3. Clitic order and attachment.
4. `ser/estar`, `por/para`, `deber/deber de`.
5. Regional and register marking for colloquial items.

## 11. Annotation checklist

- [ ] Gender/number of annotated nouns and adjectives.
- [ ] Verb tense/mood/person; irregular stem or ending noted.
- [ ] Clitic expansion shown (`dímelo` → `di + me + lo`).
- [ ] `se` type named, not just "reflexive".
- [ ] `¿` `¡` preserved in quoted text.
- [ ] Regional label specific or marked unverified.
- [ ] No CEFR or frequency claim.
