# Dealer
Create a standard 52-card deck. Shuffle & deal cards. Sort by suit or face value. Display cards with Unicode suit icons.

Python.

*** Requires Unicode fonts to display suit icon characters: ♥ ♦ ♣ ♠ ***

Module functions:

build_deck():
    Return a list of 52 playing-card identifiers for display, dealing, sorting etc.
    Each card is a tuple: ((face value, suit value), (string)).
    The first tuple item [(f, s) pair] enables sorting functions.
    deck = build_deck() returns a 52-card deck in standard order.
