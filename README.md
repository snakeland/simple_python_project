# Simple Python Project

<!-- Status -->
[![CI](https://github.com/snakeland/simple_python_project/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/snakeland/simple_python_project/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/snakeland/simple_python_project/branch/main/graph/badge.svg)](https://codecov.io/gh/snakeland/simple_python_project)

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

Makefile shortcuts
------------------

If you prefer shortcuts, the repository contains a `Makefile` with convenient targets. From the repository root copy/paste these commands (zsh):

```bash
# create a venv
make venv

# install editable package + test extras
make install

# run test suite
make test

# run the CLI (set ARGS for arguments, e.g. ARGS="add 4 7")
make cli ARGS="add 4 7"
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

## Pre-built macOS binary

Download the latest Apple Silicon (arm64) binary from [Releases](https://github.com/snakeland/simple_python_project/releases):

```bash
# Using GitHub CLI
gh release download --pattern 'run-calc-macos-arm64'

# Remove quarantine and make executable
xattr -d com.apple.quarantine run-calc-macos-arm64
chmod +x run-calc-macos-arm64

# Run it
./run-calc-macos-arm64 add 10 20

# Optional: install to PATH
sudo mv run-calc-macos-arm64 /usr/local/bin/run-calc
run-calc multiply 6 7
```

**Note**: macOS marks downloaded files as quarantined. The `xattr -d` command removes this flag so the binary runs without Gatekeeper warnings.
