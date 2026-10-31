#!/usr/bin/env python3
"""
Validate a European Language Studio learning document.

Checks:
  1. Schema conformance (jsonschema when installed; structural checks otherwise)
  2. ID uniqueness and format per collection
  3. Cross-reference resolution (sentence <-> vocab/expression/grammar/exercise)
  4. Source integrity (sentence concatenation vs. source text, whitespace-insensitive)
  5. Surface integrity (each vocabulary/expression surface occurs in its sentence)

Usage:
    python3 validate_document.py path/to/document.json [--source path/to/source.txt]
    python3 validate_document.py path/to/document.json --strict

Exit code 0 on pass (warnings allowed), 1 on any failing hard check, 2 on invalid input.
"""

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA_PATH = HERE.parent / "schemas" / "learning-document.schema.json"

SENTENCE_RE = re.compile(r"^s\d{2,4}-\d{2,4}$")
VOCAB_RE = re.compile(r"^v\d{3,4}$")
EXPR_RE = re.compile(r"^e\d{3,4}$")
GRAMMAR_RE = re.compile(r"^g\d{3,4}$")
EXERCISE_RE = re.compile(r"^x\d{3,4}$")


def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def ws_normalize(text: str) -> str:
    """Remove all whitespace for a formatting-insensitive integrity comparison."""
    return re.sub(r"\s+", "", text or "")


def validate_schema(doc: dict) -> list:
    """Return a list of schema problems; empty means pass."""
    problems = []
    try:
        import jsonschema  # noqa: F401
    except ImportError:
        return ["jsonschema not installed — structural checks only"]

    try:
        import jsonschema
        schema = load_json(SCHEMA_PATH)
        validator = jsonschema.Draft202012Validator(schema)
        for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.path)):
            problems.append(f"{'.'.join(str(p) for p in err.path) or '$'}: {err.message}")
    except Exception as e:  # noqa: BLE001
        problems.append(f"schema validation error: {e}")
    return problems


def main():
    parser = argparse.ArgumentParser(description="Validate a European Language Studio document")
    parser.add_argument("document", help="Path to the learning-document JSON")
    parser.add_argument("--source", help="Optional separate source.txt for integrity comparison")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    doc_path = Path(args.document)
    if not doc_path.exists():
        print(f"ERROR: document not found: {doc_path}", file=sys.stderr)
        sys.exit(2)

    try:
        doc = load_json(doc_path)
    except json.JSONDecodeError as e:
        print(f"ERROR: invalid JSON: {e}", file=sys.stderr)
        sys.exit(2)

    errors = []
    warnings = []

    def err(msg):
        errors.append(msg)

    def warn(msg):
        warnings.append(msg)

    # 1. Schema
    schema_problems = validate_schema(doc)
    if schema_problems:
        # Distinguish "not installed" from real problems
        if schema_problems and "not installed" in schema_problems[0]:
            warn(schema_problems[0])
        else:
            for p in schema_problems:
                err(f"schema: {p}")

    # Structural: required top-level collections
    for key in ("meta", "source", "sentences", "vocabulary", "expressions", "grammar", "exercises", "qa"):
        if key not in doc:
            err(f"missing top-level key: {key}")

    meta = doc.get("meta") or {}
    source = doc.get("source") or {}
    sentences = doc.get("sentences") or []
    vocabulary = doc.get("vocabulary") or []
    expressions = doc.get("expressions") or []
    grammar = doc.get("grammar") or []
    exercises = doc.get("exercises") or []

    # 2. ID uniqueness and format
    def check_ids(items, regex, label):
        ids = [it.get("id") for it in items]
        if any(i is None for i in ids):
            err(f"{label}: an item is missing 'id'")
        seen = set()
        for i in ids:
            if not isinstance(i, str) or not regex.match(i):
                err(f"{label}: bad id format: {i!r}")
            if i in seen:
                err(f"{label}: duplicate id: {i}")
            seen.add(i)
        return {i for i in ids if isinstance(i, str)}

    sent_ids = check_ids(sentences, SENTENCE_RE, "sentences")
    vocab_ids = check_ids(vocabulary, VOCAB_RE, "vocabulary")
    expr_ids = check_ids(expressions, EXPR_RE, "expressions")
    gram_ids = check_ids(grammar, GRAMMAR_RE, "grammar")
    exer_ids = check_ids(exercises, EXERCISE_RE, "exercises")

    if not sentences:
        err("sentences: must contain at least one sentence")

    # 3. Cross-reference resolution
    for s in sentences:
        for ref in s.get("vocabularyRefs") or []:
            if ref not in vocab_ids:
                err(f"{s.get('id')}: vocabularyRefs -> unknown {ref}")
        for ref in s.get("expressionRefs") or []:
            if ref not in expr_ids:
                err(f"{s.get('id')}: expressionRefs -> unknown {ref}")
        for ref in s.get("grammarRefs") or []:
            if ref not in gram_ids:
                err(f"{s.get('id')}: grammarRefs -> unknown {ref}")

    for v in vocabulary:
        for ref in v.get("sentenceRefs") or []:
            if ref not in sent_ids:
                err(f"{v.get('id')}: sentenceRefs -> unknown {ref}")

    for e in expressions:
        for ref in e.get("sentenceRefs") or []:
            if ref not in sent_ids:
                err(f"{e.get('id')}: sentenceRefs -> unknown {ref}")

    for g in grammar:
        for ref in g.get("sentenceRefs") or []:
            if ref not in sent_ids:
                err(f"{g.get('id')}: sentenceRefs -> unknown {ref}")

    for x in exercises:
        for ref in x.get("relatedVocabulary") or []:
            if ref not in vocab_ids:
                err(f"{x.get('id')}: relatedVocabulary -> unknown {ref}")
        for ref in x.get("relatedExpressions") or []:
            if ref not in expr_ids:
                err(f"{x.get('id')}: relatedExpressions -> unknown {ref}")
        for ref in x.get("relatedGrammar") or []:
            if ref not in gram_ids:
                err(f"{x.get('id')}: relatedGrammar -> unknown {ref}")
        for ref in x.get("relatedSentences") or []:
            if ref not in sent_ids:
                err(f"{x.get('id')}: relatedSentences -> unknown {ref}")

    # 4. Source integrity
    sent_text_by_id = {s.get("id"): s.get("text", "") for s in sentences}
    concatenated = "".join(s.get("text", "") for s in sentences)
    embedded_source = source.get("text", "")

    if embedded_source:
        if ws_normalize(concatenated) != ws_normalize(embedded_source):
            err("source integrity: sentence concatenation does not match source.text "
                "(ignoring whitespace)")

    if args.source:
        try:
            source_txt = Path(args.source).read_text(encoding="utf-8")
            if ws_normalize(concatenated) != ws_normalize(source_txt):
                err("source integrity: sentence concatenation does not match --source file")
        except OSError as e:
            err(f"source: cannot read --source file: {e}")

    # 5. Surface integrity
    for v in vocabulary:
        surf = v.get("surface", "")
        refs = v.get("sentenceRefs") or []
        if not any(surf in sent_text_by_id.get(r, "") for r in refs):
            err(f"{v.get('id')}: surface {surf!r} does not occur in any referenced sentence")

    for e in expressions:
        text = e.get("text", "")
        refs = e.get("sentenceRefs") or []
        if not any(text in sent_text_by_id.get(r, "") for r in refs):
            err(f"{e.get('id')}: text {text!r} does not occur in any referenced sentence")

    # Warnings: bidirectional reference consistency
    refs_by_vocab = {s.get("id"): set(s.get("vocabularyRefs") or []) for s in sentences}
    for v in vocabulary:
        vid = v.get("id")
        for r in v.get("sentenceRefs") or []:
            if vid not in refs_by_vocab.get(r, set()):
                warn(f"{vid}: sentence {r} lists it in sentenceRefs but the sentence "
                     f"does not reference it back in vocabularyRefs")

    # Report
    print(f"Validating: {doc_path}")
    print(f"  sentences: {len(sentences)}  vocabulary: {len(vocabulary)}  "
          f"expressions: {len(expressions)}  grammar: {len(grammar)}  exercises: {len(exercises)}")
    print()

    if schema_problems and "not installed" in schema_problems[0]:
        print("Schema: skipped (jsonschema not installed)")
    elif schema_problems:
        print("Schema: FAIL")
    else:
        print("Schema: pass")

    for w in warnings:
        print(f"  WARN: {w}")

    if errors:
        print()
        print(f"{len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        print()
        print("RESULT: FAIL")
        sys.exit(1)

    if warnings and args.strict:
        print()
        print("RESULT: FAIL (strict mode: warnings are failures)")
        sys.exit(1)

    print()
    print("RESULT: PASS" + (f" ({len(warnings)} warning(s))" if warnings else ""))
    sys.exit(0)


if __name__ == "__main__":
    main()
