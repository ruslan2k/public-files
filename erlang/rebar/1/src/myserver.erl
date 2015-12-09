-module(myserver).
-behaviour(gen_server).
-define(SERVER, ?MODULE).
-define(DEFAULT_PORT, 1055).

-record(state, {port, lsock, request_count = 0}).

%% ------------------------------------------------------------------
%% API Function Exports
%% ------------------------------------------------------------------

-export([start_link/0]).

%% ------------------------------------------------------------------
%% gen_server Function Exports
%% ------------------------------------------------------------------

-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
         terminate/2, code_change/3]).

-export([get_count/0]).
-export([increment_count/0]).
-export([stop/0]).

%% ------------------------------------------------------------------
%% API Function Definitions
%% ------------------------------------------------------------------

start_link(Port) ->
    gen_server:start_link({local, ?SERVER}, ?MODULE, [Port], []).

start_link() ->
    start_link(?DEFAULT_PORT).
%% ------------------------------------------------------------------
%% gen_server Function Definitions
%% ------------------------------------------------------------------

init([Port]) ->
    {ok, LSock} = gen_tcp:listen(Port, [{active, true}]),
    State = #state{port = Port, lsock = LSock},
    {ok, State}.

%%handle_call(_Request, _From, State) ->
%%    {reply, ok, State}.
handle_call(get_count, _From, State) ->
    {reply, {ok, State#state.request_count}, State};

handle_call(increment_count, _From, State) ->
    RequestCount = State#state.request_count,
    State1 = State#state{request_count = RequestCount + 1},
    {reply, ok, State1}.

%%handle_cast(_Msg, State) ->
%%    {noreply, State}.
handle_cast(stop, State) ->
    {stop, normal, State}.

handle_info(_Info, State) ->
    {noreply, State}.
%handle_info(timeout, State) ->
%    {ok, _Sock} = gen_tcp:accept(State

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.

%% ------------------------------------------------------------------
%% Internal Function Definitions
%% ------------------------------------------------------------------

%% ------------------------------------------------------------------
%% External Function Definitions
%% ------------------------------------------------------------------

%%
%% @doc
%%
get_count() ->
    gen_server:call(?SERVER, get_count).

increment_count() ->
    gen_server:call(?SERVER, increment_count).

stop() ->
    gen_server:cast(?SERVER, stop).
