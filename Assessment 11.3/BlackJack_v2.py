"""BlackJack version 2."""

import random
import highscores

# define suits and ranks for the deck
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# define base card values
base_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

# define available player options
cards_options = ["stand", "hit", "surrender", "double down"]


def create_deck():
    """Shuffles cards. Creates deck."""
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def draw_card(deck):
    """Draws a card from the deck, reshuffling if empty."""
    if not deck:
        print("Deck empty, reshuffling...")
        deck.extend(create_deck())  # refill deck if empty
    return deck.pop(0)


def card_value(card):
    """Values the hand."""
    rank = card.split()[0]
    return base_values[rank]


def hand_value(hand):
    """Ace handling and gives the value of the hand."""
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card.startswith("A"))

    while total > 21 and aces:
        total -= 10  # adjust ace value from 11 to 1
        aces -= 1

    return total


def dealer_turn(deck, dealer_hand):
    """Dealer draws until hand value is at least 17."""
    print(f"Dealer's hidden card was: {dealer_hand[1]}")

    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))

    print(f"Dealer's hand: {dealer_hand} (Value: {hand_value(dealer_hand)})")
    return hand_value(dealer_hand)


def compare_hand_to_dealer(hand, dealer_total, bet):
    """Compare player's hand with dealer's and return outcome."""
    player_total = hand_value(hand)

    if player_total > 21:
        print(f"{hand} busted. 💀 You lose {bet}.")
        return -bet

    elif dealer_total > 21 or player_total > dealer_total:
        print(f"{hand} wins! 🎉 You win {bet}.")
        return bet

    elif player_total < dealer_total:
        print(f"{hand} loses. 💀 You lose {bet}.")
        return -bet

    else:
        print(f"{hand} pushes 🤝 (tie).")
        return 0


def play_split_hand(deck, hand):
    """Play a split hand, allowing hit or stand."""
    while True:
        if hand_value(hand) > 21:
            print(f"{hand} busts!")
            return hand

        value = hand_value(hand)
        choice = input(f"{hand} (Value: {value}) - Hit or Stand? ").lower()

        if choice == "hit":
            card = draw_card(deck)
            hand.append(card)
            print(f"You drew: {card}")

        elif choice == "stand":
            break

        else:
            print("Invalid choice. Please type 'hit' or 'stand'.")

    return hand


def hand_split(deck, player_hand, dealer_hand, balance, bet):
    """Handle splitting of a hand into two separate hands."""
    print("\n--- Splitting Hand! ---")

    hand1 = [player_hand[0], draw_card(deck)]
    hand2 = [player_hand[1], draw_card(deck)]

    balance -= bet

    print(f"Hand 1: {hand1} (Value: {hand_value(hand1)})")
    print(f"Hand 2: {hand2} (Value: {hand_value(hand2)})")

    print("\n--- Hand 1 ---")
    hand1 = play_split_hand(deck, hand1)

    print("\n--- Hand 2 ---")
    hand2 = play_split_hand(deck, hand2)

    dealer_total = dealer_turn(deck, dealer_hand)

    balance += compare_hand_to_dealer(hand1, dealer_total, bet)
    balance += compare_hand_to_dealer(hand2, dealer_total, bet)

    return balance


def play_round(balance, deck):
    """Play a single round of Blackjack."""
    bet = 0

    while True:
        try:
            bet = int(input("Place your bet: "))
            if bet > balance:
                raise ValueError
            if bet > 0:
                break
        except ValueError:
            print("Invalid, Try again")
            continue

    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    print(f"Your hand: {player_hand} (Value: {hand_value(player_hand)})")
    print(f"Dealer shows: {dealer_hand[0]}")

    # check if player has a pair for split
    if player_hand[0].split()[0] == player_hand[1].split()[0]:
        split_choice = input("You have a pair! Split? (y/n): ").lower()
        if split_choice != 'n':
            return hand_split(deck, player_hand, dealer_hand, balance, bet)

    while True:
        if hand_value(player_hand) > 21:
            print("Bust! You lose.")
            return balance - bet

        choice = input(f"Choose {cards_options}: ").lower()

        if choice == "surrender":
            print("You surrendered! Lose half bet.")
            return balance - bet / 2

        elif choice == "stand":
            break

        elif choice == "hit":
            card = draw_card(deck)
            player_hand.append(card)
            print(f"You drew: {card}")
            value = hand_value(player_hand)
            print(f"Your hand: {player_hand} (Value: {value})")

        elif choice == "double down":
            bet *= 2
            card = draw_card(deck)
            player_hand.append(card)
            print(f"You drew: {card}")
            value = hand_value(player_hand)
            print(f"Your hand: {player_hand} (Value: {value})")

            if hand_value(player_hand) > 21:
                print("Double Down! You lose double the bet.")
                return balance - bet
            else:
                break

        else:
            print("Invalid choice. Try again.")

    dealer_total = dealer_turn(deck, dealer_hand)
    balance += compare_hand_to_dealer(player_hand, dealer_total, bet)
    return balance


def main(name):
    """BlackJack runs."""
    print(f"\nHello {name}! Nice choice!")
    print("----------Welcome to the Game of BlackJack----------")

    # instructions
    print("\n=== Instructions ===")
    print("1. You start with a balance of 1000 cards.")
    print("2. Place a bet at the start of each round.")
    print("3. You and the dealer get two cards. One is hidden.")
    print("4. Your goal: get closer to 21 than dealer without going over.")
    print("5. Options each turn:")
    print("   - Hit: draw another card")
    print("   - Stand: keep your hand")
    print("   - Double Down: double bet and draw one final card")
    print("   - Surrender: give up half your bet")
    print("   - Split: split if first two cards are a pair")
    print("6. Ace counts as 11 or 1; face cards are 10.")
    print("7. If you bust (go over 21), you lose the round.")
    print("9. Wins/losses adjust balance. Balance 0 = game over!\n")

    start_ = input(f"Are you ready {name}? (y/n) ").lower()
    if start_ not in ("yes", "y"):
        print("Dont rush, take your time to think, you are welcomed here.")
        return 0

    print(f"Good luck {name}:)")

    balance = 1000
    deck = create_deck()

    while balance > 0:
        print(f"\nBalance: {balance} cards")
        balance = play_round(balance, deck)
        cont = input(f"Wanna play again {name}? (y/n): ").lower()
        if cont == 'n':
            break

    highscores.HighScores.save("BlackJack", name, balance, None)
    highscores.HighScores.show("BlackJack")
    return 1


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    main(player_name)
