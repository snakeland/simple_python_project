PY=python
VENV=.venv

.PHONY: venv install test cli clean

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

clean:
	@echo "Cleaning common artifacts"
	rm -rf $(VENV) build dist *.egg-info .pytest_cache
