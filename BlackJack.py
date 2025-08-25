import random as r
total = 0
dtotal = 0

card_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q","K", "A"]
player = []
dealer = []

player.append(r.choice(card_number))
player.append(r.choice(card_number))
print(player)

another_one = input("Get another card? ").lower()
if another_one == "y":
    player.append(r.choice(card_number))
else:
    pass

for i in player:
    if i == "K" or i == "Q" or i == "J":
        total += 10

    elif i == "A":
        total += 11
    else:
        total += i

dealer.append(r.choice(card_number))
dealer.append(r.choice(card_number))
for i in dealer:
    if i == "K" or i == "Q" or i == "J":
        dtotal += 10
    elif i == "A":
        dtotal += 11
    else:
        dtotal += i
if dtotal < 18:
    dealer.append(r.choice(card_number))
    dtotal = 0
    for i in dealer:
        if i == "K" or i == "Q" or i == "J":
            dtotal += 10
        elif i == "A":
            dtotal += 11
        else:
            dtotal += i
print(total)
if dtotal > 21:
    print("the dealer busts, you win!")
else:
    pass

if total > 21:
    print("Bust! You lost")
else:
    pass


