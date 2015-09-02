messenger.beam :
	erlc -W messenger.erl

1 :
	screen -AdmS myshell -t tab0 ping ya.ru
	screen -S myshell -X screen -t tab1 ping tut.by
	screen -S myshell -X screen -t tab2 ping www.google.com

tmux :
	tmux new -d -s messenger 
	tmux split-window -v 'ping tut.by'
	tmux attach-session -t messenger


