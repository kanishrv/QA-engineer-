# QA Assessment – Job Application Workflow

A local mock hiring portal plus browser tests. Submission scenarios run locally and never send fake applications to a production portal.

## Stack
Python 3.10+, Flask, pytest, Playwright.

## Run
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
python app.py
```
Open http://127.0.0.1:5000. In another terminal:
```bash
pytest -q
```

## Contents
- `app.py`: local mock application
- `tests/test_application.py`: browser automation
- `tests/test_cases.md`: 20 manual scenarios
- `docs/test_plan.md`: scope and prioritization
- `bugs/`: reporting template and findings log

## Important
Run the suite yourself and record the actual output before submitting. No test results or production-portal defects are claimed in advance. Replace placeholder links in the assessment form with your real repository/demo links. Be prepared to explain the tests and adjust them based on your own observations.\n