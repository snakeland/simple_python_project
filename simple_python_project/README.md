# Simple Python Project

<!-- CI status badge: replace OWNER/REPO with your GitHub repo -->
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
<!-- Link to Copilot action log -->
[Project / Copilot log](Copilot.md)

A tiny, self-contained Python project demonstrating a small package with basic arithmetic functions, a CLI entrypoint, unit tests (pytest), and a requirements.txt.

## What you'll find

- `src/simple_calc` — package with a `calculator` module
- `bin/run_calc.py` — small CLI to run the calculator from the command line
- `tests/` — pytest-based unit tests
- `requirements.txt` — minimal dependencies (pytest)

## Quick start

Create a virtual environment, install the requirements, and run tests:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -q
```

Run the CLI script directly (after activating your venv):

```bash
python bin/run_calc.py add 4 7
# prints the result of 4 + 7
```

Installable package
-------------------

You can make the project installable and add a console script by installing it editable in your venv:

```bash
python -m pip install -e .
```

This will provide a `run-calc` command you can run from anywhere:

```bash
run-calc add 4 7
# prints the result of 4 + 7
```
