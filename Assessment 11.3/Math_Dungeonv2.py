""""Math Dungeon v2."""

import random as r
import math as m

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
        safe_math = {
            "__builtins__" : None,
            "sqrt" : m.sqrt,
            "pi" : m.pi
        }
        reverse_op = {
            "+" : "-",
            "-" : "+",
            "*" : "/",
            "/" : "*",
            "**" : "sqrt",
            "sqrt" : "**"
        }
        if self.level < 3:
            a,b = tuple(self.non_zero(-20, 20) for _ in range(2))
            op = r.choice(["+","-"])
            ans_op = reverse_op[op]
            question_text = f"Solve the equation and find x: {a} {op} x = {b}"
            if op == "-":
                ans = eval(f"{a} {op} {b}")
            else:
                ans = eval(f"{b} {ans_op} {a}")
            return question_text, ans
        elif 3 <= self.level < 5:
            sec_choice = r.randint(1,100)
            if sec_choice >= 100:
                a, b = tuple(self.non_zero(-20, 20) for _ in range(2))
                op = r.choice(["+", "-", "*", "/"])
                ans_op = reverse_op[op]
                question_text = f"Solve the equation and find x: {a} {op} x = {b}"
                ans = eval(f"{b} {ans_op} {a}")
                return question_text, ans
            else:
                a = r.choice([16,25,81,100,1,4,9,36,48,64,121,144])
                b, c = tuple(self.non_zero(-20, 20) for _ in range(2))
                op = r.choice(["+", "-", "*", "/"])
                special_op = "sqrt"
                ans_op = reverse_op[op]
                question_text = f"Solve the equation and find x: {special_op}({a}) {op} {b} = x {op} {c}"
                expr = f"sqrt({a}) {op} {b} {ans_op} {c}"
                ans = eval(expr, safe_math)
                return question_text, ans

        elif 5 <= self.level < 10:
            a, b, c, d, e = tuple(self.non_zero(-20, 20) for _ in range(5))
            op, op1, op2 = tuple(r.choice(["+", "-", "*", "/"]) for _ in range(3) )
            ans_op, ans_op1 = reverse_op[op], reverse_op[op1]
            question_text = f"Solve the equation and find x: {a} {op} x {op1} {e} = {c} {op2} {d}"
            ans = eval(f"(({c} {op2} {d}) {ans_op1} {e}) {ans_op} {a}")
            return question_text, ans
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
        return "think"

    # Loop through all enemies and bosses
    for enemy in enemy_list + boss_list:
        print(f"\nYou encounter {enemy.name} (Level {enemy.difficulty})!")

        # Generate a math question based on the enemy's difficulty
        question = Math(enemy.difficulty, 0)
        print("Question:", question.question_text)

        if lives < 1:
            print(f"Bad luck {name} try again next time!")
            return -1
        try:
            user_answer = float(input("Your answer: "))
            if round(user_answer, 2) == round(question.answer, 2):
                print("Correct! You defeated the", enemy.name)

            else:
                lives -= 1
                print("Wrong! The correct answer was:", round(question.answer, 2))
                print("The", enemy.name, "Blocked your attack!")
        except ValueError:
            print("Please enter a valid number.")

    print(f"CONGRATULATIONS, {name} YOU WON! :D")
    return 0


if __name__ == "__main__":
    player_name = input("Enter your name: ")
    main(player_name)