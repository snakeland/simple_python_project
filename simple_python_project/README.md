# Simple Python Project

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
