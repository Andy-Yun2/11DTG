import TikTakToev2, BlackJack_v2, Math_Dungeonv2

print("----------Welcome to Game Compendium 101!----------")

top_score_cards = 0
top_score_wins = 0
top_score_math = 0

# Ask for player name once
player_name = input("Please enter your name: ").strip().capitalize()
if not player_name:
    player_name = "Player"
else:
    print("Nice name!")

games = ["BlackJack", "Tik Tak Toe", "Math Dungeon"]
playing = True

def show_games():
    print("\nCollection of games:")
    for g in games:
        print("-", g)

while playing:
    show_games()
    choice = input(f"\nHey {player_name}, which game do you want to play? (type 'exit' to quit): ").strip()

    if choice.lower() == "exit":
        print(f"I'll see you next time, {player_name}!")
        break

    elif choice not in games:
        print("Invalid game, please select one from the list.")

    elif choice == "BlackJack":
        result_cards = BlackJack_v2.main(player_name)
        if result_cards != 0 and top_score_cards == 0:
            top_score_cards = result_cards
    elif choice == "Tik Tak Toe":
        TikTakToev2.main(player_name)

    elif choice == "Math Dungeon":
        Math_Dungeonv2.main(player_name)
