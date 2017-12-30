'''
DEALER
by Andrew Court

Create a standard 52-card deck. Shuffle & deal cards. Sort by suit or face value.
Display cards with Unicode suit icons.
'''

def build_deck():
    '''
    Return a list of 52 playing-card identifiers for display, dealing, sorting etc.
    Each card is a tuple: ((face value, suit value), (string)).
    The first tuple item [(f, s) pair] enables sorting functions.
    deck = build_deck() returns a 52-card deck in standard order.
    '''
    face = ['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    suit = [u'\u2665'.encode('utf-8'), u'\u2666'.encode('utf-8'),
            u'\u2663'.encode('utf-8'), u'\u2660'.encode('utf-8')]
    face_value = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    suit_value = [4, 3, 2, 1]
    cards = [str(f + s) for s in suit for f in face]
    values = [(f, s) for s in suit_value for f in face_value]
    deck = zip (values, cards)
    return deck

def shuffle():
    '''
    Return a 'stack' of shuffled cards.
    deck = shuffle() returns shuffled deck by appending one randomly-chosen card for each of 52 iterations.
    Calls build_deck().
    '''
    stack = [None] * 52
    deck = build_deck()
    import random
    for i in range(0, 52):
        n = random.randint(0, len(deck)-1)
        stack[i] = deck[n]
        deck.pop(n)
    return stack

def display(cards):
    '''
    Decode card identifier string to display cards with Unicode suit icons.
    '''
    for card in cards: print(card[1].decode('utf-8')),
    return

def deal(x, stack):
    '''
    Deal a hand of cards.
    hand = deal(x, stack) returns hand[0] (hand of x cards) and hand[1] (remaining cards in stack).
    '''
    hand = stack[0:x]
    stack = stack[x:]
    return hand, stack

def sort(hand, option=1):
    '''
    Sort cards by suit (and value within suit) or face value (and suit within value).
    Option: 1 = sort by suit (default), 2 = sort by value.
    hand = sort(hand, option) assigns sorted hand.
    display(sort(hand, option)) displays sorted hand without assignment.
    '''
    if option == 1:
        hand = sorted(hand)
        hand.sort(key=lambda x:x[0][1])
        hand.reverse()
    if option == 2:
        hand = sorted(hand)
        hand.reverse()
    return hand
