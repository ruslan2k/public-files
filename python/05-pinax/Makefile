APP_NAME:=mysite

info: ${APP_NAME}
	echo 'http://pinaxproject.com/pinax/pinax_starter_projects/#getting-started'

${APP_NAME}: env/bin/pinax
	./env/bin/pinax start account $@

env/bin/pinax: env
	./env/bin/pip install pinax-cli

env:
	virtualenv -p python3 env
