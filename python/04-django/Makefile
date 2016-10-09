run: venv
	./venv/bin/python manage.py runserver

venv:
	virtualenv -p python3 $@
	./venv/bin/pip install -r requirements.txt

shell:
	./venv/bin/python manage.py shell
