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
