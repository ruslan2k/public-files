SERVER=ru0

defult :
	scp war.erl ${SERVER}:git/public-files/erlang/war/
	ssh ${SERVER} 'cd ~/git/public-files/erlang/war && erlc -W war.erl'
