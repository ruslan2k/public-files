build:
	docker build -t nginx-stream .

run:
	#docker  run  -i --rm -t nginx-stream  bash
	docker  run --rm  -t -v `pwd`:/opt/build  nginx-stream  bash

daemon:
	docker  run  -d -t -v `pwd`:/opt/build  nginx-stream  bash
