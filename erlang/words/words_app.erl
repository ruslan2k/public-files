-module(words_app).

-export([init/0]).
-export([start/0]).
-export([readlines/1]).
-export([readlines_v2/1]).
-export([get_all_lines/1]).
-export([find_single_word/2]).


start() ->
    register(words, spawn(?MODULE, init, [])).


init() ->
    Words = get_words(),
    loop(Words).


find_words_in_list(Words, List) -> true.


find_single_word(Word, List) ->
    lists:any(fun(X) -> compare_strings(X, Word) end, List).


compare_strings(S1, S2) ->
    io:format("~p == ~p~n", [S1, S2]),
    S1 == S2.


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



