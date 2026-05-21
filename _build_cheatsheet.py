#!/usr/bin/env python3
"""Build the frameworks cheat sheet PDF.

Pipeline:  .md  ->  preprocess  ->  python-markdown  ->  postprocess  ->  CSS+HTML  ->  weasyprint  ->  PDF
Follows study_sheets_recipe v1 (centred colour-bordered boxes, Atkinson Hyperlegible, white background).
"""
from __future__ import annotations

import re
from pathlib import Path

import markdown as md
from weasyprint import HTML, CSS

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "frameworks_cheatsheet.md"
OUT = ROOT / "frameworks_cheatsheet.pdf"
FONT_DIR = Path("/home/lorepinillos/.local/share/fonts/atkinson")

# ----------------------- 1. Preprocess markdown -------------------------------

def preprocess(text: str) -> str:
    """Fix indentation + insert blank lines so python-markdown parses lists correctly.

    Rules from the recipe:
      - nested bullets need 4-space indentation (not 2)
      - blank line after every heading
      - blank line before any list that follows a paragraph
    """
    lines = text.splitlines()
    out: list[str] = []
    for i, line in enumerate(lines):
        # Convert leading 2-space bullet indentation to 4-space (recursive)
        m = re.match(r"^( +)([-*] )(.*)", line)
        if m:
            spaces, bullet, rest = m.groups()
            depth = len(spaces) // 2
            line = ("    " * depth) + bullet + rest

        # Blank line BEFORE a top-level bullet list that follows a paragraph
        is_top_bullet = re.match(r"^[-*] ", line) is not None
        if is_top_bullet and out and out[-1].strip() and not re.match(r"^\s*[-*] ", out[-1]):
            # previous line is non-blank, non-bullet → insert blank
            out.append("")

        out.append(line)

        # Blank line AFTER every heading
        if line.startswith("#") and i + 1 < len(lines) and lines[i + 1].strip():
            out.append("")
    return "\n".join(out)


# ----------------------- 2. Markdown -> HTML ----------------------------------

def render_html(md_text: str) -> str:
    return md.markdown(
        md_text,
        extensions=["extra", "sane_lists", "attr_list"],
        output_format="html5",
    )


# ----------------------- 3. Postprocess HTML ----------------------------------

# colour mapping for the leading emoji on each H3
COLOR_MAP = {
    "🔴": ("core", "#C0392B"),    # red / Core
    "🔵": ("key", "#2563EB"),     # blue / Key
    "🟣": ("supporting", "#7C3AED"),  # purple / Supporting
    "🟢": ("alt", "#1E8A4C"),     # green (reserved)
    "⚫": ("ink", "#3F3A33"),     # ink (reserved)
}

H3_RE = re.compile(
    r"<h3>(?P<emoji>🔴|🔵|🟣|🟢|⚫)\s*(?P<rest>.*?)</h3>\s*"
    r"(?:<p><em>(?P<summary>.*?)</em></p>\s*)?"
    r"(?P<list><ul>.*?</ul>)",
    re.DOTALL,
)


def wrap_authors(html: str) -> str:
    """Wrap each H3 + italic summary + first <ul> into a coloured card.

    Per recipe: swap colour emojis for CSS dots (emoji font doesn't render in
    Atkinson Hyperlegible), and wrap author headings into bordered cards.
    """

    def repl(m: re.Match[str]) -> str:
        emoji = m.group("emoji")
        rest = m.group("rest")
        summary = m.group("summary") or ""
        body = m.group("list")
        cls, hex_color = COLOR_MAP.get(emoji, ("ink", "#3F3A33"))
        summary_html = f'<p class="card-summary"><em>{summary}</em></p>' if summary else ""
        # CSS dot replaces the unicode coloured emoji (the dot lives inside the title)
        dot = f'<span class="dot" style="background:{hex_color}"></span>'
        return (
            f'<section class="card card-{cls}" style="--col:{hex_color}">'
            f'<div class="card-accent"></div>'
            f'<h3 class="card-title">{dot}{rest}</h3>'
            f'<div class="card-band"></div>'
            f"{summary_html}"
            f'<div class="card-body">{body}</div>'
            f"</section>"
        )

    return H3_RE.sub(repl, html)


# Replace stray emoji dots (e.g. inside the How-to-use intro list) with
# inline CSS dots, so they render even though Atkinson lacks emoji glyphs.
INLINE_EMOJI_RE = re.compile(r"(🔴|🔵|🟣|🟢|⚫)")


def replace_inline_emojis(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        _, hex_color = COLOR_MAP[m.group(1)]
        return f'<span class="dot" style="background:{hex_color}"></span>'
    return INLINE_EMOJI_RE.sub(repl, html)


def wrap_block_sections(html: str) -> str:
    """Wrap H1 (Block headers) blocks into a banner."""

    def repl(m: re.Match[str]) -> str:
        title = m.group(1)
        return f'<div class="block-banner"><h1>{title}</h1></div>'

    return re.sub(r"<h1>(.*?)</h1>", repl, html)


def add_stars_styling(html: str) -> str:
    """Highlight star sequences in titles."""
    return re.sub(r"(★+)", r'<span class="stars">\1</span>', html)


def postprocess(html: str) -> str:
    html = wrap_authors(html)
    html = replace_inline_emojis(html)
    html = wrap_block_sections(html)
    html = add_stars_styling(html)
    return html


# ----------------------- 4. CSS + page ----------------------------------------

CSS_TEXT = f"""
@font-face {{
  font-family: 'Atkinson Hyperlegible';
  src: url('file://{FONT_DIR}/AtkinsonHyperlegible-Regular.ttf') format('truetype');
  font-weight: 400; font-style: normal;
}}
@font-face {{
  font-family: 'Atkinson Hyperlegible';
  src: url('file://{FONT_DIR}/AtkinsonHyperlegible-Bold.ttf') format('truetype');
  font-weight: 700; font-style: normal;
}}
@font-face {{
  font-family: 'Atkinson Hyperlegible';
  src: url('file://{FONT_DIR}/AtkinsonHyperlegible-Italic.ttf') format('truetype');
  font-weight: 400; font-style: italic;
}}
@font-face {{
  font-family: 'Atkinson Hyperlegible';
  src: url('file://{FONT_DIR}/AtkinsonHyperlegible-BoldItalic.ttf') format('truetype');
  font-weight: 700; font-style: italic;
}}

@page {{
  size: A4;
  margin: 14mm 12mm 16mm 12mm;
  @bottom-center {{
    content: "People Management — Frameworks Cheat Sheet · " counter(page) " / " counter(pages);
    font-family: 'Atkinson Hyperlegible', sans-serif;
    font-size: 7.5pt;
    color: #888;
  }}
}}

* {{ box-sizing: border-box; }}
html, body {{
  font-family: 'Atkinson Hyperlegible', sans-serif;
  font-size: 9pt;
  line-height: 1.5;
  color: #232323;
  background: #ffffff;
  margin: 0; padding: 0;
}}

/* Top-of-document title (the H1 before any block) is replaced; use the
   first '.block-banner' rendering for course header too — handled via CSS. */

/* Document intro (very first h1 banner) */
.block-banner:first-of-type {{
  text-align: center;
  margin: 0 0 6pt 0;
  border: 0;
  background: transparent;
  padding: 0;
}}
.block-banner:first-of-type h1 {{
  font-size: 19pt;
  font-weight: 700;
  color: #1f2937;
  letter-spacing: -0.01em;
}}

/* Block banner — stays glued to following content */
.block-banner {{
  margin: 14pt 0 6pt 0;
  padding: 8pt 14pt;
  background: #f3f4f6;
  border-radius: 9px;
  border: 1px solid #e5e7eb;
}}
.block-banner h1 {{
  font-size: 13pt;
  font-weight: 700;
  text-align: center;
  color: #1f2937;
  letter-spacing: -0.01em;
}}

/* H2 — section heads inside a block */
h2 {{
  font-size: 11.5pt;
  font-weight: 700;
  margin: 14pt 0 6pt 0;
  text-align: center;
  color: #1f2937;
  padding-bottom: 4pt;
  border-bottom: 1px solid #e5e7eb;
}}

/* Intro paragraph */
body > p {{
  text-align: center;
  color: #555;
  margin: 4pt 0 12pt 0;
  font-style: italic;
  font-size: 9pt;
}}

/* Lead paragraph after each h2 (e.g. How-to-use) */
ul {{
  margin: 4pt 0 8pt 18pt;
  padding: 0;
}}
li {{
  margin: 1pt 0;
}}
li > ul {{
  margin-top: 2pt;
  margin-bottom: 2pt;
}}

/* Coloured author cards */
.card {{
  page-break-inside: avoid;
  break-inside: avoid;
  margin: 7pt auto;
  padding: 7pt 12pt 8pt 12pt;
  border: 1.5px solid var(--col);
  border-radius: 9px;
  background: #ffffff;
  position: relative;
  width: 96%;
  box-shadow: 0 0 0 1px rgba(0,0,0,0.01);
  orphans: 3;
  widows: 3;
}}
.card-accent {{
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: var(--col);
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}}
.card-title {{
  font-size: 10.4pt;
  font-weight: 700;
  text-align: center;
  margin: 4pt 0 4pt 0;
  color: #1f2937;
  padding: 0 6pt;
}}
.card-band {{
  height: 2px;
  margin: 0 auto 6pt auto;
  width: 70%;
  background: linear-gradient(to right, transparent, var(--col) 40%, var(--col) 60%, transparent);
  opacity: 0.55;
}}
.card-summary {{
  text-align: center;
  font-size: 9pt;
  margin: 0 0 6pt 0;
  color: #4b5563;
  padding: 0 4pt;
}}
.card-summary em {{
  font-style: italic;
}}
.card-body ul {{
  margin: 2pt 0 0 18pt;
  padding: 0;
}}
.card-body li {{
  margin: 1.5pt 0;
}}
.card-body strong {{
  color: #1f2937;
}}

/* Stars */
.stars {{
  color: #d97706;
  letter-spacing: 1px;
  font-size: 8.4pt;
  white-space: nowrap;
}}

/* Inline coloured dot (replaces the unicode emoji which Atkinson lacks) */
.dot {{
  display: inline-block;
  width: 8.5px;
  height: 8.5px;
  border-radius: 50%;
  margin-right: 6px;
  vertical-align: middle;
  position: relative;
  top: -1px;
}}

/* Horizontal rule */
hr {{
  border: 0;
  border-top: 1px dashed #d1d5db;
  margin: 12pt auto;
  width: 80%;
}}

/* Bold author names in concept bullets */
strong {{
  font-weight: 700;
}}

em {{
  font-style: italic;
}}
"""


# ----------------------- 5. Build --------------------------------------------

def build() -> None:
    md_text = SRC.read_text(encoding="utf-8")
    md_text = preprocess(md_text)
    html_body = render_html(md_text)
    html_body = postprocess(html_body)

    html_doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Frameworks Cheat Sheet</title></head>
<body>
{html_body}
</body></html>"""

    HTML(string=html_doc, base_url=str(ROOT)).write_pdf(
        target=str(OUT),
        stylesheets=[CSS(string=CSS_TEXT)],
    )
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
