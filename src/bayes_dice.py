import random

class BayesDice:
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        self.die = None

    def choose_die(self):
        self.die = random.choice(self.dice)
        return self.die

    def roll_die(self):
        roll = random.choice(range(1, self.dice + 1))
        posterior = (bayes_theorem(roll))
        return posterior

    def bayes_theorem(self, roll):
        posterior = (1/self.die) * .2 / (prob_of_roll(self.die))
        return posterior

    def prob_of_roll(self, roll):
        valid_dice = [die for die in self.dice if roll <= die]
        print(valid_dice)
