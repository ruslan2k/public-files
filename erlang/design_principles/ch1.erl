%% http://www.erlang.org/doc/design_principles/des_princ.html

-module(ch1).
-export([start/0]).
-export([alloc/0]).
-export([free/1]).
-export([init/0]).

start() ->
    ch1 ! {self(), alloc),
    receive
        {ch1, Res} ->
            Res
    end.

alloc() ->
    ch1 ! {self(), alloc},
    receive
        {ch1, Res} ->
            Res
    end.

free(Ch) ->
    ch1 ! {free, Ch},
    ok.

init() ->
    register(ch1, self()),
    Chs = channels(),
    loop(Chs).

loop(Chs) ->
    receive
        {From, alloc} ->
            {Ch, Chs2} = alloc(Chs),
            From ! {ch1, Ch},
            loop(Chs2);
        {free, Ch} ->
            Chs2 = free(Ch, Chs),
            loop(Chs2)
    end.

%%

channels() ->
    {_Allocated = [], _Fress = lists:seq(1, 10)}.

alloc({Allocated, [H|T] = _Free}) ->
    {H, {[H|Allocated], T}}.

free(Ch, {Alloc, Free} = Channels) ->
    case lists:member(Ch, Alloc) of
        true ->
            {lists:delete(Ch, Alloc), [Ch|Free]};
        false ->
            Channels
    end.
