% Define the constraint that ensures no two variables have the same digit.
all_different([]).
all_different([H|T]) :- \+ member(H, T), all_different(T).

% Define the main predicate for solving the puzzle.
send_more_money([S, E, N, D, M, O, R, Y]) :-
    Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    member(S, Digits), S > 0,
    member(E, Digits),
    member(N, Digits),
    member(D, Digits),
    member(M, Digits), M > 0,
    member(O, Digits),
    member(R, Digits),
    member(Y, Digits),
    all_different([S, E, N, D, M, O, R, Y]),
    1000 * S + 100 * E + 10 * N + D +
    1000 * M + 100 * O + 10 * R + E =:= 
    10000 * M + 1000 * O + 100 * N + 10 * E + Y.
