messenger.beam : messenger.erl
	erlc -W messenger.erl

1 :
	screen -AdmS myshell -t tab0 ping ya.ru
	screen -S myshell -X screen -t tab1 ping tut.by
	screen -S myshell -X screen -t tab2 ping www.google.com

tmux : messenger.beam
	tmux new -d -s messenger 'erl -sname messenger -s messenger start_server || sleep 300'
	sleep 3
	tmux split-window -v 'erl -sname peter -s messenger logon peter'
	tmux split-window -v 'erl -sname james -s messenger logon james'
	# messenger:message(peter, 'hello')
	tmux attach-session -t messenger

clean :
	rm -f *.beam

