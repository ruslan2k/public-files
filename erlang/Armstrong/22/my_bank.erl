-module(my_bank).

-behavior(gen_server).
-export([start/0]).

%% gen server callbacks
-export([init/1]).
-export([handle_call/3]).
-export([handle_cast/2]).
-export([handle_info/2]).
-export([terminate/2]).
-export([code_change/3]).

-compile(export_all).
-define(SERVER, ?MODULE).


start() -> gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).
stop()  -> gen_server:call(?MODULE, stop).

new_account(Who)      -> gen_server:call(?MODULE, {new, Who}).
deposit(Who, Amount)  -> gen_server:call(?MODULE, {add, Who, Amount}).
withdraw(Who, Amount) -> gen_server:call(?MODULE, {remove, Who, Amount}).

init({}) -> {ok, ets:new(?MODULE, [])}.

handle_call({new, Who}, _From, Tab) ->
    Replay = case ets:lookup(Tab, Who) of
            [] -> ets:insert(Tab, {Who, 0}),
                {welcome, Who};
            [_] -> {Who, you_already_are_a_customer}
        end,
    {reply, Reply, Tab};
