# Study Sheets — Recipe (v1)

> How to build the full study system used for this course.
> Reusable for any exam-heavy course (lots of authors, lots of concepts, an essay/MCQ exam).

---

## What this system produces

Four complementary artefacts. Each does *one* job well.

- **Flashcards (per session)** — for active recall during the week
- **Author cheat sheet (full, A–Z)** — for citing authors in essay answers
- **Main authors cheat sheet** — for last-minute revision, the essay anchors only
- **MCQ mock exam** — for self-testing under exam conditions

Don't merge them. One source = one purpose.

---

## Core principles (read first)

- **Content first, design later** — get the markdown right before touching the PDF.
- **Lists, not paragraphs** — short bullets beat sentences with semicolons.
- **One source of truth** — the `.md` file. The PDF is generated from it.
- **No giveaways** — see the anti-patterns section below.
- **Accessibility ≠ childish** — clean professional fonts work for everyone.

---

## Step 1 — Extract concepts from the course

Per session, for every concept worth knowing, capture five fields:

- **Term** — the name of the concept (e.g. "Risk Society").
- **Author / source** — who said it (e.g. Ulrich Beck).
- **Definition** — what it means, in 1–2 lines.
- **Extra** — the quote, example, or detail you'd add in an exam.
- **Exam priority** — ★ to ★★★★★, based on how much the professor pushed it.

Sources to mine:
- the slides (especially repeated headers / colour-blocks)
- the set readings (look at section titles)
- exam-prompt hints the professor gave in class

Keep one digest file per session while you read. Don't try to organise yet.

---

## Step 2 — Build the flashcards (one HTML deck per session)

The flashcard deck has two modes:

- **Flashcards** — one concept at a time, flip to reveal.
- **Pinterest view** — all concepts visible at once, sorted by tier.

Each card needs:

- emoji icon (visual hook)
- category tag (e.g. risk, ethics, framework)
- size (large / medium / small — for the masonry layout)
- term
- definition
- extra (quote, example, exam priority)

Format roughly 30–35 cards per session. Tag the top ones ★★★★★ so the eye finds them first in Pinterest view.

---

## Step 3 — Build the full author cheat sheet (A–Z)

This is the heaviest artefact and the one you'll cite from most.

### 3.1 — Choose the colour code

Five colours, max two per author:

- 🔴 critical of markets / egalitarian-left
- 🔵 pro-market / neoliberal
- 🟢 sustainability / future generations
- 🟣 pragmatist / institutionalist ("it depends")
- ⚫ ethics / normative philosophy

The colour is a **memory hook**, not a label. Write the nuance in the concept bullets.

### 3.2 — Organise by author, A–Z

Not by theme. Not by tier. A–Z is what your eyes do under exam stress.

Some authors span themes (Sandel, Rodrik) — tag every session they appear in.

### 3.3 — Author block template

Use this exact shape for every author:

```markdown
### 🎨 Surname · S#
*One-line summary of their overall argument.*
- **Concept name** ★★★★
  - one sub-bullet per idea
  - keep each sub-bullet to one short line
- **Next concept** ★★★
  - same shape again
```

Strict rules:

- **Colour dot BEFORE the name** (so the eye reads camp → name → topic)
- **Session codes (S#) after the name, nothing else**
  - no "philosopher", no book title, no year — the slides already gave that
- **Italic one-line summary** under the name
- **Every concept** the author explains, not only the headline one
  - example: Beck has *risk society* AND *reflexive modernisation* AND *manufactured risks*
- **Sub-bullets, not run-on text** — split at every `;` or em-dash
- **Stars per concept**, not per author

### 3.4 — Things to leave out

- "Debate vs X" lines (clutter; pair authors in the timeline section instead)
- Book titles, dates, where they're from (unless the date is the *point*, e.g. Crenshaw 1989)
- Page references and citation strings

### 3.5 — Extra sections at the end

After all authors, add (in this order):

- **Timeline** — major dates in one column (Bretton Woods 1944, WTO 1995, etc.)
- **SDGs** — list the 17 goals, then map each course theme → lead SDG → hook author
- **Caveat** — one line reminding yourself the colour is a heuristic

---

## Step 4 — Build the main authors sheet

This is the *condensed* version for the last 48 hours before the exam.

### 4.1 — Selection

Keep ~20 authors. Pick the ones you'd actually *build an essay around*. Drop the supporting ones.

Heuristic: an author goes in only if they have at least one ★★★★★ concept *and* you can imagine writing 200 words about them.

### 4.2 — Template

Same per-author block as the full sheet, but:

- **2–3 top concepts** only
- **Each concept = one line**, not a sub-bullet tree
- Example:

```markdown
### 🔴 Sandel · S2 · S10
*Market-driven meritocracy corrodes the common good and feeds populism.*
- **Hubris vs humiliation** ★★★★★ — winners forget luck; losers carry self-doubt → populist fuel
- **Outsourcing moral judgement** ★★★★★ — markets/experts empty democracy; authoritarian identity fills the void
```

### 4.3 — Layout difference

The main sheet uses **centred colour-bordered boxes**, not a left-only colour bar.

Why: a left bar makes the page feel "left-leaning" visually and pushes the eye sideways. A centred box with a full border *and* a thicker top accent reads balanced and lets you scan vertically.

---

## Step 5 — Build the MCQ mock exam

### 5.1 — Question rules

- **10 questions per session** (40 minimum across a course; 100 for full coverage).
- **Each question has exactly one best answer.**
- **All four options ~ same length.** A longer correct option is the #1 tell — examiners avoid it, you should too.
- **Distractors swap close concepts** — that's where exam confusion actually happens:
  - Risk vs Uncertainty (Knight) — easy to swap with McKinsey's 4 levels
  - Black Swan (Taleb) vs Grey Rhino (Wucker) — opposite logic
  - Anti-fragile vs Resilient vs Robust — adjacent on the spectrum
  - Filter Bubble (Pariser) vs Echo Chamber — algorithmic vs self-selected
  - Bobbitt's five arguments (a/b/c/d/e) — all about the nation-state crisis
  - The three corners of Rodrik's trilemma — easy to mix up
  - Sandel's two "misdiagnoses" (nativism / dislocation) vs his actual view
- **Author swaps work as distractors** — Beck ↔ Giddens ↔ Castiñeira ↔ Taleb, etc.

### 5.2 — The answer key trap (and how to avoid it)

The big mistake I made first time:

- I made the correct answer cycle `A, B, C, D, A, B, C, D…`
- Distribution looked balanced (25 each) — *but* the *order* was perfectly predictable
- A test-wise student notices "every 4th is A" in the first page and cheats the rest

Fix:

- Take a balanced list, e.g. `['A']*25 + ['B']*25 + ['C']*25 + ['D']*25`
- **Shuffle it randomly** with a seed
- **Check no 3-in-a-row** of the same letter
- **Reject the i % 4 cycle** explicitly

Pseudocode:

```python
import random
base = ['A']*25 + ['B']*25 + ['C']*25 + ['D']*25
rng = random.Random(seed)
while True:
    seq = base[:]; rng.shuffle(seq)
    # max run check
    if max_run(seq) <= 2 and seq != cycle_pattern:
        break
```

Then place each question's correct option at the target letter position, keeping the relative order of the three distractors.

### 5.3 — Answer key location

- All answers + one-line rationales at the **end** of the PDF, not next to the questions.
- One rationale per question — say *what the trap was* (which neighbouring concept the distractor borrowed from).
- Show the distribution + max-run number in the legend, so future-you can sanity-check.

---

## The design system (what makes the PDFs look right)

### Colours (use these exact hex codes)

- red `#C0392B` · blue `#2563EB` · green `#1E8A4C` · purple `#7C3AED` · ink `#3F3A33`
- Background: white `#FFFFFF` (not cream, not beige — they feel hot/yellow under stress)
- Text: `#232323` (not pure black — softer on the eye)

### Stars

- ★★★★★ — essay-anchor, must-know
- ★★★★ — strong supporting cite
- ★★★ / ★★ — useful detail, exam-detail level

### Font

- **Atkinson Hyperlegible** — designed by the Braille Institute, accessibility-grade, looks like a normal clean professional sans-serif.
- **Not OpenDyslexic** — the heavy weighted bottoms read as childish for many people.
- Body size ~9pt, line-height 1.5.
- Left-align body text (never justify). Centre only headings.

### Layout

- **Centred colour-bordered boxes** for authors, balanced left-and-right
  - full border in author's colour, 1.5px
  - thicker top edge (4px) in the same colour as an accent
  - rounded corners (8–9px radius)
  - short colour band under the name, fading on both sides (symmetric)
- **White card on light-grey background** for visual breathing room
- **Reference sections** (How to use, Timeline, SDGs) → neutral white panel with grey border, same shape

### Nested lists in markdown

This trips up `python-markdown`. The fix:

- Nested bullets need **4-space indentation**, not 2.
- **Blank line** before any list that follows a paragraph.
- **Blank line** after every heading.

You can write 2-space indented and have a preprocessor add the spaces and blanks before passing to markdown.

---

## Build pipeline (technical)

If you want to make this yourself, the chain is:

```
.md  →  python-markdown  →  HTML  →  weasyprint  →  PDF
```

Tools needed:

- `python3` with `markdown` package
- `weasyprint` (`pip install weasyprint`)
- Font files locally (`.otf` or `.ttf`) referenced with `@font-face` and a `file://` URL
- Optional: `pymupdf` (`fitz`) to render preview pages as PNG to check visually

The Python script does three jobs:

- **Preprocess the markdown** (fix nested list indentation, add blank lines)
- **Post-process the generated HTML** (swap colour emojis for CSS dots, wrap author headings into bordered cards)
- **Inject CSS + @font-face** and call weasyprint

Keep the script alongside the `.md` — the `.md` is human, the script is machine.

---

## Writing patterns that work

### A good concept bullet

```markdown
- **Black swan** ★★★★★
  - an unforeseeable chance event
  - with huge repercussions
  - identified only after the fact
  - strategy: focus on (known) consequences, not (unknown) probabilities
```

What makes it work:

- bold concept name + stars on one line
- each sub-bullet is *one idea*, not a sentence with sub-clauses
- the last bullet often gives the *exam move* (what to actually say)

### A good summary line (one-line author italic)

- States the author's overall argument in one breath
- Examples that work:
  - "Modernity's own side-effects became its dominant threats." (Beck)
  - "Globalization is a political choice with hard trade-offs — *it depends*." (Rodrik)
  - "Migration/asylum policy is the litmus test of the Rule of Law." (de Lucas)

### A good MCQ distractor

- Plausibly correct to someone who *half*-remembers
- Most often a **neighbouring concept** (the trap is conceptual proximity)
- Sometimes an **author swap** (right concept, wrong author)
- Same length and tone as the correct option

Avoid silly distractors. They make the test feel easy and don't help you learn the real confusions.

---

## Anti-patterns (mistakes I made; don't repeat)

- **Cream/beige backgrounds.** Felt warm and inviting in theory; felt *hot and crowded* in practice. Use white or very light grey.
- **OpenDyslexic.** Technically dyslexia-friendly; reads as childish to many adults. Use Atkinson Hyperlegible.
- **Long correct option.** The #1 way to leak the answer in MCQs.
- **`i % 4` answer cycle.** Looks balanced, is fully predictable. Use a seeded random shuffle with a max-run check.
- **Run-on paragraphs with `;` separators.** Hard to read under stress. Bullet every clause.
- **Left-only colour bar.** Makes the page feel directionally weighted. Centre the whole box.
- **"Where they're from" filler.** "German-born sociologist of the 1980s" — eats line-space, never used in an exam.
- **Mixing artefacts.** Don't fold the MCQ key into the cheat sheet, or add stars to flashcards in a different scheme than the cheat sheet uses. Each artefact has one job.

---

## Workflow (the order I'd do it next time)

1. **Read everything once** — slides + readings + class notes — and dump concepts as a flat list per session.
2. **Build flashcards** (per session) — forces you to write definitions in your own words.
3. **Build the full author cheat sheet in `.md`** — *don't touch the PDF yet*.
4. **Show the `.md` to yourself the next day** — does it read as a study tool, or as a transcript?
5. **Render the PDF** — only when the content is solid.
6. **Distill the main sheet** from the full one — *don't write it fresh*, pick what survives.
7. **Build the MCQ mock** — fresh questions, not flashcard-clones.
8. **Take the mock cold** a week before the exam. Check the answer key only after.

---

## A short list of things that genuinely help under exam pressure

- A **one-line summary** per author you can recall before you write the paragraph.
- A **mental colour** for each author (the dot trick).
- Two or three **debates** you've already framed in your head (so the "compare and contrast" essay writes itself).
- A list of **dates** so you can anchor periods without remembering decades vaguely.
- The list of **SDGs you can plausibly cite** for each theme.

That's it. The rest is just having read enough.
