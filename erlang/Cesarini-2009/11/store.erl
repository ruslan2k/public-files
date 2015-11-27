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
            server(New_Nodes);
        {From, put, Key, Value} ->
            io:format("put key [~p] value [~p]~n", [Key, Value]),
            From ! {ok, put},
            server(Nodes);
        {From, get, Key} ->
            io:format("get key [~p] value [~p]~n", [Key, get(Key)]),
            From ! {get, get(Key)},
            server(Nodes)
    end.

slave_connect(From, Name, Nodes) ->
    case lists:keymember(Name, 2, Nodes) of
        true ->
            From ! {store, stop, node_exists},
            Nodes;
        false ->
            From ! {store, logged_on},
            [{From, Name} | Nodes]
    end.


start_slave() ->
    [Name | _] = re:split(atom_to_list(node()), "@"),
    start_slave(Name).

start_slave(Name) ->
    case whereis(store_slave) of
        undefined ->
            register(store_slave,
                spawn(store, slave, [get_master(), Name]));
        _ -> slready_logged_on
    end.

slave(Master, Name) ->
    io:format("Slave name <~p>~n", [Name]),
    Master ! {self(), slave_connect, Name},
    await_result(),
    slave(Master).

slave(Master) ->
    io:format("Master: <~p>~n", [Master]),
    receive
        {put, Key, Value} ->
            io:format("Slave put~n"),
            put(Key, Value),
            slave(Master);
        {get, From, Key} ->
            io:format("Slave get~n"),
            Value = get(Key),
            From ! {Key, Value},
            slave(Master)
    end.

await_result() ->
    receive
        {store, stop, Why} ->
            io:format("~p~n", [Why]),
            exit(normal);
        {store, What} ->
            io:format("What <~p>~n", [What])
    end.

put_data(Key, Value) ->
    get_master() ! {self(), put, Key, Value},
    receive
        {ok, put} -> {ok, put}
    end.


get_data(Key) ->
    get_master() ! {self(), get, Key},
    receive
        {get, Value} -> Value
    end.


%% EOF
