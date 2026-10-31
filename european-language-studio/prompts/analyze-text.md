# Prompt — Analyze Text

Used in Step 1. Produces a short teaching plan, not a lesson.

## When to use

Before segmenting or translating. Also on request ("what's worth learning in this text?").

## Required inputs

- `{{TEXT}}` — full source, verbatim
- `{{EXPLANATION_LANGUAGE}}` — default English
- `{{LEARNER_LEVEL}}` — optional; default `unknown`
- `{{USER_GOAL}}` — optional ("read the news", "understand a short story", "exam prep")

## Prompt

```text
You are a language teacher analyzing an authentic text before building a study packet.

Text:
"""
{{TEXT}}
"""

Explanation language: {{EXPLANATION_LANGUAGE}}
Learner level: {{LEARNER_LEVEL}} (if "unknown", assume a B1 reader)
Learner goal: {{USER_GOAL}}

Do all of the following, briefly:

1. Identify the language (en/fr/es/de/it/pt/nl/sv/no/da), genre, register, and likely audience. State the evidence for each in a few words (e.g. "Belgian Dutch lexicon: gij").
2. Identify the text's structure: paragraphs, dialogue turns, headings. Note anything that complicates sentence segmentation (abbreviations, ellipses, embedded quotes, headlines).
3. List 3–6 teaching targets that are actually instantiated in the text. For each, give the sentence ID pattern or a short quoted fragment. Prefer items that affect comprehension or are productive for the learner.
4. Note observable difficulty signals (syntactic depth, idiomaticity, lexical opacity, register distance, orthographic load). Do NOT assign a CEFR level to the text or to any word.
5. Flag any source problems: OCR noise, typos, mixed languages, missing text, unclear referents.
6. State what you will NOT annotate, and why (e.g. "proper nouns except the institution name").
7. Confirm the output mode is `study` (the default; the packet always renders to HTML + DOCX).

Rules:
- Do not translate yet.
- Do not invent facts about the author, publication, or culture.
- If the language is mixed, choose the primary and say why.
- Keep the whole answer under 400 words.

Output:
## Text profile
- Language / genre / register:
- Structure:
- Segmentation risks:

## Teaching targets
1. … (refs)
2. …

## Difficulty signals
…

## Source issues
…

## Scope decisions
…

## Mode
study
```

## Output contract

Return the six headings above. No translation, no vocabulary records, no exercises.

## Self-check

- [ ] Every teaching target quotes or points to actual text.
- [ ] No CEFR or frequency claim.
- [ ] Segmentation risks named specifically (which abbreviation, which ellipsis).
- [ ] Mixed-language decision justified if applicable.
- [ ] Under 400 words.
