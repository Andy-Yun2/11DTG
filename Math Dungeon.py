"""Math Dungeon version 1."""

def easy():
    pass

def math_problems(difficulty):
    if difficulty == "easy": return easy()

    return None

def prompt():
    return input("select your difficulty")

def main():
    while True:
        math_problems(prompt())


main()