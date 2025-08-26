import random as r
balance = 200
while True:  # 🔁 retry loop
    total = 0
    dtotal = 0

    card_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q","K", "A"]
    player = []
    dealer = []
    lost = "n"
    print(f"Your balance is {balance}")
    while True:
        try:
            bid = int(input("Place your bid: "))
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
                total + 11
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
                            total + 11
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
        except Exception:
            print("Error")
            continue

    dealer.append(r.choice(card_number))
    dealer.append(r.choice(card_number))
    for a in dealer:
        if a == "K" or a == "Q" or a == "J":
            dtotal += 10
        elif a == "A":
            dtotal += 11
        else:
            dtotal += a
    if dtotal < 18:
        dealer.append(r.choice(card_number))
        dtotal = 0
        for b in dealer:
            if b == "K" or b == "Q" or b == "J":
                dtotal += 10
            elif b == "A":
                dtotal += 11
            else:
                dtotal += b
        if dtotal < 19:
            if r.randint(1,20) > 3:
                dealer.append(r.choice(card_number))
                dtotal = 0
                for b in dealer:
                    if b == "K" or b == "Q" or b == "J":
                        dtotal += 10
                    elif b == "A":
                        dtotal += 11
                    else:
                        dtotal += b
    print(f"the dealer total is {dtotal}")

    if lost == "n":
        if dtotal > 21:

            print("the dealer busts, you win!")
            balance += 3 * bid

        if total > dtotal:
            print("You Win!")
            balance += 2 * bid
        elif total == dtotal:
            print("It is a draw")
        else:
            print("The dealer Won!")
            balance -= bid
    print(f"Your balance is {balance}")

    if balance != 0:
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break
    else:
        print("Thanks for playing!")
        break
