# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Help flag support (`--help` and `-h`) for CLI
- Documentation reorganization for better navigation

## [0.2.0] - 2025-11-30

### Added
- Average function with variadic arguments (`average(*numbers)`)
- CLI alias `avg` for average operation
- GitHub Copilot custom instructions (`.github/copilot-instructions.md`)
- README badges (Python version, ruff, license, release)

### Changed
- CLI refactored to support both binary and variadic operations
- Binary operations require exactly 2 arguments
- Variadic operations accept 1+ arguments
- Improved error handling and usage messages

### Fixed
- Codecov CI failures when token unavailable (added `fail_ci_if_error: false`)

### CI/CD
- Optimized binary builds to run only on push to main (not PRs)
- Configured branch protection with required status checks
- Added ruff linting to CI workflow
- Dependabot configured for automated dependency updates

### Documentation
- Updated Copilot.md with comprehensive development log
- Added documentation requirements to Copilot instructions

## [0.1.0] - 2025-11-27

### Added
- Initial project release
- Basic arithmetic operations: add, subtract, multiply, divide
- CLI interface with console script `run-calc`
- Operation aliases: `mul` for multiply, `div` for divide
- Comprehensive test suite with pytest (100% coverage)
- CI/CD with GitHub Actions (Python 3.10, 3.11, 3.12)
- Codecov integration for coverage reporting
- macOS arm64 binary builds with PyInstaller
- Automated GitHub releases with binaries
- PEP 621 packaging with `pyproject.toml`

### Developer Experience
- Pre-commit hooks for code quality
- ruff linting and formatting
- Makefile shortcuts (`make lint`, `make format`, `make test`)

[Unreleased]: https://github.com/snakeland/simple_python_project/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/snakeland/simple_python_project/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/snakeland/simple_python_project/releases/tag/v0.1.0
