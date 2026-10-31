# Italian — Teaching Norm

Load when `textLanguage` is `it`. Italian marks gender, number, person, tense, and mood through endings; word order is flexible around an SVO core; clitic pronouns, the subjunctive, and the passato prossimo/imperfetto contrast are central teaching points.

## 1. Orthography and Unicode

- Grave vs acute accents: most word-final stressed vowels take the grave (`città`, `virtù`, `però`, `caffè`); the acute marks a closed e/o in a few words (`perché`, `affinché`, `né`, `sé`). `è` (is) is grave; `e` (and) is accentless. Do not conflate `è`/`e`, `da`/`dà`, `la`/`là`, `si`/`sì`, `se`/`sé`, `ne`/`né`.
- A stressed final vowel is always written with an accent (`città`, `perché`, `così`, `lunedì`, `farò`). Final `i`/`u` accents are always grave (`così`, `giù`, `più`).
- Uppercase accented vowels keep the accent (`È`, `Perché`); do not replace with an apostrophe fallback.
- No `ñ`. Palatal /ɲ/ is `gn` (`gnocchi`, `bagno`); /ʎ/ is `gli` (`figlio`, `voglio`). Hard /k/ and /g/ before e/i are written `ch`/`gh` (`chiesa`, `ghiaccio`); `c`/`g` before e/i are soft (`cena`, `gelato`).
- Elision apostrophes: `l'` (lo/la before a vowel), `un'` (feminine `una` before a vowel: `un'amica`), `dell'`, `all'`, `nell'`, `sull'`, `dall'`, `quest'`, `un po'` (from `poco`). `un` before a masculine vowel takes no apostrophe (`un amico`).
- Preserve the source's apostrophe glyph (`'` or `’`). Do not strip accents in generated examples.

## 2. Segmentation

Split at `.` `?` `!` and `…`. Do not split after:

- `Sig.`, `Sig.ra`, `Dott.`, `Dott.ssa`, `Prof.`, `Prof.ssa`, `Avv.`, `Ing.`, `ecc.`, `p. es.`, `ca.`, `N.B.`, `n.`;
- decimals and thousands: `1,5`, `3.000,50`;
- initials.
- Roman numerals and century abbreviations (`XX secolo`, `il '900`) form one unit.

Italian sentences can be long with embedded clauses; prefer the larger unit when the boundary is uncertain.

## 3. Nouns, gender, number, articles

- Gender is lexical. `-o` is usually masculine, `-a` usually feminine, `-e` either (`il fiore`, `la notte`). Do not guess from meaning.
- Exceptions: Greek-derived `-ma`/`-ta` are masculine (`il problema`, `il tema`, `il sistema`, `il programma`); some `-o` are feminine (`la mano`, `la foto`, `la radio`); `-tà`/`-tù` abstract nouns are feminine (`la città`, `la virtù`); `-zione`/`-sione` feminine; `-ore` masculine; agent nouns in `-tore`/`-trice` (`il traduttore`, `la traduttrice`).
- Plurals: `-o → -i` (`libro → libri`), `-a → -e` (`casa → case`), `-e → -i` (`fiore → fiori`, `notte → notti`).
- Invariable nouns: those ending in an accented vowel (`città → città`), a consonant (`bar → bar`), or `-i` (`crisi → crisi`). Plural of `-tà` stays unchanged.
- Irregular plurals: `uomo → uomini`, `moglie → mogli`, `bue → buoi`, `dio → dei`; some masculine `-o` nouns take a feminine `-a` plural with collective meaning (`l'uovo → le uova`, `il dito → le dita`, `il braccio → le braccia`).
- Definite articles: `il` (masc + consonant), `lo` (masc + s+consonant, z, gn, ps, x: `lo studente`, `lo zio`), `l'` (masc/fem + vowel), `la` (fem); plural `i`, `gli` (of `lo`/`l'`), `le`.
- Indefinite: `un`, `uno` (same environments as `lo`: `uno studente`), `una`, `un'` (fem + vowel).
- Article choice is phonologically conditioned: `lo/gli` before `s`+consonant, `z`, `gn`, `ps`, `x` (`lo psicologo`, `gli zaini`); `l'` before any vowel (`l'amico`, `l'amica`).
- Preposizioni articolate — fused preposition + article. `a`: `al, allo, all', alla, ai, agli, alle`; `di`: `del, dello, dell', della, dei, degli, delle`; `da`: `dal, dallo, dall', dalla, dai, dagli, dalle`; `in`: `nel, nello, nell', nella, nei, negli, nelle`; `su`: `sul, sullo, sull', sulla, sui, sugli, sulle`. Expand them in glosses (`nel` → `in + il`). `con` may fuse (`col`, `coi`) but the separated form is standard today; `per`, `tra`, `fra` never fuse.

## 4. Verbs

- Three conjugations: `-are` (`parlare`), `-ere` (`vendere`, `leggere`, `prendere`), `-ire` (`dormire`; many `-ire` verbs insert `-isc-`: `finisco`, `capisco`, `preferisco`). Identify the conjugation and any stem change.
- Auxiliaries: `avere` for transitive verbs; `essere` for reflexive/pronominal verbs and intransitive verbs of motion, state, and change (`andare, venire, arrivare, partire, entrare, uscire, nascere, morire, restare, stare, essere, diventare`). Some verbs take either with a meaning shift (`ho cambiato` = I changed something vs. `sono cambiato` = I changed).
- Passato prossimo (`avere`/`essere` + participle) = completed past with present relevance. Imperfetto = background, habit, ongoing past, description. Explain the contrast, not just the label.
- Participle agreement: with `essere`, the participle agrees with the subject (`è andata`, `sono partiti`); with `avere`, it agrees with a preceding direct-object clitic (`l'ho vista`, `li ho visti`), otherwise it stays masculine singular.
- Congiuntivo (subjunctive): triggered by verbs of opinion, doubt, hope, emotion, and will (`penso che`, `credo che`, `spero che`, `voglio che`, `ho paura che`, `dubito che`), impersonal expressions (`è importante che`, `bisogna che`), and conjunctions (`benché`/`sebbene`, `affinché`/`perché` (purpose), `prima che`, `a meno che`, `senza che`). Identify the trigger; certainty takes the indicative (`so che è vero`).
- Reflexive and pronominal verbs take `essere` in compound tenses (`mi sono lavato`, `si è arrabbiata`).
- `piacere`-type verbs take an indirect object (`mi piace`, `gli piacciono`); the grammatical subject is the liked thing, not the person.
- `stare` + gerundio = progressive (`sto leggendo`); `stare per` + infinitive = about to (`sto per uscire`).
- Modals `potere`, `dovere`, `volere` + infinitive; in compound tenses they may take the auxiliary of the dependent infinitive (`sono dovuto andare` alongside `ho dovuto andare`).
- Future (`parlerò`) and conditional (`parlerei`) are synthetic; the passato remoto (`parlai`) is a narrative/literary tense (regional in speech).
- Irregular participles: `aperto`, `detto`, `fatto`, `scritto`, `visto`, `preso`, `messo`, `letto`, `rotto`, `morto`, `nato`, `venuto`.
- Imperative: affirmative attaches pronouns (`dammelo`, `dimmelo`); the negative `tu` form uses the infinitive (`non dirmelo`), other persons use the subjunctive.
- `ci` and `ne` are part of many fixed verb constructions (`esserci`, `avercela`, `volerci`, `andarsene`, `farcela`) — record them as expressions, not as the pronoun alone.

## 5. Pronouns and clitics

- Direct-object clitics: `mi, ti, lo, la, ci, vi, li, le`. Indirect: `mi, ti, gli, le, ci, vi, gli` (plural `loro` in formal writing). Formal `Le` (to you) is capitalized.
- `lo/la` also translate "it/him/her"; `le` is both "to her" and "them (fem. direct object)". Disambiguate by function.
- Combined clitics: indirect before direct. `mi/ti/ci/vi` + `lo/la/li/le/ne` become `me lo, te lo, ce lo, ve lo` (`me lo dai`); `gli/le` + direct/`ne` fuse into `glielo, gliela, glieli, gliele, gliene` (`glielo do`). Show the expansion.
- `ne` = partitive ("of it/them", "some": `ne voglio due`) or replaces `di + phrase` (`ne parlo`). `ci` = "there" (`ci vado`) or replaces `a + phrase` (`ci penso`). `c'è`/`ci sono` = there is/are.
- Placement: before the finite verb (`lo vedo`, `me lo dai`); attached to infinitive, gerund, and affirmative imperative, dropping the infinitive's final `-e` (`vederlo`, `vedendolo`, `dammelo`). With compound tenses the clitic precedes the auxiliary (`l'ho visto`, `gliel'ho detto`).
- Stressed/disjunctive pronouns follow prepositions: `per me`, `con te`, `penso a lui/lei`, `da solo`. Full set: `me, te, lui/lei/sé, noi, voi, loro`; also used for emphasis (`Voglio te`). Never use subject pronouns as objects.
- Impersonal/passive `si`: `si parla italiano`, `si vende`, `si dice`; with a plural direct object the verb agrees (`si vendono case`).
- `si` is ambiguous: reflexive (`si lava`), reciprocal (`si incontrano`), impersonal (`si dice`), passive (`si vende`). Name the type from context; do not label every `si` as reflexive.
- Subject pronouns are usually omitted; keep them only for contrast, emphasis, or disambiguation.

## 6. Prepositions and valency

- `a` (to/at/in), `di` (of/from), `da` (from/by/since/at someone's place), `in` (in), `con` (with), `su` (on/about), `per` (for/through), `tra`/`fra` (between/among/in X time). Explain the relation in the sentence, not a single English gloss.
- `a` before cities (`a Roma`), `in` before countries/regions (`in Italia`). `da` + infinitive = something to do (`c'è molto da fare`).
- `da` + present = "for/since" with duration continuing now (`vivo qui da due anni` = I have lived here for two years) — English present perfect, Italian present.
- Fixed valency to record: `pensare a`, `parlare di/con`, `interessarsi di`, `occuparsi di`, `dipendere da`, `credere in`, `innamorarsi di`, `contare su`, `andare a`, `venire da`, `sognare di`, `rinunciare a`, `abituarsi a`.
- Double-object verbs: `dare qc a qn`, `mandare qc a qn`; the recipient is indirect (`le do il libro`).

## 7. Register and colloquial forms

- Address: `tu` (informal singular), `Lei` (formal, third-person singular, capitalized), `voi` (plural; also an older/historical formal singular, still heard in some southern varieties), `loro` (very old formal, rare).
- In writing, formal `Lei`/`Voi` may be capitalized; preserve the source's capitalization and gloss the social force.
- Spoken reductions: `'sta` (`questa`), `'sto` (`questo`), dropped final vowels in some dialects; mark `informal`/`colloquial`, not standard.
- Discourse markers: `allora` (well/then), `cioè` (I mean), `insomma` (in short), `dai` (come on), `magari` (maybe/if only), `ecco` (here/there), `beh` (well), `boh` (I don't know, informal) — gloss functionally.
- Slang is regional and fast-moving; label region and mark `needsVerification` unless well established.
- Do not treat dialect-influenced Italian as an error; mark it as regional/colloquial.

## 8. Regional variation

- Standard Italian is Tuscan-based; regional Italian carries local lexicon, syntax, and phonology. Label a form "regional" only with evidence from the source or a cited dictionary.
- Lexical variation is common across regions: `anguria`/`cocomero` (watermelon), `babbo`/`papà` (dad), `marinare`/`bigiare` (to skip school), `stampella`/`gruccia` (hanger). Do not assign these without evidence.
- Southern varieties may retain `voi` as a formal singular; central/southern usage keeps the passato remoto for recent past, while northern usage leans on the passato prossimo. Neither is "wrong"; note the region.
- When the region is not identifiable, use `regionCertainty: "unverified"`. Never call a regional form "wrong Italian".

## 9. Common learner errors and false friends

- `attualmente` = currently, not "actually" (`in realtà`).
- `libreria` = bookshop; "library" = `biblioteca`.
- `sensibile` = sensitive; "sensible" = `ragionevole`.
- `parenti` = relatives; "parents" = `genitori`.
- `camera` = room; "camera" = `macchina fotografica`.
- `fabbrica` = factory; "fabric" = `tessuto`/`stoffa`.
- `pretendere` = to demand/claim; "pretend" = `fingere`.
- `morbido` = soft; "morbid" = `morboso`.
- `eventualmente` = possibly, not "eventually" (`alla fine`); `simpatico` = likeable, not "sympathetic" (`comprensivo`); `rumore` = noise, not "rumor" (`voce`); `bravo` = good/skillful, not "brave" (`coraggioso`); `educato` = polite, not "educated" (`istruito`); `firma` = signature, not "firm" (`azienda`/`ditta`); `argomento` = topic, not "argument" (`litigio`).
- Gender/number agreement errors; wrong auxiliary in compound tenses; missing or misplaced subjunctive; clitic order and `me lo`/`glielo` combinations; confusing `ne` and `ci`; expanding `nel`/`della` incorrectly; English double negatives (Italian uses `non … mai/niente/nessuno`); omitting the accent or using the wrong grave/acute.

## 10. Teaching priorities for Italian texts

1. Passato prossimo vs imperfetto and the discourse role of the choice.
2. Subjunctive triggers and their contrast with the indicative.
3. Clitic order, combination, and placement; `ne`/`ci`.
4. Participle agreement with `essere` and with preceding objects.
5. Preposizioni articolate and verb valency.
6. Address forms (`tu`/`Lei`) and register.

## 11. Annotation checklist

- [ ] Gender and number given for annotated nouns; irregular plural noted.
- [ ] Verb conjugation, auxiliary, and participle-agreement trigger stated.
- [ ] Subjunctive trigger identified, or indicative justified.
- [ ] Clitic expansion shown (`glielo` → `gli + lo`); `ne`/`ci` function named.
- [ ] Preposizione articolata expanded (`nel` → `in + il`).
- [ ] Grave/acute accent and elision apostrophe preserved from source.
- [ ] Address form (`tu`/`Lei`/`voi`) noted when the text turns on it.
- [ ] Regional label only with evidence; otherwise unverified.
- [ ] No CEFR or frequency claim.
