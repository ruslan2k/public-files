build:
	docker build -t nginx-stream .

run:
	#docker run --rm -i -t nginx-stream  bash
	docker  run --rm -i -t -v `pwd`:/opt/build  nginx-stream  bash

daemon:
	docker  run  -d -t -v `pwd`:/opt/build  nginx-stream  bash
