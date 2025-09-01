import random
from logging import raiseExceptions

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}
player_hand = []
dealer_hand = []
cards_options = ["stand", "hit", "surrender", "double down", "split"]

card_deck = [(rank, suit, card_values[rank]) for suit in suits for rank in ranks]
random.shuffle(card_deck)


def draw_card(deck):
    if len(deck) == 0:
        return None
    card = deck.pop(0)
    rank, suit, value = card
    print(f"You drew: {rank} of {suit}")
    return card


def hand_value(hand):
    total = sum(card[2] for card in hand)
    aces = sum(1 for card in hand if card[0] == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def

def main():
    player_hand.append(draw_card(card_deck))
    player_hand.append(draw_card(card_deck))
    print(player_hand)
    print(hand_value(player_hand))
    more = "none"
    while more != "surrender":
        try:
            more = input(f"Make Your Choice: {cards_options} ").lower()
            if more not in cards_options:
                raise Exception
        except Exception:





