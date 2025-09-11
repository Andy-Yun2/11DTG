print("Welcome to waffle time 101")
games = ["BlackJack", "Tik Tak Toe", "Something else"]

while True:
    print("\nCollection of games: "
          "\nBlackJack"
          "\nTik Tak Toe"
          "\nSomething else")
    game = input("\nWhat game do you want to play? (Copy paste form the list above): ")
    if game not in games:
        print("Invalid, Try again")
        continue
    elif game == "BlackJack":
        import BlackJack_v2
        print("----------Welcome to the Game of BlackJack----------")
        while True:
            if __name__ == '__main__':
                BlackJack_v2.main()
            break
    elif game == "Tik Tak Toe":
        import TikTakToev2
        print("Welcome to Tik Tak Toe")
        while True:
            if __name__ == '__main__':
                TikTakToev2.main()
            break