""""Math Dungeon v2."""

import random as r
import highscores
import sympy as sp

class Enemy:

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty * 2


class Boss:

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty + difficulty * 10



class Math:
    def __init__(self, level, q_length):
        self.level = level
        self.length = q_length
        self.q_type = self.pick_question_type(level)
        self.question_text, self.answer = self.generate_question()

    def pick_question_type(self, level):
        if level >= 5:
            allowed = ["geometry", "algebra", "graphing"]
        else:
            allowed = ["numbers", "algebra"]
        return r.choice(allowed)

    def non_zero(self, low, high):
        return r.choice([i for i in range(low, high + 1) if i != 0])

    def generate_question(self):
        if self.q_type == "numbers":
            return self.generate_numbers()
        elif self.q_type == "geometry":
            return self.generate_geometry()
        elif self.q_type == "graphing":
            return self.generate_graphing()
        elif self.q_type == "algebra":
            return self.generate_algebra()
        else:
            return self.generate_numbers()

    def generate_numbers(self):
        if self.level < 2:
            a,b = r.randint(-10, 10), r.randint(-20, 20)
            op = r.choice(["+", "-", "*"])
        else:
            a,b = r.randint(-8,25), r.randint(-34,30)
            op = r.choice(["+", "-", "*", "/"])

        return f"{a} {op} {b}", eval(f"{a}{op}{b}")

    def generate_geometry(self):
        if 2 <= self.level <= 11:
            choices = r.choice(["area", "volume", "length"])
            if choices == "area":
                a, b = r.randint(5, 10 * self.level), r.randint(7, 20 * self.level)
                return  f"Find the area of the rectangle when the length and width are {a},{b}", eval(f"{a} * {b}")
            elif choices == "volume":
                a,b,c = r.randint(5, 10 * self.level), r.randint(7, 20 * self.level), r.randint(10,30)
                return (f"Find the volume of the rectangle when the length, width and height are {a}, {b}, {c}",
                        eval(f"{a} * {b} * {c}"))
            elif choices == "length":
                a, b = r.randint(10, 20 * self.level), r.randint(1,5 + self.level)
                return (f"Find the length of the rectangle when the area is {a} and the width is {b}",
                        eval(f"{a} / {b}"))
            else:
                a, b = r.randint(5, 10), r.randint(7, 10)
                return f"Find the area of the rectangle when the length and width are {a},{b}", eval(f"{a} * {b}")
        else:
            return None


    def generate_graphing(self):
        choices = r.choice(["cubic", "quartic", "quadratic", "linear"])
        if self.level < 6:
            match choices:
                case "linear":
                    # Linear question
                    a, b = (self.non_zero(-3, 7) for _ in range(2))
                    op = r.choice(["+", "-"])
                    x = self.non_zero(-5, 5)
                    question_text = f"Find f({x}) if f(x) = {a}x {op} {b}"

                    question_text = question_text.replace("+ -", "- ")
                    question_text = question_text.replace("- -", "+ ")
                    answer = eval(f"({a})*({x}) {op} ({b})")
                    return question_text, answer
                case "quadratic":
                    # Quadratic question
                    a, b, c = (self.non_zero(-3, 7) for _ in range(3))
                    op, op1 = tuple(r.choice(["+", "-"]) for _ in range(2))
                    x = self.non_zero(-5, 5)
                    question_text = f"Find f({x}) if f(x) = {a}x^2 {op} {b}x {op1} {c}"

                    question_text = question_text.replace("+ -", "- ")
                    question_text = question_text.replace("- -", "+ ")
                    answer = eval(f"({a})*({x})**2 {op} ({b})*({x}) {op1} ({c})")
                    return question_text, answer
        elif self.level >= 6:
            match choices:
                case "cubic":
                    # Cubic question
                    a, b, c, d = (self.non_zero(-3, 7) for _ in range(4))
                    op, op1, op2 = tuple(r.choice(["+", "-"])for _ in range(3))
                    x = self.non_zero(-5,5)
                    question_text = f"Find f({x}) if f(x) = {a}x^3 {op} {b}x^2 {op1} {c}x {op2} {d} "

                    question_text = question_text.replace("+ -", "- ")
                    question_text = question_text.replace("- -", "+ ")
                    answer = eval(f"({a})*({x})**3 {op} ({b})*({x})**2 {op1} ({c})*({x}) {op2} ({d})")
                    return question_text, answer
                case "quartic":
                    # Quartic question
                    a, b, c, d, e = tuple(self.non_zero(-3, 7) for _ in range(5))
                    op, op1, op2, op3 = tuple(r.choice(["+", "-"]) for _ in range(4))
                    x = self.non_zero(-5, 5)
                    question_text = f"Find f({x}) if f(x) = {a}x^4 {op} {b}x^3 {op1} {c}x^2 {op2} {d}x {op3} {e} "

                    question_text = question_text.replace("+ -", "- ")
                    question_text = question_text.replace("- -", "+ ")
                    answer = eval(f"({a})*({x})**4 {op} "
                                  f"({b})*({x})**3 {op1}"
                                  f"({c})*({x})**2 {op2}"
                                  f" ({d})*({x}) {op3} {e}")
                    return question_text, answer
        else:
            return None

    def generate_algebra(self):
        x = sp.symbols('x')  # Define x as a variable
        if self.level < 3:
            # Simple linear equations: a ± x = b
            a, b = tuple(self.non_zero(-20, 20) for _ in range(2))
            op = r.choice(["+", "-"])
            question_text = f"Solve the equation and find x: {a} {op} x = {b}"
            # Build the equation using SymPy
            left_expr = a + x if op == "+" else a - x
            right_expr = b
            solution = sp.solve(sp.Eq(left_expr, right_expr), x)
            ans = float(solution[0])
            return question_text, ans
        elif 3 <= self.level < 5:
            # Linear with optional sqrt: sqrt(a) ± b = x ± c
            a = r.choice([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144])
            b, c = tuple(self.non_zero(-20, 20) for _ in range(2))
            op = r.choice(["+", "-", "*", "/"])
            # Choose randomly if sqrt is applied to left or right
            if r.choice([True, False]):
                left_expr = sp.sqrt(a) + b if op == "+" else sp.sqrt(a) - b
                right_expr = x + c if op == "+" else x - c
            else:
                left_expr = x + b if op == "+" else x - b
                right_expr = sp.sqrt(a) + c if op == "+" else sp.sqrt(a) - c
            question_text = f"Solve the equation and find x: {left_expr} = {right_expr}"
            solution = sp.solve(sp.Eq(left_expr, right_expr), x)
            ans = float(solution[0])
            return question_text, ans
        elif 5 <= self.level < 12:

            a, b, c, d = r.randint(1, 10), r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)
            op1, op2 = r.choice(["+", "-", "*", "/"]), r.choice(["+", "-", "*", "/"])

            lhs = a * x if op1 in ["*", "/"] else x
            if op1 == "+":
                lhs = lhs + b
            elif op1 == "-":
                lhs = lhs - b
            elif op1 == "*":
                lhs = lhs * b
            elif op1 == "/":
                lhs = lhs / b

            if op2 == "+":
                lhs = lhs + c
            elif op2 == "-":
                lhs = lhs - c
            elif op2 == "*":
                lhs = lhs * c
            elif op2 == "/":
                lhs = lhs / c

            rhs = d
            eq = sp.Eq(lhs, rhs)
            solution = sp.solve(eq, x)[0]

            question = f"Solve for x: {eq}"
            return question, float(solution)
        else:
            question_text = "level too high"
            ans = "none"
            return question_text, ans


def main(name):
    enemy_list = [
        Enemy("Novice", 1),
        Enemy("Apprentice", 1),
        Enemy("Beginner", 2),
        Enemy("Student", 2),
        Enemy("Learner", 3),
        Enemy("Amateur", 3),
        Enemy("Intermediate", 4),
        Enemy("Adept", 4),
        Enemy("Skilled", 5),
        Enemy("Specialist", 5),
        Enemy("Advanced", 6),
        Enemy("Tactician", 6)
    ]

    boss_list = [
        Boss("Professional", 7),
        Boss("Expert", 7),
        Boss("Veteran", 8),
        Boss("Ace", 8),
        Boss("Master", 9),
        Boss("Champion", 9),
        Boss("Conqueror", 10),
        Boss("Overlord", 10),
        Boss("Eternity", 11),
        Boss("Masochist", 11)
    ]

    print(f"\nHail, {name}! Welcome to the hallowed halls of Math Dungeon!")
    print("=== Instructions ===")
    print("1. Face enemies and mighty bosses, each of daunting intellect.")
    print("2. To vanquish an enemy, solve the riddle they conjure.")
    print("3. Your lives depends on difficulty; each blunder costs thee one.")
    print("4. Answer with precision; round to 2 decimals when needed.")
    print("5. Lose all lives and thy quest ends. Defeat all foes to claim glory!")
    print("6. May fortune favor thee, brave scholar!\n")

    start_ = input(f"Art thou ready, {name}? (y/n): ").lower()
    if start_ not in ("y", "yes"):
        print(f"Take thy time, {name}. Return when ready to prove thy might!")
        return 0

    difficulty_levels = {
        "easy": 20,
        "normal": 18,
        "hard": 11,
        "insane": 5
    }

    print("\nChoose your difficulty:")
    print("Easy, Normal, Hard, Insane")
    while True:
        difficulty_input = input("Enter difficulty: ").lower()
        if difficulty_input in difficulty_levels:
            lives = difficulty_levels[difficulty_input]
            break
        else:
            print("Invalid choice. Please select Easy, Normal, Hard, or Insane.")


    for enemy in enemy_list + boss_list:
        enemy_max_hp = enemy.hp
        print(f"\nA wild {enemy.name} of level {enemy.difficulty} appears! Prepare thyself!")

        if isinstance(enemy, Boss):
            boss_lines = [
                f"I am {enemy.name}, ruler of this realm! Solve my riddle if thou darest!",
                f"Foolish mortal, {enemy.name} stands before thee! Canst thou answer my challenge?",
                f"Tremble! {enemy.name} demands thy wits, or be vanquished!"
            ]
            print(r.choice(boss_lines))

        while enemy.hp > 0:
            question = Math(enemy.difficulty, 0)
            print(f"\nThe riddle speaks: {question.question_text}")

            # Enemy health bar
            bar_length = 20
            filled = int((enemy.hp / enemy_max_hp) * bar_length)
            health_bar = "[" + "#" * filled + "-" * (bar_length - filled) + "]"
            print(f"{enemy.name} HP: {health_bar} ({enemy.hp}/{enemy_max_hp})")

            try:
                user_answer = float(input("Thy answer: "))
                if round(user_answer, 2) == round(question.answer, 2):
                    damage = 1  # Correct answer reduces enemy HP by 1
                    enemy.hp -= damage
                    print(f"Well met! Thy answer strikes {enemy.name} for {damage} damage!")
                else:
                    lives -= 1
                    print(f"Alas! The correct answer was {round(question.answer,2)}. The {enemy.name} strikes back!")
                    print(f"Lives remaining: {lives}")

                if lives < 1:
                    print(f"\nAlas, thy journey ends here. Return stronger next time, {name}!")
                    return -1

            except ValueError:
                print("Pray, enter a valid number.")

        victory_messages = [
            f"Victory! {enemy.name} is vanquished by thy wisdom!",
            f"Thy intellect triumphs over {enemy.name}'s cunning!",
            f"A fine strike! {enemy.name} yields before thy might!"
        ]
        print(r.choice(victory_messages))

    print(f"\nHuzzah, {name}! Thou hast conquered all enemies in the Math Dungeon!")
    highscores.HighScores.save("Math Dungeon", name, lives, difficulty_input)
    highscores.HighScores.show("Math Dungeon")

    again = input("Do you want to challenge Math Dungeon again? (y/n): ").lower()
    if again in ("y", "yes"):
        main(name)
    return 1


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    main(player_name)