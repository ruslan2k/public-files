-module(hello_erlang_app).
-behaviour(application).

-export([start/2]).
-export([stop/1]).

-include("user_record.hrl").

start(_Type, _Args) ->
    %% Start mnesia database in current nide
    %% which is nonode@nohost
    mnesia:create_schema([node()]),
    mnesia:start(),

    mnesia:create_table(user, []),

    Dispatch = cowboy_router:compile([
        %% {HostMatch, list({PathMatch, Handler, Opts})}
        {'_', [{"/", hello_handler, []}]}
    ]),
    %% Name, NbAcceptors, TransOpts, ProtoOpts
    {ok, _} = cowboy:start_http(my_http_listener, 100,
                [{port, 8080}],
                [{env, [{dispatch, Dispatch}]}]
    ),
	hello_erlang_sup:start_link().

stop(_State) ->
	ok.
