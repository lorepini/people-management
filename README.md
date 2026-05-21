# People Management — Study Tools

Personal exam-prep tools for the ESADE People Management course.

## Files

- **`mcq_trainer.html`** — Single-file MCQ practice platform. Open in any browser, no server needed. 58 questions across 6 blocks. Spaced-repetition (wrong questions re-queue), 7-question break prompts, medal system stored in `localStorage`. Reusable for other subjects — swap the `<script id="quiz-data">` JSON block at the top of the file.
- **`frameworks_cheatsheet.pdf`** — Essay-ready cheat sheet, 19 pages. 87 frameworks across the 6 blocks in coloured cards (Core / Key / Supporting), italic one-line summaries, bullet "moves" for each framework.
- **`frameworks_cheatsheet.md`** — Source markdown for the cheat sheet. Edit this, then re-run the build script.
- **`_build_cheatsheet.py`** — Build script: markdown → HTML → PDF via `weasyprint`. Requires Atkinson Hyperlegible font installed locally.
- **`study_sheets_recipe.md`** — The original recipe / design system both artefacts follow.

## Rebuilding the cheat sheet

```bash
pip install markdown weasyprint
python3 _build_cheatsheet.py
```

## Adapting the MCQ trainer for another subject

1. Copy `mcq_trainer.html` to a new file (e.g. `mcq_trainer_marketing.html`)
2. Replace the contents of `<script id="quiz-data" type="application/json">` near the top with your own JSON following the documented schema
3. Open in browser — progress is keyed off `subjectId`, so different subjects don't collide in `localStorage`
