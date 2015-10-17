-module(echo).
-compile(export_all).


start() ->
    case whereis(echo) of
        undefined ->
            Pid = spawn(?MODULE, loop, []),
            register(echo, Pid);
        _ ->
            {error, alerady_started}
    end.


loop() ->
    receive
        stop ->
            exit(normal);
        {print, Msg} ->
            io:format("~w~n", [Msg])
    end,
    loop().


stop() ->
    echo ! stop.


print(Msg) ->
    echo ! {print, Msg}.    
