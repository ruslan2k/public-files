runserver: venv
	$(MAKE) migrate
	$(MAKE) loaddata
	venv/bin/python ./manage.py runserver

venv:
	virtualenv -p python3 venv
	venv/bin/pip install -r requirements.txt

migrate:
	venv/bin/python ./manage.py migrate

loaddata:
	venv/bin/python ./manage.py loaddata sites

push:
	git push heroku master

