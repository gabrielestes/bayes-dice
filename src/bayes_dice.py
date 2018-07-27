import random
import numpy as np
class BayesDice:
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        self.die = None

    def choose_die(self):
        self.die = random.choice(self.dice)
        return self.die

    def roll_die(self):
        roll = random.choice(range(1, self.dice + 1)) # roll the die and get a random number from the die range
        return (bayes_theorem(roll)) # execute bayes theorem once and set to posterior, P(B|A)

    def bayes_theorem(self, roll):
        return (1/self.die) * .2 / (prob_of_roll(self.die))

    def prob_of_roll(self, roll):
        valid_dice = [die for die in self.dice if roll <= die]
        each_prob = sum([1/die for die in valid_dice])/50
        options = (valid_dice.count())/50
