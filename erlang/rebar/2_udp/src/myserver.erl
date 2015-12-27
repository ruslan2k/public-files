-module(myserver).
-behaviour(gen_server).

-define(SERVER, ?MODULE).
-define(DEF_PORT, 2345).
-define(DEF_FILE, "/tmp/File.bin").

-record(state, {udp_sock, io_device, counter = 0}).

%% ------------------------------------------------------------------
%% API Function Exports
%% ------------------------------------------------------------------

-export([start_link/0]).

%% ------------------------------------------------------------------
%% gen_server Function Exports
%% ------------------------------------------------------------------

-export([init/1, handle_call/3, handle_cast/2, handle_info/2,
         terminate/2, code_change/3]).

%% ------------------------------------------------------------------
%% API Function Definitions
%% ------------------------------------------------------------------

start_link(Port, FileName) ->
    gen_server:start_link({local, ?SERVER}, ?MODULE, [Port, FileName], []).

start_link() ->
    start_link(?DEF_PORT, ?DEF_FILE).

%% ------------------------------------------------------------------
%% gen_server Function Definitions
%% ------------------------------------------------------------------

init([Port, FileName]) ->
    {ok, Socket} = gen_udp:open(Port, [binary]),
    io:format("Socket[~p]~n", [Socket]),
    {ok, IoDevice} = file:open(FileName, [write, binary]),
    State = #state{udp_sock = Socket, io_device = IoDevice},
    {ok, State}.

handle_call(_Request, _From, State) ->
    {reply, ok, State}.

handle_cast(_Msg, State) ->
    {noreply, State}.

handle_info({udp, Socket, _Ip, _Port, Msg}, State) ->
    [A1, A2 | _] = binary_to_list(Msg),
    IoDevice = State#state.io_device,
    ok = file:write(IoDevice, Msg),
    io:format("receive udp size[~p] Socket[~p] ip[~p] port[~p]~n", [byte_size(Msg), Socket, _Ip, _Port]),
    io:format("A1 ~p A2 ~p~n", [A1, A2]),
    io:format("bye~n", []),
    {noreply, State}.

terminate(_Reason, _State) ->
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.

%% ------------------------------------------------------------------
%% Internal Function Definitions
%% ------------------------------------------------------------------
