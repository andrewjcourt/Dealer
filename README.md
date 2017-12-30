# Dealer
Create a standard 52-card deck. Shuffle & deal cards. Sort by suit or face value. Display cards with Unicode suit icons.

Python.

*** Requires Unicode fonts to display suit icon characters: ♥ ♦ ♣ ♠ ***

To instantiate:

from dealer import *

deck = shuffle(); display(deck)

To deal a hand of 7 cards:

hand = deal(7, deck); display(hand[0])

Sort by suit:

hand = sort(hand, 1); display(hand)

... or by face value:

hand = sort(hand, 2)
