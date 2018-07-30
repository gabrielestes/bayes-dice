import random
import numpy as np
class BayesDice:
    def __init__(self):
        self.dice = [4, 6, 8, 12, 20]
        self.die = 0
        prior = 0.20
        self.data = {die: prior for die in self.dice}

    def choose_die(self):
        self.die = random.choice(self.dice)
        return self.die

    def roll_die(self):
        roll = random.randint(1, self.dice + 1) # roll the die and get a random number from the die range
        update_priors(roll)
        return (bayes_theorem(roll)) # execute bayes theorem once and set to posterior, P(B|A)

    def bayes_theorem(self, roll):
        return (1/self.die) * .2 / (prob_of_roll(self.die))

    def update_priors(self, roll):
        denominator = list(map(lambda die: 0 if roll > die else (1/die) * self.data[die], self.dice)) # P(B)
        for i in range(len(self.dice)):
            die = self.dice[i]
            numerator = denominator[i]
            posterior = numerator / denomenator
            self.data[die] = posterior
            print('die:', self.die, 'roll:', roll)
            for die, prior in self.data.items():
                print("{}: {:.2f}".format(die, prior))
            print('\n')
