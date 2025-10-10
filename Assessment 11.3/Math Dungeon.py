"""Math Dungeon version 1."""

print("")

import random

maths_level = 1

numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 0]
random.shuffle(numbers)
operators = ["+", "-", "*", "/"]
enemies = ["Fire", "Water", "Earth", "Air", "Aether", "Guardian", "Knight", "Master", "Expert", "Professional"]
lives = 5

while enemies:
    print(f"Your lives: {lives}")
    chosen = random.choice(enemies)
    enemies.remove(chosen)

    a, b, c = random.sample(numbers, 3)

    if a == 1:
        a += b + c
        b += a - c
        c += a * b

    question = f"{a} {random.choice(operators)} {b} {random.choice(operators)} {c}"

    try:
        answer = eval(question)
    except ZeroDivisionError:
        continue

    print(f"\nYou are fighting the {chosen}! ")
    print(f"\nSolve this to damage him {question}")

    answering = True
    while answering:
        try:
            user_answer = float(input("Your answer: "))
            if user_answer - answer < 0.001:
                print("Correct")
                answering = False
            else:
                print("Wrong")
                print(f"the Correct answer was {answer}")
                lives -= 1
                answering = False
                enemies.append(chosen)
        except ValueError:
            print("That is not a number")
            continue

    if lives < 0:
        print("YOU LOST")
        break

if lives > 0:
    print("YOU WON :)")