-module(name_server).
-export([init/0]).
-export([add/2]).
-export([find/1]).
-export([handle/2]).
-import(server1, [rpc/2]).

add(Name, Place) -> rpc(name_server, {add, Name, Place}).
find(Name)       -> rpc(name_server, {find, Name}).

init() -> dict:new().
