import random

class BayesDice:
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]

    def choose_die(self):
        return random.choice(self.dice)
