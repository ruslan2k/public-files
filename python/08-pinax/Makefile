default:
	$(MAKE) migrate
	$(MAKE) loaddata

venv:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

migrate:
	./manage.py migrate

loaddata:
	./manage.py loaddata sites

runserver: default
	./manage.py runserver

