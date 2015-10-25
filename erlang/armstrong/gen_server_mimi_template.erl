%%

-module(module_name).

%% gen_server_mini_template

-behavior(gen_server).
-export([start_link/0]).

%% gen_server callbacks
-export([init/1]).
-export([handle_call/3]).
-export([handel_cast/2]).
-export([handle_info/2]).
-export([terminate/2]).
-export([code_change/3]).



start_link() ->
  gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).








