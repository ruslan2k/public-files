-module(words).

-export([init/0]).
-export([start/0]).

start() ->
    register(words, spawn(?MODULE, init, [])).

init() ->
    Words = get_words(),
    loop(Words).

get_words() -> ["a", "b", "c"].

loop(Words) ->
    receive
        Any ->
            io:format("Received:~p~n", [Any]),
            loop(Words)
    end.


