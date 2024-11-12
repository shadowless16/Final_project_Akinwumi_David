import random

# Deck of cards with values 
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

def deal_card():
    return deck.pop()

def calculate_hand(hand):
    value = 0
    ace_count = 0
    for card in hand:
        if card in 'JQK':
            value += 10
        elif card == 'A':
            value += 11
            ace_count += 1
        else:
            value += int(card)
    
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

