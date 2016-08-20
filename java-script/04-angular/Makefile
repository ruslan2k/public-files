PORT:=8008

express:
	DEBUG=express:* node express.js

node:
	node node_modules/http-server/bin/http-server -a localhost -p ${PORT}

default:
	php -S 0.0.0.0:8008

install:
	npm install
