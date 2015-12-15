run: myserver.beam
	erl -s myserver start_link
myserver.beam: myserver.erl
	erlc -W $<
