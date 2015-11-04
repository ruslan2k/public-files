-module(store).
-compile([export_all]).

get_master() ->
    ok.

start_master() ->
    register(store, spawn(store, server, [[]])).

%%  start_slave(Master) ->
%%     spawn(

server(Nodes) ->
    receive
        {From, slave_connect, Name} ->
            io:format("Nodes: ~p~n", [Nodes]),
            io:format("From <~p>, Name <~p>~n", [From, Name]),
            New_Nodes = slave_connect(From, Name, Nodes),
            server(New_Nodes)
    end.

slave_connect(From, Name, Nodes) ->
    case lists:keymember(Name, 2, Nodes) of
        true ->
            From ! {master, stop, node_exists},
            Nodes;
        false ->
            From ! {master, logged_on},
            [{From, Name} | Nodes]
    end.

    
% EOF
