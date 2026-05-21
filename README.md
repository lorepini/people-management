# People Management — Study Tools

Personal exam-prep tools for the ESADE People Management course.

## 🔗 Live links

- **MCQ trainer** — https://lorepini.github.io/people-management/mcq_trainer.html
- **Frameworks cheat sheet (PDF)** — https://lorepini.github.io/people-management/frameworks_cheatsheet.pdf

## Files

- **`mcq_trainer.html`** — Single-file MCQ practice platform. Open in any browser, no server needed. 180 situational questions across 6 blocks (30 per block). Wrong-answer re-queueing, 7-question break prompts, medal system stored in `localStorage`.
- **`frameworks_cheatsheet.pdf`** — Essay-ready cheat sheet, 19 pages. 87 frameworks across the 6 blocks in coloured cards (Core / Key / Supporting), italic one-line summaries, bullet "moves" for each framework.
- **`frameworks_cheatsheet.md`** — Source markdown for the cheat sheet. Edit this, then re-run the build script.
- **`_build_cheatsheet.py`** — Build script: markdown → HTML → PDF via `weasyprint`. Requires Atkinson Hyperlegible font installed locally.
- **`_build_mcq.py`** — Build script for the MCQ data: holds questions in Python, audits option-length parity (correct answer must be within ±10 chars of distractors), injects JSON into `mcq_trainer.html`.
- **`study_sheets_recipe.md`** — The original recipe / design system both artefacts follow.

## Rebuilding the cheat sheet

```bash
pip install markdown weasyprint
python3 _build_cheatsheet.py
```

## Rebuilding the MCQ trainer

```bash
python3 _build_mcq.py
```

## Adapting the MCQ trainer for another subject

Use the dedicated template repo: **https://github.com/lorepini/mcq-template**

Clone it, edit `SUBJECT` and the `TOPIC_n` lists in `_build_mcq.py`, run the script, open the HTML. The template includes the question-writing rulebook and sample questions illustrating the situational/application style.
