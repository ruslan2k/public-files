PIP := venv/bin/pip
PYTHON := venv/bin/python


test: venv
	$(PYTHON) test.py	

venv: requirements.txt
	virtualenv -p python3 $@
	$(PIP) install -r requirements.txt
