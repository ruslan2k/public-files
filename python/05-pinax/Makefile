APP_NAME=mysite
GECKO_URL=https://github.com/mozilla/geckodriver/releases

#info: ${APP_NAME}
#	echo 'http://pinaxproject.com/pinax/pinax_starter_projects/#getting-started'

run: ${APP_NAME}
	cd ${APP_NAME} && ../env/bin/python ./manage.py runserver 0.0.0.0:8000

${APP_NAME}:
	cd ${APP_NAME} && chmod +x manage.py
	cd ${APP_NAME} && ../env/bin/python ./manage.py loaddata sites

new-install: ./env/bin/pinax
./env/bin/pinax: env
	./env/bin/pip install pinax-cli

env:
	virtualenv -p python3 env
	./env/bin/pip install -r ${APP_NAME}/requirements.txt

makemigrations:
	#./env/bin/python ${APP_NAME}/manage.py makemigrations resources
	./env/bin/python ${APP_NAME}/manage.py makemigrations
	./env/bin/python ${APP_NAME}/manage.py migrate
	./env/bin/python ${APP_NAME}/manage.py showmigrations  --list
	cd ${APP_NAME} && ../env/bin/python ./manage.py migrate

geckodriver:
	geckodriver -h >/dev/null|| echo geckodriver not installed download ${GECKO_URL}
	@echo geckodriver installed

tests: geckodriver test_django test_selenium
test_django:
	cd ${APP_NAME} && ./manage.py test resources.tests.UserTest
test_selenium:
	cd ${APP_NAME} && ./manage.py test resources.tests.MySeleniumTests.test_login
