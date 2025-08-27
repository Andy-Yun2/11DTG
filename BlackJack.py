import random as r
balance = 1000

while True:
    total = 0
    dealer_total = 0
    d_bust = "n"
    card_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q","K", "A"]
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
    print(player)
    for i in player:
        if i == "K" or i == "Q" or i == "J":
            total += 10
        elif i == "A":
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        else:
            total += i
    print(total)
    while True:
        try:
            another_one = input("Get another card? ").lower()
            if another_one == "y":
                player.append(r.choice(card_number))
                print(player)
                total = 0
                for i in player:
                    if i == "K" or i == "Q" or i == "J":
                        total += 10
                    elif i == "A":
                        if total + 11 > 21:
                            total += 1
                        else:
                            total += 11
                    else:
                        total += i
                print(total)
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

    dealer.append(r.choice(card_number))
    dealer.append(r.choice(card_number))
    for a in dealer:
        if a == "K" or a == "Q" or a == "J":
            dealer_total += 10
        elif a == "A":
            dealer_total += 11
        else:
            dealer_total += a
    for i in range(3):
        if dealer_total < 18:
            dealer.append(r.choice(card_number))
            dealer_total = 0
            for b in dealer:
                if b == "K" or b == "Q" or b == "J":
                    dealer_total += 10
                elif b == "A":
                    dealer_total += 11
                else:
                    dealer_total += b
            if dealer_total < 19:
                if r.randint(1,20) > 3:
                    dealer.append(r.choice(card_number))
                    dealer_total = 0
                    for b in dealer:
                        if b == "K" or b == "Q" or b == "J":
                            dealer_total += 10
                        elif b == "A":
                            dealer_total += 11
                        else:
                            dealer_total += b
            if dealer_total < 20:
                if r.randint(1, 100) > 95:
                    dealer.append(r.choice(card_number))
                    dealer_total = 0
                    for c in dealer:
                        if c == "K" or c == "Q" or c == "J":
                            dealer_total += 10
                        elif c == "A":
                            dealer_total += 11
                        else:
                            dealer_total += c
    if lost == "n":
        print(dealer)
        print(f"the dealer total is {dealer_total}")

    if lost == "n":
        if dealer_total > 21:
            d_bust = "y"
            print("the dealer busts, you win!")
            balance += 3 * bid

        if total > dealer_total:
            print("You Win!")
            balance += 2 * bid
        elif total == dealer_total:
            print("It is a draw")
            balance -= bid
        elif d_bust == "n":
            print("The dealer Won!")
            balance -= bid
    print(f"Your balance is {balance}")

    if balance != 0:
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break
        else:
            continue
    else:
        print("Thanks for playing!")
        break
