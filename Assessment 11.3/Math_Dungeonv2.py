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
        if 2 <= self.level <= 9:
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
        elif 5 <= self.level < 10:

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
    lives = 5
    enemy_list = [
        Enemy("Novice", 1),
        Enemy("Easy", 1),
        Enemy("Beginner", 2),
        Enemy("Normal", 2),
        Enemy("Learner", 3),
        Enemy("Intermediate", 3),
        Enemy("Adept", 4),
        Enemy("Skilled", 5),
        Enemy("Advanced", 5)
    ]

    boss_list = [
        Boss("Professional", 6),
        Boss("Ace", 6),
        Boss("Expert", 7),
        Boss("Legendary", 7),
        Boss("Master", 8),
        Boss("Conqueror", 8),
        Boss("Eternity", 9),
        Boss("Masochist", 9),
    ]
    print(f"\nHELLO {name}! Welcome to Math Dungeon !!!!!")
    print("=== Instructions ===")
    print("1. You will face a series of enemies and bosses, each with a difficulty level.")
    print("2. To defeat an enemy, solve the math question they present.")
    print("3. You start with 5 lives. Each wrong answer costs you 1 life.")
    print("4. Answer as accurately as possible. Make sure all the answers are rounded to 2 decimal places.")
    print("5. If you lose all your lives, the game ends. Defeat all enemies to win!")
    print("6. Have fun and challenge your math skills! :D\n")

    start_ = input(f"Ready to start {name}? (y/n): ").lower()
    if start_ not in ("y", "yes"):
        print(f"No worries {name}:) Take your time. Come back when you're ready!")
        return 0

    # Loop through all enemies and bosses
    for enemy in enemy_list + boss_list:
        print(f"\nYou encounter {enemy.name} (Level {enemy.difficulty})!")

        # Generate a math question based on the enemy's difficulty
        question = Math(enemy.difficulty, 0)
        print("Question:", question.question_text)

        if lives < 1:
            print(f"Bad luck. try again next time!")
            return -1
        try:
            user_answer = float(input("Your answer: "))
            if round(user_answer, 2) == round(question.answer, 2):
                print("Correct! You defeated the", enemy.name)

            else:
                lives -= 1
                print("Wrong! The correct answer was:", round(question.answer, 2))
                print("The", enemy.name, "Blocked your attack!")
                print(f"Your lives : {lives}")
        except ValueError:
            print("Please enter a valid number.")

    print(f"congratulations, you beat all the enemies! :D")
    highscores.HighScores.save("Math Dungeon", name, lives)
    highscores.HighScores.show("Math Dungeon")
    return 1


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    main(player_name)