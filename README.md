# deal-with-it
Create &amp; shuffle a standard 52-card deck; deal &amp; display hands.

*** Requires Unicode fonts to display suit characters ***

To instantiate:

from shuffler import *

deck = shuffle()

display(deck)

To deal a hand of 7 cards:

hand = deal(7, deck)

display(hand[0])

deck = hand[1] # remainder of shuffled deck
