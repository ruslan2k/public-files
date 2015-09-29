#!/usr/bin/env escript
%% -*- erlang -*-

main([WordsFile, Word]) ->
    %io:format("Word: ~p~n", [Word]),
    %io:format("WordsFile: ~p~n", [WordsFile]),
    Words = words_app:readlines_v2(WordsFile),
    Annagrams = words_app:perms(Word),
    Result = lists:filter(fun(X) -> find_single_word(X, Annagrams) end, Words),
    io:format("Result: ~p~n", [Result])
    ;

main(_) ->
    usage().


usage() ->
    io:format("usage:\n\twords.escript path_to/words_file Word\n"),
    halt(1).


find_single_word(Word, List) ->
    lists:any(fun(X) -> compare_strings(X, Word) end, List).


compare_strings(S1, S2) ->
    string:to_lower(S1) == string:to_lower(binary_to_list(S2)).


