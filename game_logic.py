import random

class RockPaperScissors:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]
        self.rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.options)

    def get_winner(self, user, computer):
        if user == computer:
            return "tie"
        elif self.rules[user] == computer:
            return "user"
        else:
            return "computer"

    def update_score(self, winner):
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1
