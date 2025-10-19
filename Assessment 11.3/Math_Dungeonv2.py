""""Math Dungeon v2."""

import random as r
import math as m

class Enemy:

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty * 2


    def enemy_attack(self):
        print(f"{self.name} attacks with difficulty: {self.difficulty}!")


class Boss:

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty + difficulty * 10


    def boss_attack(self):
        print("\nA GOD HAS ARRIVED! ")
        print(f"{self.name} with level {self.difficulty} has come to take your Soul!")


class Math:
    def __init__(self, level, q_length, q_type):
        self.level = level
        self.length = q_length
        self.q_type = q_type
        self.question_text, self.answer = self.generate_question()

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
        if self.level == 1:
            return self.generate_algebra()
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
        choices = r.choice(["cubic", "quartic", "quadratic"])
        if self.level > 0:
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
        reverse_op = {
            "+" : "-",
            "-" : "+",
            "*" : "/",
            "/" : "*"
        }
        if self.level < 3:
            a,b = tuple(self.non_zero(-20, 20) for _ in range(2))
            op = r.choice(["+","-"])
            ans_op = "+" if op == "-" else "-"
            question_text = f"Solve the equation and find x: {a} {op} x = {b}"
            ans = eval(f"{b} {ans_op} {a}")
            return question_text, ans
        elif 3 <= self.level < 5:
            a, b = tuple(self.non_zero(-20, 20) for _ in range(2))
            op = r.choice(["+", "-", "*", "/"])
            ans_op = reverse_op[op]
            question_text = f"Solve the equation and find x: {a} {op} x = {b}"
            ans = eval(f"{b} {ans_op} {a}")
            return question_text, ans
        elif 5 <= self.level < 10:
            a, b, c, d, e = tuple(self.non_zero(-20, 20) for _ in range(5))
            op, op1, op2 = tuple(r.choice(["+", "-", "*", "/"]) for _ in range(3) )
            ans_op, ans_op1 = reverse_op[op], reverse_op[op1]
            question_text = f"Solve the equation and find x: {a} {op} x {op1} {e} = {c} {op2} {d}"
            ans = eval(f"({c} {op2} {d}) {ans_op1} {e} {ans_op} {a}")
            return question_text, ans
        else:
            question_text = "level too high"
            ans = "none"
            return question_text, ans

enemy_list = [
    Enemy("Novice", 1),
    Enemy("Adept", 2),
    Enemy("Professional", 3),
    Enemy("Expert", 4),
    Enemy("Master", 5),
]

boss_list = [
    Boss("Ace", 6),
    Boss("Legendary", 7),
    Boss("Conqueror", 8),
    Boss("Masochist", 9),
]

print("Welcome to math dungeon :)")

# Loop through all enemies and bosses
for enemy in enemy_list + boss_list:
    print(f"\nYou encounter {enemy.name} (Level {enemy.difficulty})!")

    # Generate a math question based on the enemy's difficulty
    question = Math(enemy.difficulty, 0, r.choice(["algebra", "geometry", "graphing", "numbers"]))
    print("Question:", question.question_text)

    try:
        user_answer = float(input("Your answer: "))
        if round(user_answer, 2) == round(question.answer, 2):
            print("Correct! You defeated the", enemy.name)
        else:
            print("Wrong! The correct answer was:", round(question.answer, 2))
            print("The", enemy.name, "Blocked your attack!")
    except ValueError:
        print("Please enter a valid number.")



