-module(test).

-export([fib/1]).
-export([bump/1]).

%sum(0) -> 0.

fib(N) when N > 0 -> N + fib(N-1);
fib(N) when N == 0 -> N.

bump([]) -> [];
bump([Head | Tail]) -> [Head + 1 | bump(Tail)].


