# Dealer
Create a standard 52-card deck. Shuffle & deal cards. Sort by suit or face value. Display cards with Unicode suit icons.

Python.

*** Requires Unicode fonts to display suit icon characters: ♥ ♦ ♣ ♠ ***

### MODULE FUNCTIONS

### build_deck():

Return a list of 52 playing-card identifiers for display, dealing, sorting etc.
Each card is a tuple: ((face value, suit value), (string)).
The first tuple item [(f, s) pair] enables sorting functions.
deck = build_deck() returns a 52-card deck in standard order.

### shuffle():

Return a 'stack' of shuffled cards.
deck = shuffle() returns shuffled deck by appending one randomly-chosen card for each of 52 iterations.
Calls build_deck()

### display(cards):

Decode card identifier string to display cards with Unicode suit icons.

### deal(x, stack):

Deal a hand of cards.
hand = deal(x, stack) returns hand[0] (hand of x cards) and hand[1] (remaining cards in stack).

### sort(hand, option):

Sort cards by suit (and value within suit) or face value (and suit within value).
Option: 1 = sort by suit (default), 2 = sort by value.
hand = sort(hand, option) assigns sorted hand.
display(sort(hand, option)) displays sorted hand without assignment.
