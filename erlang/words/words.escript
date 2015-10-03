#!/usr/bin/env escript
%% -*- erlang -*-

main([WordsFile, Word]) ->
    %io:format("Word: ~p~n", [Word]),
    %io:format("WordsFile: ~p~n", [WordsFile]),
    Words = readlines(WordsFile),
    Annagrams = perms(Word),
    Result = lists:filter(fun(X) -> find_single_word(X, Annagrams) end, Words),
    io:format("Result: ~p~n", [Result]),
    loop("dfdfd")
    ;

main(_) ->
    usage().


usage() ->
    io:format("usage:\n\twords.escript path_to/words_file Word\n"),
    halt(1).

loop(Word) ->
    %% Find word:
    io:format("Word: [~p]~n", [Word]),
    Result = io:read("Word> "),
    {_, NewWord} = Result,
    loop(NewWord).


find_single_word(Word, List) ->
    lists:any(fun(X) -> compare_strings(X, Word) end, List).


compare_strings(S1, S2) ->
    string:to_lower(S1) == string:to_lower(binary_to_list(S2)).


readlines(FileName) ->
    {ok, Data} = file:read_file(FileName),
    binary:split(Data, [<<"\n">>], [global]).


perms([]) -> [[]];
perms(L) -> [[H|T] || H <- L, T <- perms(L--[H])].



