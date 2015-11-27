compile: store.beam

store.beam: store.erl
	erlc -W store.erl

clean:
	rm -vf *.beam

master: store.beam
	erl -name store -s store start_master

slave1: compile
	erl -name $@ -s store start_slave
