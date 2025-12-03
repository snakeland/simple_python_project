# Simple Python Project

<!-- Status -->
[![CI](https://github.com/snakeland/simple_python_project/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/snakeland/simple_python_project/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/snakeland/simple_python_project/branch/main/graph/badge.svg)](https://codecov.io/gh/snakeland/simple_python_project)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/snakeland/simple_python_project)](https://github.com/snakeland/simple_python_project/releases)

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

## Contributing

This project uses a **Git Flow** workflow with separate development and production branches:

- **`develop`** - main development branch (all feature work happens here)
- **`main`** - production releases only (protected, release PRs only)
- **`release/X.Y.Z`** - temporary release branches (created by workflow, merged to main)

### Development workflow

1. **Create feature branch from develop**:
   ```bash
   git checkout develop
   git pull
   git checkout -b feature/your-feature-name
   ```

2. **Make changes using conventional commits**:
   ```bash
   git commit -m "feat: add new calculator function"
   git commit -m "fix: correct edge case in divide"
   git commit -m "docs: update README examples"
   ```

3. **Create PR to develop** (not main):
   - All feature PRs must target `develop`
   - CI runs on both branches (lint + tests on Python 3.10, 3.11, 3.12)
   - PRs require passing CI before merge

4. **Release process** (maintainers only):
   - Trigger manual release workflow from GitHub Actions
   - Workflow creates release PR from develop to main
   - After merge, automated workflow creates tag, GitHub release, and binary

See [RELEASE.md](RELEASE.md) for detailed release process documentation.

### Commit message format

We use [Conventional Commits](https://www.conventionalcommits.org/) for automatic semantic versioning:

- `feat:` - new feature (MINOR version bump: 0.2.0 → 0.3.0)
- `fix:` - bug fix (PATCH version bump: 0.2.0 → 0.2.1)
- `docs:` - documentation only
- `ci:` - CI/CD changes
- `test:` - test updates
- `chore:` - maintenance tasks

Add `!` or `BREAKING CHANGE:` for breaking changes (MAJOR version bump: 0.2.0 → 1.0.0).
