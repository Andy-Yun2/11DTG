"""Tic-Tac-Toe Game (TOE)."""

import random
import highscores

board = [" "] * 9
win = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def print_board():
    """Print the current game board."""
    print("┌───┬───┬───┐")
    for i in range(3):
        print(f"│ {board[i * 3]} │ {board[i * 3 + 1]} │ {board[i * 3 + 2]} │")
        if i < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")


def check_win(player):
    """Check if the given player has won."""
    for a, b, c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def check_terminal_state(player, e_char):
    """Check if the game has reached a terminal state."""
    if check_win(player):
        return player
    if check_win(e_char):
        return e_char
    if " " not in board:
        return "Draw"
    return None


def minimax(is_maximising, player, e_char):
    """Minimax algorithm for enemy moves."""
    state = check_terminal_state(player, e_char)
    if state == player:
        return -1
    if state == e_char:
        return 1
    if state == "Draw":
        return 0

    if is_maximising:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = e_char
                score = minimax(False, player, e_char)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = player
            score = minimax(True, player, e_char)
            board[i] = " "
            best_score = min(best_score, score)
    return best_score


def selection():
    """Ask player to select difficulty."""
    while True:
        difficulty = input(
            "Choose your difficulty: (Easy, Medium, Impossible or Nightmare): "
        ).capitalize()
        if difficulty in ["Easy", "Medium", "Impossible", "Nightmare"]:
            return difficulty
        print("Invalid choice! Try again.")


def character_selection(exclude=None):
    """Ask player to choose their character, optionally excluding one."""
    while True:
        temp = input("What character do you want to be? ")
        if len(temp) != 1:
            print("Please choose only one character.")
            continue
        if exclude and temp == exclude:
            print("That character is already taken! Choose another one.")
            continue
        return temp


def choose_enemy_char(player):
    """Randomly choose an enemy character different from player."""
    e_chars = ["!", "@", "#", "O", "X", "?", "+", "=", "-", "~", "^"]
    return random.choice([c for c in e_chars if c != player])


def enemy(level, enemy_char, player):
    """Enemy makes a move depending on difficulty level."""
    print("Your opponent is choosing...")

    if level == "Easy":
        while True:
            index = random.randint(0, 8)
            if board[index] == " ":
                board[index] = enemy_char
                break

    elif level == "Medium":
        for (a, b, c) in win:
            if board[a] == board[b] == enemy_char and board[c] == " ":
                board[c] = enemy_char
                return
            if board[a] == board[c] == enemy_char and board[b] == " ":
                board[b] = enemy_char
                return
            if board[b] == board[c] == enemy_char and board[a] == " ":
                board[a] = enemy_char
                return

        for (a, b, c) in win:
            if board[a] == board[b] == player and board[c] == " ":
                board[c] = enemy_char
                return
            if board[a] == board[c] == player and board[b] == " ":
                board[b] = enemy_char
                return
            if board[b] == board[c] == player and board[a] == " ":
                board[a] = enemy_char
                return

        for i in range(9):
            if board[i] == " ":
                board[i] = enemy_char
                return

    elif level in ["Impossible", "Nightmare"]:
        best_score = -float("inf")
        best_moves = []
        for i in range(9):
            if board[i] == " ":
                board[i] = enemy_char
                score = minimax(False, player, enemy_char)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_moves = [i]
                elif score == best_score:
                    best_moves.append(i)
        move = random.choice(best_moves)
        board[move] = enemy_char


def mode():
    """Ask player which mode to play."""
    while True:
        game_mode = input("Game mode? (first/last/duo) ").lower()
        if game_mode not in ["first", "last", "duo"]:
            print("Invalid Mode.")
            continue
        return game_mode


def play_mode(mod, player, level, enemy_char, score):
    """Run the game loop for the chosen mode."""
    if mod != "duo":
        turn = "player" if mod == "first" else "enemy"

        while True:
            if level != "Nightmare":
                print_board()

            if turn == "player":
                try:
                    pos = int(input("What position? (1 - 9): "))
                    if pos < 1 or pos > 9:
                        print("That is an invalid spot!")
                        continue

                    index = pos - 1
                    if board[index] != " ":
                        print("That spot is taken!")
                        continue

                    board[index] = player

                    if check_win(player):
                        print_board()
                        print("You WIN!!!")
                        score += 1
                        return score

                    turn = "enemy"
                except ValueError:
                    print("Invalid :(")

            elif turn == "enemy":
                enemy(level, enemy_char, player)
                if check_win(enemy_char):
                    print_board()
                    print("Enemy wins!")
                    return score - 1
                turn = "player"

            if " " not in board:
                print_board()
                print("It's a draw!")
                return score
    else:
        turn = "player" if mod == "duo" else "other"

        while True:
            print_board()

            if turn == "player":
                try:
                    pos = int(input(f"Player:{player} What position? (1 - 9): "))
                    if pos < 1 or pos > 9:
                        print("That is an invalid spot!")
                        continue

                    index = pos - 1
                    if board[index] != " ":
                        print("That spot is taken!")
                        continue

                    board[index] = player

                    if check_win(player):
                        print_board()
                        print(f"{player} WIN!!!")
                        score += 1
                        return score

                    if " " not in board:
                        print_board()
                        print("It's a draw!")
                        return score

                    turn = "other"

                except ValueError:
                    print("Invalid :(")

            elif turn == "other":

                try:
                    pos = int(input(f"Player:{enemy_char} What position? (1 - 9): "))
                    if pos < 1 or pos > 9:
                        print("That is an invalid spot!")
                        continue

                    index = pos - 1
                    if board[index] != " ":
                        print("That spot is taken!")
                        continue

                    board[index] = enemy_char

                    if check_win(enemy_char):
                        print_board()
                        print(f"{enemy_char} WIN!!!")
                        score += 1
                        return score

                    if " " not in board:
                        print_board()
                        print("It's a draw!")
                        return score

                    turn = "player"

                except ValueError:
                    print("Invalid :(")


def game_loop():
    """Initialize a single game round."""
    global board
    board = [" "] * 9
    score = 0

    gm_mode = mode()
    player = character_selection()
    if gm_mode != "duo":
        level = selection()
        enemy_char = choose_enemy_char(player)
        print(f"Your Opponent will be: {enemy_char}")
        return play_mode(gm_mode, player, level, enemy_char, score)
    else:
        other = character_selection(exclude=player)
        return play_mode(gm_mode, player, None, other, score)


def show_instructions():
    """Presents instructions."""
    print("\n=== Tic-Tac-Toe (TOE) (Naught and Crosses) Instructions ===")
    print("1. The game is played on a 3x3 grid.")
    print("2. Each player picks a character to represent their moves.")
    print("3. Your goal: get three of your symbols in a row (horizontal, vertical, or diagonal) before your opponent.")
    print("4. Game Modes:")
    print("   - First: You go first, then the computer (or your opponent) takes turns.")
    print("   - Last: The computer (or your opponent) goes first, then you take turns.")
    print("   - Duo: Two players take turns on the same board (You can play against your friend).")
    print("5. Difficulty Levels (for computer opponent only):")
    print("   - Easy: Random moves.")
    print("   - Medium: Blocks your winning moves and tries to win.")
    print("   - Impossible: Uses Minimax algorithm; nearly impossible to beat.")
    print("   - Nightmare: Same as impossible, but You play blindfolded.")
    print("6. On your turn, choose a position from 1 to 9 as shown below:")
    print("   1 | 2 | 3")
    print("   4 | 5 | 6")
    print("   7 | 8 | 9")
    print("7. The game ends when a player or your opponent wins or the board is full (draw).")
    print("8. Keep track of your score! Wins give +1, losses give -1, draws give 0.\n")


def main(name):
    """Run the game."""
    print(f"Welcome to Tik tak toe {name}")
    show_instructions()
    start_ = input("Are you ready for this exciting game? ").lower()
    if start_ not in ("y", "yes"):
        print(f"See you later {name}")
        return 0
    print("Lets see how good you are! ")

    score = 0
    while True:
        score += game_loop()
        print(f"Your Score: {score}")
        repeat = input("Play again? y/n ").lower()
        if repeat != "y":
            print("Thank You for Playing.")
            highscores.HighScores.save("Tik Tak Toe", name, score)
            highscores.HighScores.show("Tik Tak Toe")
            return 1


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    main(player_name)
