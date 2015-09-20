-module(user).

-export([init/0]).

-include_lib("stdlib/include/qlc.hrl").
-include("user_record.hrl").


init() ->
    mnesia:create_table(user, []).


