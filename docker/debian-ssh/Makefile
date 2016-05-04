NAME := debian-ssh

default:
	docker run -dt --name debian \
		-p 8001:80 -p 13000:12000 -p 2202:22 ${NAME}
	sleep 2
	docker ps

build:
	docker build -t ${NAME} .
