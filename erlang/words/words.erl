-module(words_app).

-export([init/0]).
-export([start/0]).
-export([readlines/1]).
-export([readlines_v2/1]).
-export([get_all_lines/1]).


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


readlines(FileName) ->
    {ok, Device} = file:open(FileName, [read]),
    try get_all_lines(Device)
        after file:close(Device)
    end.


readlines_v2(FileName) ->
    {ok, Data} = file:read_file(FileName),
    binary:split(Data, [<<"\n">>], [global]).


get_all_lines(Device) ->
    case io:get_line(Device, "") of
        eof -> [];
        Line -> Line ++ get_all_lines(Device)
    end.



