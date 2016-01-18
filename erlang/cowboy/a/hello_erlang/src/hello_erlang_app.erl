-module(hello_erlang_app).
-behaviour(application).

-export([start/2]).
-export([stop/1]).

start(_Type, _Args) ->
    Dispatch = cowboy_router:compile([
        {'_', [
            {"/", hello_handler, []},
            {"/:model", model_handler, []}
        ]}
    ]),
    cowboy:start_http(my_http_listener, 5, [{port, 8080}],
        [{env, [{dispatch, Dispatch}]}]
    ),
    hello_erlang_sup:start_link().

stop(_State) ->
	ok.