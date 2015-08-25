%%% http://stackoverflow.com/questions/146622/sieve-of-eratosthenes-in-erlang

-module(primes).
-export([sieve/1]).

sieve([]) ->
    [];
sieve([H|T]) ->
    List = lists:filter(fun(N) -> N rem H /= 0 end, T),
    [H|sieve(List)];
sieve(N) ->
    sieve(lists:seq(2,N)).


