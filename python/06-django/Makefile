env:
	virtualenv -p python3 env
	env/bin/pip install -r requirements.txt
	env/bin/python -m django --version

mig:
	env/bin/python manage.py makemigrations test2
	env/bin/python manage.py migrate

dump:
	sqlite3 db.sqlite3 .dump
