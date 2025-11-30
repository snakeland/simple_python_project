# GitHub Copilot Instructions for simple_python_project

## Project Overview
This is a Python calculator package demonstrating modern Python development practices with full CI/CD automation. It's a learning/reference project showcasing professional workflows.

## Code Style & Quality

### Python Standards
- **Target Python**: 3.10+ (use modern syntax like `int | float` instead of `typing.Union`)
- **Line length**: 100 characters max
- **Quotes**: Double quotes for strings
- **Indentation**: 4 spaces (no tabs)

### Linting & Formatting
- **Tool**: ruff (unified linter and formatter)
- **Before committing**: Run `make lint` and `make format`
- **Pre-commit hooks**: Installed and active - they will auto-fix issues
- **Import ordering**: Alphabetical, grouped (stdlib → third-party → local)

### Type Hints
- Always use type hints for function signatures
- Use modern Python 3.10+ union syntax: `def func(x: int | float) -> str:`
- Avoid `typing.Union`, `typing.Optional` when possible

### Error Handling
- Use exception chaining: `raise NewError(...) from original_error`
- Add descriptive error messages
- Document exceptions in docstrings

## Testing

### Test Requirements
- **Framework**: pytest
- **Coverage**: Maintain 100% coverage (current standard)
- **Location**: Tests in `tests/` directory mirror `src/` structure
- **Naming**: `test_*.py` files, `test_*` functions

### Writing Tests
- Test both success and failure cases
- Use descriptive test names: `test_divide_by_zero_raises_value_error`
- Prefer parametrized tests for multiple similar cases
- Use `pytest` fixtures for common setup
- Add `# pragma: no cover` only for truly trivial/unreachable code

### Running Tests
```bash
make test          # Run all tests
pytest -v          # Verbose output
pytest --cov       # With coverage (requires pytest-cov: pip install pytest-cov)
```

## Git Workflow

### Branch Protection
- **Main branch is protected** - all changes via pull requests
- PRs require passing CI (lint + tests on Python 3.10, 3.11, 3.12)
- No direct pushes to `main`

### Branch Naming
- `feature/<description>` - New features
- `fix/<description>` - Bug fixes
- `docs/<description>` - Documentation only
- `ci/<description>` - CI/CD changes
- `chore/<description>` - Maintenance tasks

### Commit Messages
Follow conventional commits:
```
feat: add new calculator function
fix: correct divide-by-zero handling
docs: update README installation steps
ci: optimize binary build workflow
chore: update dependencies
test: add edge cases for multiply
```

### PR Workflow
```bash
git checkout -b feature/my-feature
# make changes
git commit -m "feat: description"
git push -u origin feature/my-feature
gh pr create --fill
# wait for CI, then merge
```

## Project Structure

```
.
├── src/simple_calc/       # Main package
│   ├── __init__.py       # Package exports
│   ├── calculator.py     # Core arithmetic functions
│   └── cli.py            # CLI interface
├── tests/                # Test suite
│   ├── test_calculator.py
│   └── test_cli.py
├── bin/run_calc.py       # Standalone wrapper
├── .github/
│   ├── workflows/        # CI/CD pipelines
│   └── dependabot.yml    # Dependency automation
├── pyproject.toml        # Project metadata & config
└── Makefile              # Common tasks
```

## Adding New Features

### Calculator Functions
1. Add function to `src/simple_calc/calculator.py` with type hints and docstring
2. Export from `src/simple_calc/__init__.py`
3. Add comprehensive tests to `tests/test_calculator.py`
4. If CLI-relevant, add to `cli.py` OPS dict

### CLI Commands
1. Add operation to `OPS` dict in `src/simple_calc/cli.py`
2. Add tests to `tests/test_cli.py` (success + error cases)
3. Update README usage examples

## CI/CD Pipelines

### Workflows
- **CI** (`ci.yml`): Runs on all PRs and pushes to main
  - Lint job (ruff check + format check)
  - Test job (matrix: Python 3.10, 3.11, 3.12)
  - Coverage upload to Codecov

- **Build** (`build-macos.yml`): Runs only on push to main
  - Builds macOS arm64 binary with PyInstaller
  - Creates GitHub release with versioned binary
  - Version format: `v{pyproject.version}-{timestamp}`

### Labels
- `dependencies` - Dependency updates
- `github-actions` - GitHub Actions updates
- `python` - Python code changes

## Dependencies

### Management
- **Dependabot**: Auto-creates PRs for updates weekly (Mondays)
- **pip**: Managed via `pyproject.toml` optional dependencies
  - `[test]`: pytest (add pytest-cov for coverage support)
  - `[dev]`: ruff, pre-commit

### Adding Dependencies
1. Add to appropriate section in `pyproject.toml`:
   ```toml
   dependencies = ["new-package>=1.0"]  # Runtime
   [project.optional-dependencies]
   test = ["pytest>=7.0", "new-test-tool"]
   dev = ["ruff>=0.7.0", "new-dev-tool"]
   ```
2. Install: `pip install -e '.[dev,test]'`
3. Update if needed: `pip install --upgrade new-package`

## Common Tasks

```bash
# Development setup
python -m venv .venv
source .venv/bin/activate  # or: . .venv/bin/activate
pip install -e '.[dev,test]'
pre-commit install

# Code quality
make lint      # Auto-fix linting issues
make format    # Format code
make check     # Check without fixing

# Testing
make test      # Run tests
pytest -v      # Verbose
pytest -k test_name  # Run specific test

# CLI usage
make cli ARGS="add 2 3"
run-calc multiply 4 5
python bin/run_calc.py div 10 2
```

## Documentation

### Updating Docs
- **README.md**: User-facing documentation, installation, usage
- **Copilot.md**: Project log, development decisions, and change history
- **ROADMAP.md**: Local planning (gitignored, not committed)

### Docstrings
Use Google-style docstrings:
```python
def divide(a: int | float, b: int | float) -> float:
    """Return a / b.

    Args:
        a: The numerator
        b: The denominator

    Returns:
        The quotient as a float

    Raises:
        ValueError: If b is zero
    """
```

## Special Considerations

### CLI Design
- `cli.py` has two functions for testability:
  - `run(argv)`: Core logic, returns exit code (0=success, 1=error, 2=usage)
  - `main(argv=None, exit_process=True)`: Wrapper that can skip `sys.exit()` for tests
- Always test CLI via `main(..., exit_process=False)` to avoid test process exit

### Coverage Pragmas
Use `# pragma: no cover` sparingly, only for:
- `if __name__ == "__main__":` guards
- Unreachable defensive code
- `sys.exit()` calls in testable wrappers

### Binary Distribution
- Built only on main branch merges
- macOS arm64 (Apple Silicon) only currently
- Unsigned binaries require `xattr -d com.apple.quarantine` on first run

## Questions or Issues?
See `Copilot.md` for project history and decisions, or `README.md` for user documentation.
