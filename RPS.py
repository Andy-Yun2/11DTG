import random as r

choices = [1, 2, 3]
ai_options = 0
player_options = 0

rules = ["Rock(🪨) beats Scissors(✂️)",
         "Scissor(✂️) beats Paper(📄)",
         "Paper(📄) beats Rock(🪨)"]
print("----------‼️Welcome to Rock Paper Scissor‼️----------")
print("Rules:")
for i in rules:
    print(i)
print("------------------------------------------------------")

def compare_choices():
    if player_options == ai_options:
        return "Draw"
    elif player_options == 3 and ai_options == 2 :
        return "Lose"
    elif player_options == 2 and ai_options == 1:
        return "Lose"
    elif player_options == 1 and ai_options == 3:
        return "Lose"
    else:
        return "Win"

while True:
    try:
        player_options = input("Select your choice: (type 1 for 🪨)(type 2 for ✂️)(type 3 for 📄): ")
        player_options = int(player_options)
        if player_options > 3 or player_options < 0:
            raise ValueError
        break
    except ValueError:
        print("I don't see that choice 🤨")
        print("Please re-enter your choice.")
print("Your Opponent is choosing...")
ai_options = r.choice(choices)
print(f"Your opponent chose {ai_options}")
result = compare_choices()
print(f"You {result}")





