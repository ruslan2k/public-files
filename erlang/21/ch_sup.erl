%% http://www.erlang.org/doc/design_principles/sup_princ.html

-module(ch_sup).
-behavior(supervisor).

-export([start_link/0]).
-export([init/1]).

start_link() ->
    supervisor:start_link(ch_sup, []).

init(_Args) ->
    SupFlags = #{strategy => one_for_one, intensity => 2, period =>5},
    ChildSpecs = [#{id => ch3,
                    start => {ch3, start_link, []},
                    restart => permanent,
                    shutdown => brutall_kill,
                    type => worker,
                    modules =>[cg3]}],
    {ok, {SupFlags, ChildSpecs}}.
