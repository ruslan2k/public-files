SERVER=ru0


#e :
#	escript  war.escript


war.beam : war.erl
	erlc -W $<


defult :
	scp war.erl ${SERVER}:git/public-files/erlang/war/
	ssh ${SERVER} 'cd ~/git/public-files/erlang/war && erlc -W war.erl'


clean :
	rm -f *.beam


