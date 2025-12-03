# Copilot Project Log

Development log and changelog for the simple_python_project. Documents key decisions, features, and improvements made during development.

## Project Overview

**Project**: simple_python_project
**Purpose**: Professional Python package demonstrating modern best practices including:
- Arithmetic calculator functions with CLI interface
- Comprehensive testing (pytest) with 100% coverage
- Modern tooling (ruff for linting/formatting, pre-commit hooks)
- Full CI/CD automation (GitHub Actions, Dependabot, binary builds)
- Professional packaging (pyproject.toml, console script entry point)

## Current Status (2025-12-01)

- **Tests**: 25/25 passing, 100% coverage maintained
- **Python versions**: 3.10, 3.11, 3.12 (CI matrix)
- **Code quality**: ruff + pre-commit hooks enforced
- **Branch protection**: Main and develop branches require PRs with passing CI
- **Automation**: Dependabot for dependencies, manual Git Flow releases with automated finalization
- **Workflow**: Git Flow (develop → release/X.Y.Z → main) with manual release triggering

---

## Recent Changes

### 2025-12-01: Git Flow Workflow Implementation

**Context**: After encountering multiple consecutive failures with automatic semantic-release workflow (branch protection conflicts, permission issues, invalid CLI flags), we pivoted to a manual Git Flow approach for better control and reliability.

**Strategy Change**:
- **Old approach**: Automatic semantic-release on every push to main (failed 4-5 times with different errors)
- **New approach**: Manual release workflow with Git Flow branching model
  - `develop` - main development branch (feature work)
  - `main` - production releases only (protected)
  - `release/X.Y.Z` - temporary release branches

**Implementation**:

1. **Created `develop` branch** (PR pending):
   - Branched from main
   - Will be protected like main (require PRs, passing CI)
   - All feature development happens here

2. **New workflows**:
   - **`.github/workflows/create-release.yml`** (manual trigger):
     - Triggered via GitHub Actions UI from develop branch only
     - Accepts release type: auto/patch/minor/major
     - Uses semantic-release to analyze commits and determine version
     - Creates release branch (`release/X.Y.Z`)
     - Updates `pyproject.toml` version and `CHANGELOG.md`
     - Creates PR to main with detailed changelog excerpt
     - Labels PR with "release"

   - **`.github/workflows/finalize-release.yml`** (automatic):
     - Triggers when release PR merges to main (commit message: "chore(release): X.Y.Z")
     - Validates version format and changelog entry
     - Creates and pushes git tag (`vX.Y.Z`)
     - Creates GitHub release with changelog notes
     - **Critical**: Merges main back to develop (keeps branches in sync)
     - Triggers binary build workflow

3. **Updated workflows**:
   - **`.github/workflows/ci.yml`**: Now runs on both `main` and `develop` branches
   - **`.github/workflows/build-macos.yml`**: No changes (already runs on main pushes)

4. **Deleted workflows**:
   - **`.github/workflows/semantic-release.yml`**: Old automatic workflow (replaced by create + finalize split)

5. **Documentation**:
   - **`RELEASE.md`**: Completely rewritten with Git Flow process (310+ lines)
     - Branch strategy explanation
     - Step-by-step release process
     - Conventional commit format guide
     - Multiple scenario examples
     - Troubleshooting section
   - **`README.md`**: Added contributing section with development workflow
   - **`Copilot.md`**: This entry documenting the change

**Benefits of new approach**:
- ✅ Manual control over when releases happen
- ✅ Review release PR before finalizing (catch issues early)
- ✅ Separation of development (develop) and production (main)
- ✅ Clear release branch history (`release/X.Y.Z`)
- ✅ Automated post-merge tasks (tag, release, binary, merge back)
- ✅ No more workflow permission/branch conflicts

**Trade-offs**:
- ❌ Requires manual trigger (not automatic on every merge)
- ❌ Slightly more complex branching model
- ✅ BUT: Much more reliable and controllable

**Next steps**:
- Merge this workflow implementation to main
- Set up branch protection for both main and develop
- Test end-to-end release process
- Consider adding release type recommendations in PR template

**Files modified**:
- Created: `.github/workflows/create-release.yml`
- Created: `.github/workflows/finalize-release.yml`
- Modified: `.github/workflows/ci.yml`
- Deleted: `.github/workflows/semantic-release.yml`
- Rewritten: `RELEASE.md`
- Modified: `README.md` (contributing section)
- Modified: `Copilot.md` (this entry)

---

## Current Status (2025-12-01) [OLD - Before Git Flow]

- **Tests**: 25/25 passing, 100% coverage maintained
- **Python versions**: 3.10, 3.11, 3.12 (CI matrix)
- **Code quality**: ruff + pre-commit hooks enforced
- **Branch protection**: Main branch requires PRs with passing CI
- **Automation**: Dependabot for dependencies, PR-based semantic releases with binaries

---

## Features & Functionality

### Calculator Operations
- **Basic arithmetic**: add, subtract, multiply, divide (with zero-division handling)
- **Average function** (PR #10): Variadic `average(*numbers)` function
  - CLI aliases: `average`, `avg`
  - Handles 1+ arguments, returns float
  - Example: `run-calc avg 1 2 3 4 5` → `3.0`

### CLI Interface
- **Console script**: `run-calc` installed via entry point
- **Operations**: Supports both binary (2 args) and variadic (1+ args) operations
- **Aliases**: `mul` for multiply, `div` for divide, `avg` for average
- **Help flag** (PR #12): `--help` and `-h` display usage information
- **Error handling**: Proper exit codes (0=success, 1=operation error, 2=usage error)
- **Input parsing**: Supports integers, floats, and scientific notation (e.g., `1e2`)

**Usage examples**:
```bash
run-calc add 2 3          # → 5
run-calc mul 4 5          # → 20
run-calc average 10 20 30 # → 20.0
run-calc --help           # Display usage
```

---

## Development Setup & Tools

### Linting & Formatting
- **Tool**: ruff (unified linter + formatter)
- **Configuration**: `pyproject.toml`
  - Line length: 100 characters
  - Target: Python 3.10+
  - Rules: E, W, F, I, N, UP, B, C4
  - Modern syntax: `int | float` instead of `Union[int, float]`
- **Pre-commit hooks**: `.pre-commit-config.yaml`
  - `ruff check --fix` (auto-fix linting issues)
  - `ruff-format` (auto-format code)
  - Standard hooks: trailing-whitespace, end-of-file, yaml check
- **Makefile targets**: `make lint`, `make format`, `make check`

### Testing
- **Framework**: pytest with pytest-cov
- **Coverage**: 100% requirement maintained (25/25 tests)
- **Structure**: Tests mirror `src/` structure in `tests/`
- **Test types**:
  - Unit tests: `test_calculator.py` (11 tests)
  - CLI tests: `test_cli.py` (14 tests)
- **Best practices**:
  - Testable CLI via `main(exit_process=False)`
  - Parametrized tests for multiple scenarios
  - Both success and failure cases covered

### Packaging
- **Format**: PEP 621 via `pyproject.toml`
- **Entry point**: Console script `run-calc` → `simple_calc.cli:main`
- **Dependencies**:
  - Runtime: none (pure Python)
  - Test: `pytest>=7.0`
  - Dev: `ruff>=0.7.0`, `pre-commit>=3.0.0`
- **Installation**: `pip install -e '.[dev,test]'`

### Quick Start Commands
```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev,test]'
pre-commit install

# Development
make lint      # Auto-fix linting issues
make format    # Format code
make test      # Run tests
pytest --cov   # Run with coverage

# CLI usage
run-calc add 2 3
run-calc --help
```

---

## CI/CD & Automation

### GitHub Actions Workflows

**CI Workflow** (`.github/workflows/ci.yml`):
- **Triggers**: Push/PR to main
- **Jobs**:
  - Lint (Python 3.12): ruff check, ruff format --check
  - Test (Python 3.10, 3.11, 3.12): pytest with coverage
  - Codecov upload: `fail_ci_if_error: false` (PR #11 - handles fork PRs gracefully)
- **Status**: Required checks for PR merges

**Semantic Release Workflow** (`.github/workflows/semantic-release.yml`):
- **Triggers**: Push to main
- **Strategy**: PR-based releases (respects branch protection)
- **Jobs**:
  - `release`: Determines next version, creates release PR with updated CHANGELOG and version
  - `finalize-release`: Runs when release PR is merged, creates tag and GitHub release
  - `build-binary`: Builds macOS arm64 binary after release finalization
- **Workflow pattern**:
  1. Push to main → semantic-release determines if release needed
  2. If needed, creates PR with version bump and CHANGELOG
  3. Review and merge release PR → triggers finalization
  4. Finalization creates tag, GitHub release, and builds binary
- **Branch protection compliance**: Uses PRs instead of direct pushes to main
- **Rationale**: Original workflow pushed directly to main, violating branch protection rules. New workflow creates reviewable release PRs while maintaining full automation.
- **Reference**: PR #16, commit 3208e74

**Build Workflow** (`.github/workflows/build-macos.yml`):
- **Triggers**: Push to main only (optimized in PR #7)
- **Platform**: macOS arm64 (Apple Silicon)
- **Tool**: PyInstaller for single-file binary
- **Artifacts**: Binary uploaded to GitHub releases
- **Versioning**: `v{version}-{timestamp}` with auto-generated notes

### Dependency Management
- **Tool**: Dependabot (`.github/dependabot.yml`)
- **Schedule**: Weekly (Mondays)
- **Ecosystems**:
  - pip (`pyproject.toml`): max 10 PRs, labels: `dependencies`, `python`
  - github-actions: max 5 PRs, labels: `dependencies`, `github-actions`
- **Format**: Conventional commits (`chore(deps):`)
- **Results**: 4 initial PRs merged (actions/checkout, codecov-action, setup-python, upload-artifact)

### Branch Protection
- **Protected branch**: main
- **Requirements**:
  - PRs required (no direct pushes)
  - Required status checks: lint, test (3.10), test (3.11), test (3.12)
  - No force pushes, no deletions
- **Configuration**: Via GitHub API

---

## Changelog

### 2025-12-01

**PR #16: Semantic Release Branch Protection Fix**
- Modified semantic-release workflow to work with branch protection rules
- **Change**: Switched from direct push to PR-based release workflow
- **Workflow pattern**:
  - `release` job: Determines next version → creates release PR with CHANGELOG and version bump
  - `finalize-release` job: Runs when release PR is merged → creates tag and GitHub release
  - `build-binary` job: Builds macOS arm64 binary after release finalization
- **Rationale**: Original workflow violated branch protection by pushing directly to main. New workflow creates reviewable release PRs while maintaining automation.
- **Benefits**:
  - Respects branch protection rules (no direct pushes to main)
  - Maintains full automation (no manual steps required)
  - Allows review of release changes before finalization
  - Properly sequences tag creation, release, and binary build
- **Reference**: Commit 3208e74

### 2025-11-30

**PR #12: CLI Help Flag**
- Added `--help` and `-h` flags to CLI
- Returns exit code 0 (vs. exit code 2 for missing args)
- 2 new tests, 25 total tests, 100% coverage maintained

**PR #11: Codecov Error Handling**
- Added `fail_ci_if_error: false` to Codecov upload step
- Prevents CI failures when token unavailable (fork PRs)
- Silences "Context access might be invalid" warnings

**PR #10: Average Function**
- Added `average(*numbers)` variadic function
- CLI integration with `avg` alias
- Refactored CLI to support both binary and variadic operations
- 11 new tests (6 calculator + 5 CLI)
- Coverage: 12 → 23 tests, maintained 100%

**PR #8: GitHub Copilot Instructions**
- Created `.github/copilot-instructions.md`
- Comprehensive guide: code style, testing, git workflow, CI/CD
- Mandatory documentation requirements for PRs

**PR #7: Binary Build Optimization**
- Removed pull_request trigger from build workflow
- Binaries only built on push to main
- Faster PR feedback, cleaner releases

**PR #5: README Badges**
- Added badges: Python 3.10+, Code style: ruff, License: MIT, Release

**Linting & Formatting** (commit: dea93b3):
- Integrated ruff (unified linter + formatter)
- Added pre-commit hooks
- Makefile targets: lint, format, check
- CI lint job added
- Modernized code: `Union` → `|`, exception chaining

**Dependabot Configuration** (commit: 3b67308):
- Created `.github/dependabot.yml`
- Weekly pip + github-actions monitoring
- Created labels: dependencies, github-actions, python
- 4 PRs merged automatically

**Branch Protection**:
- Configured via GitHub API
- Required PRs with passing CI checks

### 2025-11-27

**Binary Distribution**:
- PyInstaller-based macOS arm64 builds
- Automated releases with versioning
- Binary downloads in README

**CLI Refactor**:
- Testable design: `main(exit_process=False)`
- Comprehensive test suite (12 tests)
- Coverage: 30% → 100%

**CI & Coverage**:
- GitHub Actions with Python 3.10, 3.11, 3.12 matrix
- Codecov integration

### Initial Development

**Project Scaffolding**:
- Created package structure (`src/simple_calc/`)
- Basic arithmetic functions with type hints
- pytest test suite
- PEP 621 packaging (`pyproject.toml`)
- Console script entry point

**Repository Setup**:
- GitHub repository created
- Fixed nested folder structure (moved to root)
- Cleaned up artifacts (.DS_Store, egg-info)

---

## Key Decisions & Patterns

### Code Quality
- **Modern Python**: Target 3.10+ for union syntax (`|`), modern type hints
- **100% Coverage**: Strict requirement, use `# pragma: no cover` sparingly
- **Exception Chaining**: Always use `raise ... from err` for context
- **Type Hints**: All function signatures typed

### Testing Strategy
- **Testable CLI**: `main()` accepts `exit_process` parameter to avoid `sys.exit()` in tests
- **Exit Codes**: 0=success, 1=operation error, 2=usage error
- **Comprehensive Coverage**: Both success and failure paths tested

### CI/CD Philosophy
- **Branch Protection**: All changes via PRs with required checks
- **Conventional Commits**: Structured commit messages for automation
- **Dependabot**: Weekly automated updates with auto-merge capability
- **Binary Builds**: Only on main to save resources and keep releases clean
- **Graceful Failures**: CI continues even if optional steps (Codecov) fail

### Documentation
- **Copilot.md**: Development log, decisions, and changelog
- **README.md**: User-facing docs, installation, usage
- **ROADMAP.md**: Future planning (gitignored)
- **Copilot Instructions**: `.github/copilot-instructions.md` for AI assistance

---

## File Structure

```
.
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # Lint + test CI
│   │   └── build-macos.yml     # Binary builds
│   ├── dependabot.yml          # Automated dependency updates
│   └── copilot-instructions.md # GitHub Copilot guidance
├── src/simple_calc/
│   ├── __init__.py             # Package exports
│   ├── calculator.py           # Core arithmetic functions
│   └── cli.py                  # CLI interface
├── tests/
│   ├── test_calculator.py      # Unit tests (11 tests)
│   └── test_cli.py             # CLI tests (14 tests)
├── bin/
│   └── run_calc.py             # Standalone wrapper script
├── .pre-commit-config.yaml     # Pre-commit hooks
├── pyproject.toml              # Project metadata & config
├── Makefile                    # Common dev tasks
├── README.md                   # User documentation
├── Copilot.md                  # This file (development log)
└── ROADMAP.md                  # Future plans (gitignored)
```

---

## Resources & References

- **Repository**: https://github.com/snakeland/simple_python_project
- **Python Version**: 3.10+ required
- **License**: MIT
- **Tooling**: ruff, pytest, PyInstaller, pre-commit
- **CI/CD**: GitHub Actions, Dependabot, Codecov

For future improvements and planned features, see `ROADMAP.md`.
