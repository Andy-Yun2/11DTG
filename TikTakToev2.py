"""Tic-Tac-Toe Game (TOE)."""

import random

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


def character_selection():
    """Ask player to choose their character."""
    while True:
        temp = input("What character do you want to be? ")
        if len(temp) == 1:
            return temp
        print("Please choose only one character.")


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
        game_mode = input("What mode do you want to play? (first/last) ").lower()
        if game_mode not in ["first", "last"]:
            print("Invalid Mode.")
            continue
        return game_mode


def play_mode(mod, player, level, enemy_char, score):
    """Run the game loop for the chosen mode."""
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


def game_loop():
    """Initialize a single game round."""
    global board
    board = [" "] * 9
    score = 0

    gm_mode = mode()
    level = selection()
    player = character_selection()

    enemy_char = choose_enemy_char(player)
    print(f"Your Opponent will be: {enemy_char}")

    return play_mode(gm_mode, player, level, enemy_char, score)


def main():
    """This is the main game loop."""
    score = 0
    while True:
        score += game_loop()
        print(f"Your Score: {score}")
        repeat = input("Play again? y/n ")
        if repeat.lower() != "y":
            return "Thank You for Playing."


main()
