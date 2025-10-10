""""Math Dungeon v2."""

class Enemy:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty * 10

    def enemy_attack(self):
        print(f"{self.name} attacks with difficulty: {self.difficulty}!")

enemy_list = [
    Enemy("Novice", 1),
    Enemy("Professional", 2),
    Enemy("Expert", 3),
]


class Boss:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.hp = difficulty + difficulty * 10
    def boss_attack(self):
        print("\nA GOD HAS ARRIVED! ")
        print(f"{self.name} with level {self.difficulty} has come to take your Soul!")

