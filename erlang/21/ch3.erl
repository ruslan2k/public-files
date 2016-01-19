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
