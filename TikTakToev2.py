import random

board = [" "] * 9
win = [[0,1,2], [3,4,5], [6,7,8],
       [0,3,6], [1,4,7], [2,5,8],
       [0,4,8], [2,4,6]]

def print_board():
    print("┌───┬───┬───┐")
    for i in range(3):
        print(f"│ {board[i*3]} │ {board[i*3+1]} │ {board[i*3+2]} │")
        if i < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")

def check_win(player):
    for a, b, c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def selection():
    while True:
        difficulty = input("Choose your difficulty: (Easy, Medium or Impossible): ").capitalize()
        if difficulty in ["Easy", "Medium", "Impossible"]:
            return difficulty
        print("Invalid choice! Try again.")

def character_selection():
    while True:
        temp = input("What character do you want to be? ")
        if len(temp) == 1:
            return temp
        print("Please choose only one character.")

def choose_enemy_char(player):
    e_chars = ["!", "@", "#", "O", "X", "?", "+", "=", "-", "~", "^"]
    return random.choice([c for c in e_chars if c != player])

def enemy(level, enemy_char, player):
    print("Your opponent is choosing...")

    if level == "Easy":
        while True:
            index = random.randint(0, 8)
            if board[index] == " ":
                board[index] = enemy_char
                break
    elif level == "Medium":
        for (a,b,c) in win:
            if board[a] == board[b] == enemy_char and board[c] == " ":
                board[c] = enemy_char
                return
            if board[a] == board[c] == enemy_char and board[b] == " ":
                board[b] = enemy_char
                return
            if board[b] == board[c] == enemy_char and board[a] == " ":
                board[a] = enemy_char
                return

        for (a,b,c) in win:
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
    elif level == "Impossible":
        pass


def game_loop():
    global board
    board = [" "] * 9
    score = 0

    level = selection()
    player = character_selection()

    enemy_char = choose_enemy_char(player)
    print(f"Your Opponent will be: {enemy_char}")

    while True:
        print_board()
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

        if " " not in board:
            print_board()
            print("It's a draw!")
            return score

        enemy(level, enemy_char, player)

        if check_win(enemy_char):
            print_board()
            print("Enemy wins!")
            return score


game_loop()
