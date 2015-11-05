-module(store).
-compile([export_all]).

get_master() ->
    {store, 'store@ru2.aptinfo.net'}.

start_master() ->
    register(store, spawn(store, server, [[]])).

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


start_slave() ->
    [Name | _] = re:split(atom_to_list(node()), "@"),
    start_slave(Name);
start_slave(Name) ->
    slave(get_master(), Name).

slave(Master, Name) ->
    %% Master ! {self(), connect, Name}  
    io:format("", [{self(), connect, Name}]),
    {store, Master} ! {self(), commect, Name},
    await_result(),
    slave(Master).

await_result() ->
    receive
        {store, stop, Why} ->
            io:format("~p~n", [Why]),
            exit(normal);
        {store, What} ->
            io:format("~p~n", [What])
    end.
 
%% EOF