%% https://medium.com/@kansi/getting-started-with-otp-creating-psycho-families-b4f6ce01d1e4#.cq8oo7a1j

-module(ch3).
-behaviour(gen_server).

-export([start_link/0]).

-export([alloc/0]).
-export([free/1]).

-export([init/1]).
-export([handle_call/3]).
-export([handle_cast/2]).

start_link() ->
    gen_server:start_link({local, ch3}, ch3, [], []).

alloc() ->
    gen_server:call(ch3, alloc).

free(Ch) ->
    gen_server:cast(ch3, {free, Ch}).

init(_Args) ->
    {ok, channels()}.

handle_call(alloc, _From, Chs) ->
    {Ch, Chs2} = alloc(Chs),
    {reply, Ch, Chs2}.

handle_cast({free, Ch}, Chs) ->
    Chs2 = free(Ch, Chs),
    {noreply, Chs2}.

%%% Internal

channels() ->
    [ch1, ch2, ch3].

alloc([Channel|Channels]) ->
    {Channel, Channels};
alloc([]) ->
    false.

free(Channel, Channels) ->
    [Channel | Channels].
