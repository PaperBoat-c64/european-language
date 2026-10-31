#!/usr/bin/env python3
"""
Render a European Language Studio learning document to HTML + DOCX.

Reads a learning-document JSON (schemas/learning-document.schema.json),
injects it into the HTML template (assets/templates/packet.html), and
builds a matching linear DOCX study document.

Usage:
    python3 render_packet.py --data document.json --output-dir . --stem slug
    python3 render_packet.py --data document.json --output-dir . --stem slug --palette pastel
    python3 render_packet.py --data document.json --output-dir . --stem slug --html --docx

By default both HTML and DOCX are written. The DOCX uses python-docx when
available and falls back to a minimal raw-XML document otherwise.
"""

import argparse
import io
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_ROOT = HERE.parent
TEMPLATE_PATH = SKILL_ROOT / "assets" / "templates" / "packet.html"
PALETTE_DIR = SKILL_ROOT / "assets" / "palettes"

DEFAULT_PALETTE = [
    "#E74C3C", "#E67E22", "#F1C40F", "#2ECC71", "#1ABC9C", "#3498DB",
    "#9B59B6", "#E91E63", "#16A085", "#D35400", "#2980B9", "#8E44AD",
]


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_palette(name: str) -> list:
    palette_file = PALETTE_DIR / f"{name}.json"
    if palette_file.exists():
        try:
            data = json.loads(palette_file.read_text(encoding="utf-8"))
            if isinstance(data.get("colors"), list) and data["colors"]:
                return data["colors"]
        except (json.JSONDecodeError, OSError):
            pass
    return DEFAULT_PALETTE


def assign_colors(vocabulary: list, palette: list) -> dict:
    """Map vocabulary id -> color, cycling through the palette in reading order."""
    return {v["id"]: palette[i % len(palette)] for i, v in enumerate(vocabulary)}


def html_escape(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_html(data: dict, palette: list) -> str:
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    title = html_escape((data.get("meta") or {}).get("title", "Study packet"))

    packet_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    palette_json = json.dumps(palette, ensure_ascii=False)

    html = template.replace("{{TITLE}}", title)
    html = html.replace("{{PACKET_JSON}}", packet_json)
    html = html.replace("{{PALETTE_JSON}}", palette_json)
    return html


# ---------------------------------------------------------------------------
# DOCX
# ---------------------------------------------------------------------------

def _hex_to_rgb(hex_color: str):
    hex_color = (hex_color or "").lstrip("#")
    if len(hex_color) != 6:
        return None
    try:
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def render_docx(data: dict, color_map: dict) -> bytes:
    try:
        from docx import Document
        from docx.shared import Pt, RGBColor, Cm
        from docx.enum.text import WD_ALIGN_PARAGRAPH
    except ImportError:
        print("Warning: python-docx not installed; writing minimal DOCX.", file=sys.stderr)
        return _render_docx_minimal(data, color_map)

    doc = Document()
    meta = data.get("meta") or {}
    source = data.get("source") or {}
    sentences = data.get("sentences") or []
    vocabulary = data.get("vocabulary") or []
    expressions = data.get("expressions") or []
    grammar = data.get("grammar") or []
    exercises = data.get("exercises") or []
    qa = data.get("qa") or {}

    for section in doc.sections:
        section.top_margin = Cm(2.4)
        section.bottom_margin = Cm(2.4)
        section.left_margin = Cm(2.4)
        section.right_margin = Cm(2.4)

    style = doc.styles["Normal"]
    style.font.size = Pt(11.5)
    style.font.name = "Calibri"
    style.paragraph_format.line_spacing = 1.5

    def heading(text, size=15, before=18, after=8, color=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(size)
        if color:
            r.font.color.rgb = RGBColor(*color)
        return p

    def para(text="", size=11.5, italic=False, bold=False, color=None, after=4):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(after)
        if text:
            r = p.add_run(text)
            r.font.size = Pt(size)
            r.italic = italic
            r.bold = bold
            if color:
                r.font.color.rgb = RGBColor(*color)
        return p

    def colored_run(p, text, hex_color, bold=False, size=11.5, italic=False):
        r = p.add_run(text)
        r.bold = bold
        r.italic = italic
        r.font.size = Pt(size)
        rgb = _hex_to_rgb(hex_color)
        if rgb:
            r.font.color.rgb = RGBColor(*rgb)
        return r

    lang_names = {"en": "English", "fr": "French", "es": "Spanish", "de": "German",
                  "it": "Italian", "pt": "Portuguese", "nl": "Dutch", "sv": "Swedish",
                  "no": "Norwegian", "da": "Danish"}

    # Title + metadata
    title_p = doc.add_paragraph()
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_p.add_run(meta.get("title", "Study packet"))
    title_run.bold = True
    title_run.font.size = Pt(24)
    title_p.paragraph_format.space_after = Pt(4)

    meta_parts = []
    if meta.get("textLanguage"):
        meta_parts.append(lang_names.get(meta["textLanguage"], meta["textLanguage"]))
    if meta.get("explanationLanguage"):
        meta_parts.append("→ " + meta["explanationLanguage"])
    if meta.get("genre"):
        meta_parts.append(meta["genre"])
    if meta.get("register"):
        meta_parts.append(meta["register"])
    if meta_parts:
        m = doc.add_paragraph()
        m.alignment = WD_ALIGN_PARAGRAPH.CENTER
        mr = m.add_run(" · ".join(meta_parts))
        mr.font.size = Pt(10)
        mr.font.color.rgb = RGBColor(128, 128, 128)
        m.paragraph_format.space_after = Pt(20)

    # Full translation (paragraph-aligned, reconstructed from sentences)
    heading("Translation", color=(224, 40, 60))
    by_para = {}
    for s in sentences:
        by_para.setdefault(s.get("paragraph", 1), []).append(s)
    for pnum in sorted(by_para):
        para_text = " ".join(s.get("translation", "") for s in by_para[pnum])
        para(para_text, after=8)

    # Reading (sentence-aligned)
    heading("Reading", color=(224, 40, 60))
    for s in sentences:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1)
        colored_run(p, s.get("text", ""), "#000000", bold=True, size=12.5)
        p2 = doc.add_paragraph()
        p2.paragraph_format.space_after = Pt(6)
        r2 = p2.add_run(s.get("translation", ""))
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(90, 90, 90)
        if s.get("literal"):
            p3 = doc.add_paragraph()
            p3.paragraph_format.space_after = Pt(6)
            r3 = p3.add_run(s["literal"])
            r3.italic = True
            r3.font.size = Pt(9.5)
            r3.font.color.rgb = RGBColor(140, 140, 140)

    # Vocabulary table
    heading("Vocabulary", color=(224, 40, 60))
    if vocabulary:
        table = doc.add_table(rows=1, cols=5)
        table.style = "Light Grid Accent 1"
        hdr = ["Word", "Lemma", "POS", "Meaning in context", "Morphology"]
        for i, htext in enumerate(hdr):
            cell = table.rows[0].cells[i]
            cell.text = htext
            for p in cell.paragraphs:
                for r in p.runs:
                    r.bold = True
                    r.font.size = Pt(9.5)
        for v in vocabulary:
            row = table.add_row().cells
            vals = [
                v.get("surface", ""),
                v.get("lemma", ""),
                v.get("pos", ""),
                v.get("meaningInContext", ""),
                (v.get("morphology") or {}).get("description", ""),
            ]
            for i, val in enumerate(vals):
                row[i].text = ""
                p = row[i].paragraphs[0]
                run = p.add_run(val)
                run.font.size = Pt(9.5)
                if i == 0 and v.get("id") in color_map:
                    rgb = _hex_to_rgb(color_map[v["id"]])
                    if rgb:
                        run.font.color.rgb = RGBColor(*rgb)
                        run.bold = True
        doc.add_paragraph()
    else:
        para("No vocabulary annotated for this text.", italic=True)

    # Expressions
    heading("Expressions", color=(224, 40, 60))
    if expressions:
        for e in expressions:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(1)
            colored_run(p, e.get("text", ""), "#000000", bold=True)
            tag = f"  [{e.get('type', '')} · {e.get('register', 'neutral')}]"
            p.add_run(tag).font.color.rgb = RGBColor(150, 150, 150)
            para(e.get("meaningInContext", ""), after=2)
            if e.get("literalMeaning"):
                para("Literal: " + e["literalMeaning"], size=9.5, italic=True, color=(140, 140, 140), after=8)
            else:
                para("", after=8)
    else:
        para("No fixed expressions or idioms singled out for this text.", italic=True)

    # Grammar
    heading("Grammar", color=(224, 40, 60))
    if grammar:
        for g in grammar:
            para(g.get("title", ""), bold=True, after=2)
            para(g.get("explanation", ""), after=4)
            if g.get("pattern"):
                para(g["pattern"], size=10, color=(120, 120, 120), after=4)
            if g.get("pitfalls"):
                para("Common errors: " + "; ".join(g["pitfalls"]), size=10, italic=True, after=8)
            else:
                para("", after=8)
    else:
        para("No grammar points explained for this text.", italic=True)

    # Exercises + answer key
    heading("Exercises", color=(224, 40, 60))
    if exercises:
        for x in exercises:
            para(f"{x.get('id', '')}  [{x.get('type', '')} · {x.get('difficulty', '')}]  {x.get('prompt', '')}", bold=True, after=3)
            ans = x.get("answer") or {}
            if ans.get("key"):
                para("Answer: " + ans["key"], after=2)
            if ans.get("model"):
                para("Model answer: " + ans["model"], after=2)
            if ans.get("rubric"):
                for cr in ans["rubric"]:
                    para("  • " + cr, size=10, after=1)
            if ans.get("explanation"):
                para(ans["explanation"], size=10, italic=True, after=8)
            else:
                para("", after=8)
    else:
        para("No exercises for this text.", italic=True)

    # Review cards table
    heading("Review cards", color=(224, 40, 60))
    cards = []
    for v in vocabulary:
        back = f"{v.get('lemma', '')} ({v.get('pos', '')}) — {v.get('meaningInContext', '')}"
        cards.append((v.get("surface", ""), back))
    for e in expressions:
        back = f"[{e.get('type', '')} · {e.get('register', '')}] {e.get('meaningInContext', '')}"
        cards.append((e.get("text", ""), back))
    if cards:
        table = doc.add_table(rows=1, cols=2)
        table.style = "Light Grid Accent 1"
        for i, htext in enumerate(["Front", "Back"]):
            cell = table.rows[0].cells[i]
            cell.text = htext
            for p in cell.paragraphs:
                for r in p.runs:
                    r.bold = True
                    r.font.size = Pt(9.5)
        for front, back in cards:
            cells = table.add_row().cells
            for i, val in enumerate((front, back)):
                cells[i].text = ""
                run = cells[i].paragraphs[0].add_run(val)
                run.font.size = Pt(9.5)
        doc.add_paragraph()

    # QA
    checks = (qa or {}).get("checks") or []
    if checks:
        heading("Quality check", color=(224, 40, 60))
        para(f"Summary: {(qa.get('summary') or '').upper()}", bold=True, after=4)
        for c in checks:
            para(f"{c.get('id', '')}  {c.get('name', '')}: {c.get('status', '')}", size=10, after=1)
            if c.get("notes"):
                para(c["notes"], size=9.5, italic=True, color=(120, 120, 120), after=3)

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def _xml_escape(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _render_docx_minimal(data: dict, color_map: dict) -> bytes:
    """Fallback DOCX without python-docx: raw OOXML, headings + colored paragraphs."""
    meta = data.get("meta") or {}
    sentences = data.get("sentences") or []
    vocabulary = data.get("vocabulary") or []
    expressions = data.get("expressions") or []
    grammar = data.get("grammar") or []
    exercises = data.get("exercises") or []

    body = []

    def p(text="", bold=False, italic=False, size=22, color=None, after=40):
        rpr = f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        if bold:
            rpr += "<w:b/>"
        if italic:
            rpr += "<w:i/>"
        if color:
            rpr += f'<w:color w:val="{color}"/>'
        body.append(
            f'<w:p><w:pPr><w:spacing w:after="{after}"/></w:pPr>'
            f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{_xml_escape(text)}</w:t></w:r></w:p>'
        )

    def heading(text):
        p(text, bold=True, size=30, color="E0283C", after=120)

    # Title
    p(meta.get("title", "Study packet"), bold=True, size=40, after=160)

    heading("Translation")
    for s in sentences:
        p(s.get("translation", ""), after=60)

    heading("Reading")
    for s in sentences:
        p(s.get("text", ""), bold=True, size=26, after=20)
        p(s.get("translation", ""), size=22, color="5A5A5A", after=80)

    heading("Vocabulary")
    for v in vocabulary:
        color = color_map.get(v.get("id", ""), "").lstrip("#") or "000000"
        p(f'{v.get("surface", "")}  ({v.get("lemma", "")}, {v.get("pos", "")})',
          bold=True, color=color, after=20)
        p(f'{v.get("meaningInContext", "")}', size=22, after=40)

    heading("Expressions")
    for e in expressions:
        p(f'{e.get("text", "")}  [{e.get("type", "")} · {e.get("register", "neutral")}]', bold=True, after=20)
        p(e.get("meaningInContext", ""), size=22, after=40)

    heading("Grammar")
    for g in grammar:
        p(g.get("title", ""), bold=True, after=20)
        p(g.get("explanation", ""), size=22, after=40)

    heading("Exercises")
    for x in exercises:
        p(f'{x.get("id", "")}  {x.get("prompt", "")}', bold=True, after=20)
        ans = x.get("answer") or {}
        if ans.get("key"):
            p("Answer: " + ans["key"], size=22, after=40)
        elif ans.get("model"):
            p("Model answer: " + ans["model"], size=22, after=40)

    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        + "".join(body)
        + "<w:sectPr><w:pgSz w:w=\"11906\" w:h=\"16838\"/>"
        "<w:pgMar w:top=\"1360\" w:right=\"1360\" w:bottom=\"1360\" w:left=\"1360\"/></w:sectPr>"
        "</w:body></w:document>"
    )

    buf = io.BytesIO()
    import zipfile
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(
            "[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            "</Types>",
        )
        zf.writestr(
            "_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            "</Relationships>",
        )
        zf.writestr("word/document.xml", document_xml)
    return buf.getvalue()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Render a European Language Studio document")
    parser.add_argument("--data", required=True, help="Path to the learning-document JSON")
    parser.add_argument("--output-dir", default=".", help="Directory to write outputs into")
    parser.add_argument("--stem", default="study", help="Output file stem")
    parser.add_argument("--palette", default="default", help="Palette name (default, pastel, high-contrast)")
    parser.add_argument("--html", action="store_true", help="Render HTML only")
    parser.add_argument("--docx", action="store_true", help="Render DOCX only")
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        print(json.dumps({"error": f"Data file not found: {data_path}"}), file=sys.stderr)
        sys.exit(1)

    data = load_json(data_path)
    palette = load_palette(args.palette)
    color_map = assign_colors(data.get("vocabulary", []), palette)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.stem

    render_both = not args.html and not args.docx
    results = {}
    errors = {}

    if render_both or args.html:
        try:
            html = render_html(data, palette)
            html_path = out_dir / f"{stem}.html"
            html_path.write_text(html, encoding="utf-8")
            results["html"] = str(html_path.resolve())
        except Exception as e:  # noqa: BLE001
            errors["html"] = str(e)
            print(f"Warning: HTML generation failed: {e}", file=sys.stderr)

    if render_both or args.docx:
        try:
            docx = render_docx(data, color_map)
            docx_path = out_dir / f"{stem}.docx"
            docx_path.write_bytes(docx)
            results["docx"] = str(docx_path.resolve())
        except Exception as e:  # noqa: BLE001
            errors["docx"] = str(e)
            print(f"Warning: DOCX generation failed: {e}", file=sys.stderr)

    status = "ok" if not errors else "partial"
    print(json.dumps({
        "status": status,
        "output_dir": str(out_dir.resolve()),
        "results": results,
        "errors": errors or None,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
