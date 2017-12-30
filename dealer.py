#!/usr/bin/env python

''' |   DEALER by Andrew Court
    |
    |   Create a standard 52-card deck. Shuffle & deal cards. Sort by suit or face value.
    |   Display cards with Unicode suit icons. '''


def build_deck():
    
    '''     |   Returns a list of playing-card identifiers where each card is
            |   identifed by the tuple ((face value, suit value), (string)).
            |   The (f, s) pair is required for sorting functions.
            |
            |   deck = build_deck() returns 52-card deck in standard order. '''
    
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

    '''     |   Returns a 'stack' of shuffled cards by appending one randomly-chosen card
            |   for each of 52 iterations.
            |
            |   deck = shuffle() returns shuffled deck of cards. '''
    
    stack = [None] * 52
    deck = build_deck()
    import random
    for i in range(0, 52):
        n = random.randint(0, len(deck)-1)
        stack[i] = deck[n]
        deck.pop(n)
    return stack

def display(cards):

    '''     |   Displays cards by decoding the string for each card identifier tuple. '''
    
    for card in cards: print(card[1].decode('utf-8')),
    return

def deal(x, stack):

    '''     |   Deals x number of cards from stack of cards.
            |
            |   hand = deal(x, stack) returns hand[0] (hand of x cards) and hand[1] (remaining cards in stack). '''

    hand = stack[0:x]
    stack = stack[x:]
    return hand, stack

def sort(hand, option):

    '''     |   Sorts cards by suit (and value within suit) or face value (and suit within value)
            |
            |   hand = sort(hand, option) [or display(sort(hand, option))]
            |       - Assigns sorted hand [or displays sorted hand without assignment]
            |       - Option: 1 = sort by suit, 2 = sort by value. '''

    if option == 1:
        hand = sorted(hand)
        hand.sort(key=lambda x:x[0][1])
        hand.reverse()
    if option == 2:
        hand = sorted(hand)
        hand.reverse()
    return hand


            








   






