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
	@echo "=== Commits since last release ==="
	@LAST_TAG=$$(git describe --tags --abbrev=0 2>/dev/null); \
	git log $$LAST_TAG..HEAD --oneline; \
	echo ""; \
	echo "=== Commit Type Analysis ==="; \
	echo ""; \
	FEAT_COUNT=$$(git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* feat' | wc -l | tr -d ' '); \
	FIX_COUNT=$$(git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* fix' | wc -l | tr -d ' '); \
	DOCS_COUNT=$$(git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* docs' | wc -l | tr -d ' '); \
	CI_COUNT=$$(git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* ci' | wc -l | tr -d ' '); \
	echo "Features (feat:): $$FEAT_COUNT"; \
	if [ "$$FEAT_COUNT" -gt 0 ]; then \
		git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* feat' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "Fixes (fix:): $$FIX_COUNT"; \
	if [ "$$FIX_COUNT" -gt 0 ]; then \
		git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* fix' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "Docs (docs:): $$DOCS_COUNT"; \
	if [ "$$DOCS_COUNT" -gt 0 ]; then \
		git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* docs' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	echo "CI (ci:): $$CI_COUNT"; \
	if [ "$$CI_COUNT" -gt 0 ]; then \
		git log $$LAST_TAG..HEAD --oneline | grep '^[a-f0-9]* ci' | sed 's/^/  - /'; \
	fi; \
	echo ""; \
	if [ "$$FEAT_COUNT" -gt 0 ]; then \
		echo "→ Suggested release: MINOR (new features)"; \
	elif [ "$$FIX_COUNT" -gt 0 ]; then \
		echo "→ Suggested release: PATCH (bug fixes)"; \
	else \
		echo "→ Suggested release: PATCH (other changes)"; \
	fi
