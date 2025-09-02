import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}
player_hand = []
dealer_hand = []
cards_options = ["stand", "hit", "surrender", "double down"]

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

def hand_split():
    pass

def main():
    balance = 500
    bet = 100
    player_hand.append(draw_card(card_deck))
    player_hand.append(draw_card(card_deck))
    print(f"Your hand: {player_hand}")
    print(f"Your hand's Value: {hand_value(player_hand)}")
    more = "none"
    while more != "surrender":
        try:
            more = input(f"Make Your Choice: {cards_options} ").lower()
            match more:
                case n if n == "surrender":
                    balance -= bet / 2
                case n if n == "stand":
                    break
                case n if n == "hit":
                    player_hand.append(draw_card(card_deck))
                    print(f"Your hand: {player_hand}")
                    print(f"Your hand's Value: {hand_value(player_hand)}")
                    continue
                case n if n == "double down":
                    player_hand.append(draw_card(card_deck))
                    print(f"Your hand: {player_hand}")
                    print(f"Your hand's Value: {hand_value(player_hand)}")
                    break
                case _:
                    raise TypeError
        except TypeError:
            print("Invalid Prompt")





