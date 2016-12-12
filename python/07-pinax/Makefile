runserver: migrate env
	env/bin/python ./manage.py runserver

env:
	virtualenv -p python3 env
	env/bin/pip install -r requirements.txt

migrate: dev.db
dev.db:
	env/bin/python ./manage.py migrate
