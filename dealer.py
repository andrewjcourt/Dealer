# dealer
# BUILD a standard 52-card deck (text representation) SHUFFLE it, DISPLAY it, and DEAL hands

def build_deck():
    face = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suit = [u'\u2665'.encode('utf-8'), u'\u2666'.encode('utf-8'), u'\u2663'.encode('utf-8'), u'\u2660'.encode('utf-8')]
    deck = []
    deck = [str(f + s) for s in suit for f in face]
    return deck

def shuffle():
    stack = [None] * 52
    deck = build_deck()
    import random
    for i in range(0, 52):
        n = random.randint(0, len(deck)-1)
        stack[i] = deck[n]
        deck.pop(n)
    return stack

def display(stack):
    for card in stack: print card.decode('utf-8'),
    return

def deal(x, stack):
    hand = stack[0:x]
    stack = stack[x:]
    return hand, stack

# deck = shuffle()
# display(deck) or display(shuffle())
# hand = deal(x, deck) ... returns hand[0] (hand of x cards) and hand[1] (the remaining stack)

# example: shuffle deck, display shuffled deck, and deal & display four hands of seven cards:

print('Cards shuffled and dealt by *dealer.py* by Andrew Court'); print
deck = build_deck()
print('Build 52-card deck:')
display(deck)
print;print
deck = shuffle()
print('Shuffle deck:')
display(deck)
print; print
print('Deal four 7-card hands:')
for i in range(0, 4):
    hand = deal(7, deck)
    display(hand[0])
    print
    deck = hand[1]
print
print('Display undealt cards in stack:')
display(deck)






   






