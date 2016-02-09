start:
	@erl -noshell -pa './deps/bitcask/ebin' -pa './ebin' -s bertie start

all:
	test -d deps || rebar get-deps
	rebar compile
	$(MAKE) start

