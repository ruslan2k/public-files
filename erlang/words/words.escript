#!/usr/bin/env escript
%% -*- erlang -*-

main([WordsFile]) ->
    Words = readlines(WordsFile),
    loop(Words)
    ;

main(_) ->
    usage().


usage() ->
    io:format("usage:\n\twords.escript path_to/words_file Word\n"),
    halt(1).


loop(Words) ->
    {ok, [Word]} = io:fread("New word: ", "~s"),
    Word == "quit" andalso halt(0),
    Annagrams = perms(Word),
    io:format("Annagrams: ~p~n", [Annagrams]),
    Result = lists:filter(fun(X) -> find_single_word(binary_to_list(X), Annagrams) end, Words),
    io:format("Result: ~p~n", [Result]),
    loop(Words).


find_single_word(Word, List) ->
    lists:any(fun(X) -> compare_strings(X, Word) end, List).


compare_strings(S1, S2) ->
    string:to_lower(S1) == string:to_lower(S2).


readlines(FileName) ->
    {ok, Data} = file:read_file(FileName),
    binary:split(Data, [<<"\n">>], [global]).


perms([]) -> [[]];
perms(L) -> [[H|T] || H <- L, T <- perms(L--[H])].


