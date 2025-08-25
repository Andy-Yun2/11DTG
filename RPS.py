import random as r

choices = [1, 2, 3]
ai_options = r.choice(choices)
player_options = 0
valid = True
while valid:
    try:
        player_options = input("Select your choice: (type 1 for 🪨)(type 2 for ✂️)(type 3 for 📄): ")
        player_options = int(player_options)
        if player_options > 3 or player_options <= 0:
            raise ValueError
        valid = False
    except ValueError:
        print("Invalid")

if player_options == ai_options:
    print("Draw")
elif player_options == 3 and ai_options == 2 :
    print("Lose")
elif player_options == 2 and ai_options == 1:
    print("Lose")
elif player_options == 1 and ai_options == 3:
    print("Lose")
else:
    print("Win")







