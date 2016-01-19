all: ch_app.beam ch_sup.beam ch3.beam

ch_sup.beam: ch_sup.erl
	erlc -W $<
ch_app.beam: ch_app.erl
	erlc -W $<
ch3.beam: ch3.erl
	erlc -W $<

clean:
	rm -v *.beam
	
