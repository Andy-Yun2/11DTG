
import random

board = [" "] * 9
win = [[0,1,2], [3,4,5], [6,7,8],
       [0,3,6], [1,4,7], [2,5,8],
       [0,4,8], [2,4,6],]

def print_board():
    print("┌───┬───┬───┐")
    for i in range(3):
        print(f"│ {board[i*3]} │ {board[i*3+1]} │ {board[i*3+2]} │")
        if i < 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")


def check_win(player):
    for a,b,c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def selection():
    difficulty = input("Choose your difficulty: (Easy, Medium or Hard): ").capitalize()
    if difficulty == "Easy":
        return "Easy"
    elif difficulty == "Medium":
        return "Medium"
    elif difficulty == "Hard":
        return "Hard"
    else:
        return "Invalid"

def enemy(level, ):
    choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Your opponent is choosing: ")
    if level == "Easy":
        while True:
            choice = random.choice(choices)
            index = choice - 1
            if board[index] != " ":
                choices.pop(choice)
                continue
            else:
                return board[index] =


    elif level == "Hard":
        pass
    elif level == "Medium":
        pass


def game_loop():
    score = 0
    ask = True
    letter = True
    player = ""
    level = ""

    while ask:
        level = selection()
        if level == "Invalid":
            continue
        ask = False

    while letter:
        player = input("What character do you want to be? ")
        if len(player) > 1:
            print("Too many characters")
            continue
        letter = False

    while True:
        print_board()

        pos = int(input("What position? (1 - 9) "))
        if pos > 9 or pos < 1:
            print("That is an invalid spot!")
            continue
        index = pos - 1
        if board[index] != " ":
            print("That spot is taken")
            continue

        board[index] = player

        enemy(level, player)

        if check_win(player):
            print_board()
            print("You WIN!!!")
            return score + 1

        if " " not in board:
            print_board()
            print("It is a draw")
            return score






game_loop()