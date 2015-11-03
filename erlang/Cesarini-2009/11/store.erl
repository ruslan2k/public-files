-module(store).
-compile([export_all]).

get_master() ->
    ok.

start_master() ->
    register(store, spawn(store, server, [[]])).

%%  start_slave(Master) ->
%%     spawn(

server(NodesList) ->
    receive
        {From, slave_connect, Name} ->
            io:format("From <~p>, Name <~p>~n", [From, Name]),
            New_NodesList = slave_connect(From, Name)
    end.

slave_connect(From, Name) ->
    [].
    


