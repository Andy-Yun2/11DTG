import TikTakToev2, BlackJack_v2, Math_Dungeonv2, highscores

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

    highscores.HighScores.show()

    choice = input(f"\nHey {player_name}, which game do you want to play? (type 'exit' to quit): ").strip()

    if choice.lower() == "exit":
        print(f"I'll see you next time, {player_name}!")
        break

    elif choice not in games:
        print("Invalid game, please select one from the list.")

    elif choice == "BlackJack":
        if BlackJack_v2.main(player_name) == 0:
            print("\nHaven't decided yet?")
        else:
            print("\nWelcome back! Wanna try something else?")

    elif choice == "Tik Tak Toe":
        if TikTakToev2.main(player_name) == 0:
            print("\nHaven't decided yet?")
        else:
            print("\nWelcome back! Wanna try something else?")

    elif choice == "Math Dungeon":
        if Math_Dungeonv2.main(player_name) == 0:
            print("\nHaven't decided yet?")
        else:
            print("\nWelcome back! Wanna try something else?")

