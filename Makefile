PY=python
VENV=.venv

.PHONY: venv install test cli lint format check clean

venv:
	@echo "Creating virtualenv: $(VENV)"
	$(PY) -m venv $(VENV)
	@echo "To activate: source $(VENV)/bin/activate"

install: venv
	@echo "Installing project in editable mode with test extras"
	. $(VENV)/bin/activate && $(PY) -m pip install --upgrade pip && $(PY) -m pip install -e '.[test]'

test:
	@echo "Running test suite in venv"
	. $(VENV)/bin/activate && pytest -q

cli:
	@echo "Run CLI via venv (or install -e . to create run-calc on PATH)"
	. $(VENV)/bin/activate && run-calc $(ARGS)

lint:
	@echo "Running ruff linter with auto-fix"
	. $(VENV)/bin/activate && ruff check --fix src tests bin

format:
	@echo "Running ruff formatter"
	. $(VENV)/bin/activate && ruff format src tests bin

check:
	@echo "Checking code with ruff (no auto-fix)"
	. $(VENV)/bin/activate && ruff check --diff src tests bin

clean:
	@echo "Cleaning common artifacts"
	rm -rf $(VENV) build dist *.egg-info .pytest_cache

preview-release:
	@echo "=== Release Preview ==="
	@echo ""
	@CURRENT_VERSION=$$(grep '^version = ' pyproject.toml | cut -d '"' -f 2); \
	echo "Current version: $$CURRENT_VERSION"; \
	echo ""; \
	LAST_TAG=$$(git describe --tags --abbrev=0 2>/dev/null); \
	echo "Last release tag: $$LAST_TAG"; \
	echo ""; \
	LAST_MERGE=$$(git log --oneline --grep="^chore: merge release" -1 --format="%H" 2>/dev/null); \
	if [ -z "$$LAST_MERGE" ]; then \
		COMMIT_RANGE="$$LAST_TAG..HEAD"; \
	else \
		COMMIT_RANGE="$$LAST_MERGE..HEAD"; \
	fi; \
	echo "=== Commits since last release ==="; \
	git log $$COMMIT_RANGE --oneline; \
	echo ""; \
	echo "=== Commit Type Analysis ==="; \
	echo ""; \
	FEAT_COUNT=$$(git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* feat' | wc -l | tr -d ' '); \
	FIX_COUNT=$$(git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* fix' | wc -l | tr -d ' '); \
	DOCS_COUNT=$$(git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* docs' | wc -l | tr -d ' '); \
	CI_COUNT=$$(git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* ci' | wc -l | tr -d ' '); \
	echo "Features (feat:): $$FEAT_COUNT"; \
	if [ "$$FEAT_COUNT" -gt 0 ]; then \
		git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* feat' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "Fixes (fix:): $$FIX_COUNT"; \
	if [ "$$FIX_COUNT" -gt 0 ]; then \
		git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* fix' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "Docs (docs:): $$DOCS_COUNT"; \
	if [ "$$DOCS_COUNT" -gt 0 ]; then \
		git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* docs' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "CI (ci:): $$CI_COUNT"; \
	if [ "$$CI_COUNT" -gt 0 ]; then \
		git log $$COMMIT_RANGE --oneline | grep '^[a-f0-9]* ci' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "=== Version Recommendation ==="; \
	MAJOR=$$(echo $$CURRENT_VERSION | cut -d. -f1); \
	MINOR=$$(echo $$CURRENT_VERSION | cut -d. -f2); \
	PATCH=$$(echo $$CURRENT_VERSION | cut -d. -f3); \
	if [ "$$FEAT_COUNT" -gt 0 ]; then \
		NEXT_VERSION="$$MAJOR.$$((MINOR + 1)).0"; \
		echo "Suggested bump: MINOR (new features)"; \
		echo "Next version: $$NEXT_VERSION"; \
	elif [ "$$FIX_COUNT" -gt 0 ]; then \
		NEXT_VERSION="$$MAJOR.$$MINOR.$$((PATCH + 1))"; \
		echo "Suggested bump: PATCH (bug fixes)"; \
		echo "Next version: $$NEXT_VERSION"; \
	else \
		echo "Suggested bump: NONE (no relevant commits)"; \
		echo "Next version: $$CURRENT_VERSION (no changes)"; \
	fi
