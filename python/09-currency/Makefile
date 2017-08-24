PYTHON:=venv/bin/python

run: venv
	$(PYTHON) app.py
	sqlite3 db.sq3 .dump

venv:
	virtualenv -p python3 $@
	$@/bin/pip install -r requirements.txt

