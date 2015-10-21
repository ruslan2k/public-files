-module(ring).
-compile(export_all).


start(Head, 1) ->
    io:format("Started. Number<~p>~n", [1]),
    spawn(?MODULE, loop, [Head, 1]);

start(Head, N) when N > 0 ->
    io:format("Start. Number<~p>~n", [N]),
    Child = start(Head, N-1),
    spawn(?MODULE, loop, [Child, N]).


start_head(N) when N > 0 ->
    Head = spawn(?MODULE, loop, [self(), 0]),
    Child = start(Head, N),
    Head ! {set_child, Child},
    Head.


loop(Child, N) ->
    receive
        exit ->
            io:format("exit Num<~p>~n", [N]),
            Child ! exit,
            exit(normal);
        {set_child, NewChild} ->
            io:format("NewChild<~p>~n", [NewChild]),
            loop(NewChild, N);
        {msg, 0} ->
            io:format("Me<~p> Num<~p>~n", [N, 0]),
            loop(Child, N);
        {msg, Num} ->
            io:format("Me<~p> Num<~p>~n", [N, Num]),
            Child ! {msg, Num-1},
            loop(Child, N);
        _Any ->
            io:format("~p~n", [_Any]),
            loop(Child, N)
    end.
