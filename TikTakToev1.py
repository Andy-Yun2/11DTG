board = [" "] * 9

win = [(0,1,2), (3,4,5), (6,7,8),
       (0,3,6), (1,4,7), (2,5,8),
       (0,4,8), (2,4,6)]


def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("- + - + - ")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("- + - + -")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(player):
    for a,b,c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def game(score):
    player = "X"
    for index in range(9):
        board[index] = " "
    while True:
        print_board()
        try:
            pos = int(input(f"Player {player} What position? (1 - 9): "))
            if pos > 9 or pos < 1:
                raise ValueError
            index = pos - 1
            if board[index] != " ":
                print("That spot is taken")
                raise ValueError

            board[index] = player

            if check_win(player):
                print_board()
                print(f"Player {player} wins!")
                return score + 1
            if " " not in board:
                print_board()
                print("It is a draw")
                return score
            player = "O" if player == "X" else "X"
        except ValueError:
            print("retry")

def main_loop():
    score = 0
    count = 0
    while score >= 0:
        game(score)
        retry = input("Retry? (y/n) ")
        if retry != "y":
            break

main_loop()
