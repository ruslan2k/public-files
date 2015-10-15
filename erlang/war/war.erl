-module(war).
-compile(export_all).


start() ->
    spawn(fun() -> loop([]) end).
start(L) ->
    spawn(fun() -> loop(L) end).


loop(Cards) ->
    receive
        {From, {pass_card, NewCards}} ->
            io:format("Received cards:~p~n", [NewCards]),
            From ! {self(), ok},
            loop(NewCards);
        {From, get_card} ->
            io:format("Cards:[~p]~n", [Cards]),
            NewCards = case Cards of
                [] ->
                    From ! {self(), empty},
                    Cards;
                [H | T] ->
                    From ! {self(), H},
                    T
            end,
            loop(NewCards);
        Any ->
            io:format("Received:~p~n", [Any]),
            io:format("Cards:~p~n", [Cards]),
            loop(Cards)
    end.


rpc(Pid, Request) ->
    io:format("Pid=[~p] Request=[~p]~n", [Pid, Request]),
    Pid ! {self(), Request},
    receive
        {Pid, Response} ->
            Response
    end.

server_node() ->
    {ok, Host} = inet:gethostname(),
    list_to_atom("table@" ++ Host).


logon(Name) ->
    case whereis(card_player) of
        undefined ->
            register(card_player, spawn(war, player, [server_node(), Name]));
        _ -> already_logged_on
    end.


player(ServerNode, Name) ->
    {table, ServerNode} ! {self(), logon, Name},
    await_result(),
    player(ServerNode).


player(ServerNode) ->
    receive
        logoff ->
            exit(normal);
        Any ->
            io:format("Any:<~p>~n", [Any])
    end,
    player(ServerNode).


await_result() ->
    receive
        {table, stop, Why} -> % Stop the player
            io:format("~p~n", [Why]),
            exit(normal);
        {table, What} -> % Normal response
            io:format("~p~n", [What])
    after
        5000 ->
            io:format("Timeout", [])
    end.


get_card(Pid) -> rpc(Pid, get_card).


shuffle_cards() -> [random:uniform(10) || _ <- lists:seq(1, 6)].


main() ->
    P1 = start(),
    P2 = start(),
    Cards = shuffle_cards(),
    {C1, C2} = lists:split(length(Cards) div 2, Cards),
    rpc(P1, {pass_card, C1}),
    rpc(P2, {pass_card, C2}),
    play_cards(P1, P2, []),
    %
    io:format("End~n", [])
    .


play_cards(P1, P2, Cards) -> 
    C1 = rpc(P1, get_card),
    C2 = rpc(P2, get_card),
    case {C1, C2} of
        {empty, empty} -> nobody;
        {_, empty} -> P1;
        {empty, _} -> P2;
        {_, _} -> true
    end.


loop_test(Value) -> Value - 1.


loop(Cards) ->
    receive
        {From, {pass_card, NewCards}} ->
            io:format("Received cards:~p~n", [NewCards]),
            From ! {self(), ok},
            loop(NewCards);
        {From, get_card} ->
            io:format("Cards:[~p]~n", [Cards]),
            NewCards = case Cards of
                [] ->
                    From ! {self(), empty},
                    Cards;
                [H | T] ->
                    From ! {self(), H},
                    T
            end,
            loop(NewCards);
        Any ->
            io:format("Received:~p~n", [Any]),
            io:format("Cards:~p~n", [Cards]),
            loop(Cards)
    end.
