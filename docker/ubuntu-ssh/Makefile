default:
	docker run -dt --name ubuntu \
		-p 8001:80 -p 13000:12000 -p 2201:22 ubuntu-ssh
	docker ps
	echo ssh localhost -p2201 -lroot

build:
	docker build -t ubuntu-ssh .
