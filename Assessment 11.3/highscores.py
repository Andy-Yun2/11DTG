"""Highscores. Record all gameplay stats."""


class HighScores:
    """Initialize the HighScores blueprint."""

    FILE = "all_game_highscores.txt"

    @staticmethod
    def save(game_name, player_name, score, difficulty):
        """Save a player's score for a specific game."""
        with open(HighScores.FILE, "a") as file:
            file.write(f"{game_name},{player_name},{score},{difficulty}\n")

    @staticmethod
    def show(game_name=None):
        """Display high scores, optionally filtered by game."""
        print("\n=== High Scores ===")
        try:
            with open(HighScores.FILE, "r") as file:
                lines = file.readlines()

            if not lines:
                print("No high scores yet!")
                return

            print(f"{'Game':<12} | {'Player':<10} | {'Score':<5} | {'Difficulty'}")
            print("-" * 45)
            for line in lines:
                game, name, score, difficulty = line.strip().split(",")
                if game_name is None or game == game_name:
                    print(f"{game:<12} | {name:<10} | {score:<5} | {difficulty}")
        except FileNotFoundError:
            print("No high scores yet!")
