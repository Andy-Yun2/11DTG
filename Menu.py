print("Welcome to waffle time 101")
print("Collection of games: "
      "\nBlackJack"
      "\nTik Tak Toe"
      "\nSomething else")

games = ["BlackJack", "Tik Tak Toe", "Something else"]
while True:
    game = input("\nWhat game do you want to play? (Copy paste form the list above): ")
    if game not in games:
        print("Invalid, Try again")
        continue
    elif game == "BlackJack":
        import BlackJack_v2
        return_ = 0
        print("----------Welcome to the Game of BlackJack----------")
        while return_ != 100:
            if __name__ == '__main__':
                BlackJack_v2.main()
            return_ = input("Do you want to return to main menu? (y/n) ")
            if return_ != "n":
                break
            continue
    elif game == "Tik Tak Toe":
        import TikTakToev1
        print(--------------------"Welcome to Tik Tak Toe--------------------")
        return_ = 0
        while return_ != 100:
            if __name__ == '__main__':
                TikTakToev1.game()
            return_ = input("Do you want to return to main menu? (y/n) ")
            if return_ != "n":
                break
            continue