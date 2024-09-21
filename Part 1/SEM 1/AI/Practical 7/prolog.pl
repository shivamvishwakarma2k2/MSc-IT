fruits(apple).
fruits(kiwi).
fruits(pomegranate).
fruits(strawberry).
fruits(orange).
fruits(grapes).
fruits(bananas).
fruits(guava).


sweet(guava).
sweet(kiwi).
sweet(pomegranate).
sweet(strawberry).
sweet(banana).
sweet(apple).

sour(grapes).
sour(orange).

veg(tomato).    
veg(chilli).
veg(potato).
veg(capsicum).

likes(X) :- fruits(X),sweet(X).

dislikes(Y) :- fruits(Y),sour(Y).
