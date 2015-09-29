#!/usr/bin/env escript
%% -*- erlang -*-

main([WordsFile, Word]) ->
    %io:format("Word: ~p~n", [Word]),
    %io:format("WordsFile: ~p~n", [WordsFile]),
    Words = words_app:readlines_v2(WordsFile),
    Annagrams = words_app:perms(Word),
    %io:format("Annagrams: ~p~n", [Annagrams]),
    case words_app:find_single_word(Word, Words) of
        true ->
            io:format("Found ~p~n", [Word]);
        false ->
            io:format("Not Found ~p~n", [Word])
    end,
    Result = lists:filter(fun(X) -> words_app:find_single_word(X, Words) end, Annagrams),
    io:format("Result: ~p~n", [Result])
    ;

main(_) ->
    usage().


usage() ->
    io:format("usage:\n\twords.escript path_to/words_file Word\n"),
    halt(1).


find_single_word(Word, List) ->
    BinWord = list_to_binary(Word),
    lists:any(fun(X) -> compare_strings_v2(X, BinWord) end, List).




