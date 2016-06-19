3: hello-3
	./$<
hello-3: hello-3.c
	gcc -std=c99 -o $@ $< -lncurses

2: hello-2
	./$<

hello-2: hello-2.c
	gcc -o $@ $< -lncurses

hello-1: hello-1.c
	gcc -o $@ $< -lncurses

test: test.cpp
	g++ -Wall -o $@ $<

clean:
	rm -f test hello-1 hello-2

d: debug
	./$<
debug: debug.c
	gcc -o $@ $< -lncurses
