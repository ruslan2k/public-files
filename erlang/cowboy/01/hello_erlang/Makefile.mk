start :
	$(MAKE)
	./_rel/hello_erlang_release/bin/hello_erlang_release console

mnesia :
	cd src && erlc -W user.erl



