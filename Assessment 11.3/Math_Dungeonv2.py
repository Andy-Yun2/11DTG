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


enemy_list = [
    Enemy("Novice", 1),
    Enemy("Adept", 2),
    Enemy("Professional", 3),
    Enemy("Expert", 4),
    Enemy("Master", 5),
]


class Boss:

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty + difficulty * 10


    def boss_attack(self):
        print("\nA GOD HAS ARRIVED! ")
        print(f"{self.name} with level {self.difficulty} has come to take your Soul!")

boss_list = [
    Boss("Ace", 6),
    Boss("Legendary", 7),
    Boss("Conqueror", 8),
    Boss("Masochist", 9),
]

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
            return None

    def generate_numbers(self):
        if self.level < 2:
            a,b = r.randint(-10, 10), r.randint(-20, 20)
            op = r.choice(["+", "-", "*"])
        else:
            a,b = r.randint(-8,25), r.randint(-34,30)
            op = r.choice(["+", "-", "*", "/"])

        return f"{a} {op} {b}", eval(f"{a}{op}{b}")

    def generate_geometry(self):
        if 5 < self.level < 9:
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
        choices = r.choice(["functions", "quartic"])
        if self.level > 8:
            match choices:
                case "functions":
                    a,b,c,d = (self.non_zero(-3, 7) for _ in range(4))
                    op, op1, op2 = tuple(r.choice(["+", "-"])for _ in range(3))
                    x = self.non_zero(-5,5)
                    question_text = f"Find f({x}) if f(x) = {a}x^3 {op} {b}x^2 {op1} {c}x {op2} {d} "

                    question_text = question_text.replace("+ -", "- ")
                    question_text = question_text.replace("- -", "+ ")
                    answer = eval(f"({a})*({x})**3 {op} ({b})*({x})**2 {op1} ({c})*({x}) {op2} ({d})")
                    return question_text, answer
                case "quartic":
                    a, b, c, d, e = tuple(self.non_zero(-3, 7) for _ in range(5))
                    op, op1, op2, op3 = tuple(r.choice(["+", "-"]) for _ in range(4))
                    x = self.non_zero(-5, 5)
                    question_text = f"Find f({x}) if f(x) = {a}x^4 {op} {b}x^3 {op1} {c}x^2 {op2} {d}x {op3} {e} "

                    question_text = question_text.replace("+ -", "- ")
                    question_text = question_text.replace("- -", "+ ")
                    answer = eval(f"({a})*({x})**4 {op} "
                                  f"({b})*({x})**3 {op1} ({c})*({x})**2 {op2} ({d})*({x}) {op3} {e}")
                    return question_text, answer

        else:
            return None

    def generate_algebra(self):
        pass



question = Math(9,0,"graphing")
print("Question: ", question.question_text)

user_answer = float(input("Your answer: "))
try:
    if round(user_answer, 2) == round(question.answer, 2):
        print("Correct")
    else:
        print("WRONG")
        print("The right answer was:", question.answer)
except ValueError:
    print("Please enter a valid number")



