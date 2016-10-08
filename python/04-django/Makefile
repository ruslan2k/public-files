run: venv
	./venv/bin/python mysite/manage.py runserver

venv:
	virtualenv -p python3 $@
	./venv/bin/pip install -r requirements.txt
