
-module(myapp_sup).

-behaviour(supervisor).

%% API
-export([start_link/0]).

%% Supervisor callbacks
-export([init/1]).

%% Helper macro for declaring children of supervisor
-define(CHILD(I, Type), {I, {I, start_link, []}, permanent, 5000, Type, [I]}).

%% ===================================================================
%% API functions
%% ===================================================================

start_link() ->
    supervisor:start_link({local, ?MODULE}, ?MODULE, []).

%% ===================================================================
%% Supervisor callbacks
%% ===================================================================

init([]) ->
    %% ChildSpecs = [#{id => ch3,
    %%                 start => {ch3, start_link, []},
    %%                 restart => permanent,
    %%                 shutdown => brutal_kill,
    %%                 type => worker,
    %%                 modules => [ch3]}],
    %% {ok, { {one_for_one, 5, 10}, ChildSpecs} }.
    {ok, { {one_for_one, 5, 10}, []} }.
