% Define the constraint that ensures no two variables have the same digit.
all_different([]).
all_different([H|T]) :- \+ member(H, T), all_different(T).

% Define the main predicate for solving the puzzle.
to_go_out([T, O, G, U]) :-
    Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    member(T, Digits), T > 0,  % T cannot be 0
    member(O, Digits),
    member(G, Digits),
    member(U, Digits),
    member(N, Digits), N > 0,  % N cannot be 0 (first digit of OUT)
    member(E, Digits),
    all_different([T, O, G, U, N, E]),
    
    % Equation for the problem: TO + GO = OUT
    10 * T + O + 10 * G + O =:= 1000 * O + 100 * U + 10 * T + N.
