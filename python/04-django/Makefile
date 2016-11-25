run: venv
	./venv/bin/python manage.py runserver

venv:
	virtualenv -p python3 $@
	./venv/bin/pip install -r requirements.txt

shell:
	./venv/bin/python manage.py shell

migrate:
	./venv/bin/python manage.py makemigrations resources
	./venv/bin/python manage.py makemigrations polls
	./venv/bin/python manage.py migrate

createadmin:
	./venv/bin/python manage.py createsuperuser
