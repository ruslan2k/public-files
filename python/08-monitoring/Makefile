PIP := venv/bin/pip
PYTHON := venv/bin/python


test: venv
	$(PYTHON) test.py	
	sqlite3 monitoring.sq3 .dump

venv: requirements.txt
	virtualenv -p python3 $@
	$(PIP) install -r requirements.txt

cron:
	$(PYTHON) test.py	
