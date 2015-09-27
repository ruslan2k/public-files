#!/usr/bin/env escript
%% -*- erlang -*-
main([WordsFile, Word]) ->
    %[WordsFile, Word] = Args,
    %io:format("Args: ~p~n", [Args]),
    io:format("Word: ~p~n", [Word]),
    io:format("WordsFile: ~p~n", [WordsFile]),
    Words = words_app:readlines_v2(WordsFile),
    %io:format("Words: ~p~n", [Words]),
    case words_app:find_single_word(Word, Words) of
        true ->
            io:format("Found ~p~n", [Word]);
        false ->
            io:format("Not Found ~p~n", [Word])
    end        
    ;

main(_) ->
    usage().


usage() ->
    io:format("usage: words\n"),
    halt(1).


