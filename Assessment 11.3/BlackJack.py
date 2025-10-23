"""Python BlackJack v1.6 (Done)."""

import random as r
balance = 1000
print("--------------Welcome to Black Jack Version 1.8--------------")
while True:
    total = 0
    dealer_total = 0
    d_bust = "n"
    card_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    player = []
    dealer = []
    lost = "n"
    bid = 0
    print(f"Your balance is {balance}")
    while True:
        try:
            bid = int(input("Place your bid: "))
            if bid > balance:
                raise ValueError
            break
        except ValueError:
            print("Invalid biding")

    player.append(r.choice(card_number))
    player.append(r.choice(card_number))
    print(f"Your hand: {player}")
    aces1 = 0
    for a in player:
        if a == "K" or a == "Q" or a == "J":
            total += 10
        elif a == "A":
            total += 11
            aces1 += 1
        else:
            total += a
    while total > 21 and aces1 > 0:
        total -= 10
        aces1 -= 1
    print(f"Your total is: {total}")
    dealer.append(r.choice(card_number))
    dealer.append(r.choice(card_number))
    print(f"Dealer shows: {dealer[0]}")

    aces = 0
    for a in dealer:
        if a == "K" or a == "Q" or a == "J":
            dealer_total += 10
        elif a == "A":
            dealer_total += 11
            aces += 1
        else:
            dealer_total += a
    while dealer_total > 21 and aces > 0:
        dealer_total -= 10
        aces -= 1
    while True:
        try:
            another_one = input("Get another card? (y/n): ").lower()
            if another_one == "y":
                player.append(r.choice(card_number))
                print(f"Your hand: {player}")
                total = 0
                aces1 = 0
                for a in player:
                    if a == "K" or a == "Q" or a == "J":
                        total += 10
                    elif a == "A":
                        total += 11
                        aces1 += 1
                    else:
                        total += a
                while total > 21 and aces1 > 0:
                    total -= 10
                    aces1 -= 1
                print(f"Your total is: {total}")
                if total > 21:
                    lost = "y"
                    print("Bust! You lost")
                    balance -= bid
                    break
                else:
                    continue
            elif another_one == "n":
                break
            else:
                raise ValueError
        except ValueError:
            print("Error")
            continue

    if lost == "n":
        while dealer_total < 17:
            dealer.append(r.choice(card_number))
            dealer_total = 0
            aces = 0
            for a in dealer:
                if a == "K" or a == "Q" or a == "J":
                    dealer_total += 10
                elif a == "A":
                    dealer_total += 11
                    aces += 1
                else:
                    dealer_total += a
            while dealer_total > 21 and aces > 0:
                dealer_total -= 10
                aces -= 1

        print(f"dealer hand: {dealer}")
        print(f"dealer total: {dealer_total}")

        if dealer_total > 21:
            d_bust = "y"
            print("The dealer busts, you win!")
            balance += bid

        if total > dealer_total:
            print("You Win!")
            if len(player) == 2:
                balance += 1.5 * bid
            else:
                balance += bid
        elif total == dealer_total:
            print("It is a draw")
        elif d_bust == "n":
            print("The dealer Won!")
            balance -= bid
        print(f"Your balance is {balance}")

    again = input("Do you want to play again? (y/n): ").lower()
    if again == "n":
        print("Thanks for playing!")
        print("-------------------------------------------------------------")
        break
    else:
        if balance == 0:
            print("You sold your Car")
            print("Your balance has been reset to 20000")
            balance = 20000
