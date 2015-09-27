#!/usr/bin/env escript
%% -*- erlang -*-
main([WordsFile, Word]) ->
    %[WordsFile, Word] = Args,
    %io:format("Args: ~p~n", [Args]),
    io:format("Word: ~p~n", [Word]),
    io:format("WordsFile: ~p~n", [WordsFile]),
    Words = words_app:readlines_v2(WordsFile),
    %Annagrams = words_app:perms(string:to_lower(Word)),
    Annagrams = words_app:perms(Word),
    %%io:format("Words: ~p~n", [Words]),
    io:format("Annagrams: ~p~n", [Annagrams]),
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
    io:format("usage: words\n"),
    halt(1).


