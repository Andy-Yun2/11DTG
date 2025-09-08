
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
    difficulty = input("Choose your difficulty: (Easy, Medium, Hard): ").capitalize()
    if difficulty == "Easy":
        return "Easy"
    elif difficulty == "Medium":
        return "Medium"
    elif difficulty == "Hard":
        return "Hard"
    else:
        return "Invalid"

def enemy_easy():
    pass
def enemy_medium():
    pass
def enemy_hard():
    pass


def game_loop():
    while True:
        level = selection()
        if level == "Invalid":
            continue
        print_board()








game_loop()