-module(ctemplate).
-compile(export_all).


start() ->
	spawn(ctemplate, loop, [[]]).


rpc(Pid, Request) ->
	Pid ! {self(), Request},
	receive
		{Pid, Response} ->
			Response
	end.


loop(X) ->
	receive
        {From, Request} ->
            io:format("From:[~p] Received:[~p]~n", [From, Request]),
			loop(X);
		Any ->
			io:format("Received:~p~n", [Any]),
			loop(X)
	end.


hello() ->
    {_, {Module, Function, Arity}} = process_info(self(), current_function),
    io:format("Module: ~p, Function: ~p, Arity: ~p~n",[Module, Function, Arity]).


