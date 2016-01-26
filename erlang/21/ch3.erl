-module(ch3).
-behaviour(gen_server).

-export([start_link/0]).

-export([alloc/1]).
-export([free/1]).

-export([init/1]).
-export([handle_call/3]).
-export([handle_cast/2]).
-export([handle_info/2]).
-export([terminate/2]).

start_link() ->
    gen_server:start_link({local, ch3}, ch3, [], []).

init(_Args) ->
    {ok, #{channels => []}}.

alloc(Channel) ->
    gen_server:call(ch3, {alloc. Chanel}).

free(Ch) ->
    gen_server:cast(ch3, {free, Ch}).

handle_call({alloc, Ch}, _From, #{channels := Chs} = State) ->
    Chs_new = [Ch | Chs],
    {reply, ok, State#{channels => Chs_new}}.

handle_cast({free, Ch}, #{channels := Chs} = State) ->
    Chs2 = lists:filter(fun(X) ->
                            if X == Ch -> false;
                                true -> true
                            end
                        end, Chs),
    {noreply, State#{channels => Chs2}}.

handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVersion, Library, _Extra) -> {ok, Library}.
