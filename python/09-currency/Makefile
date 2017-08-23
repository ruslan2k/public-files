PYTHON:=venv/bin/python

run: venv
	$(PYTHON) app.py

venv:
	virtualenv -p python3 $@
	$@/bin/pip install -r requirements.txt

