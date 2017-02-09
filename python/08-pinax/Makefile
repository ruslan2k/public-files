runserver: venv
	$(MAKE) migrate
	$(MAKE) loaddata
	./manage.py runserver

venv:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

migrate:
	./manage.py migrate

loaddata:
	./manage.py loaddata sites

