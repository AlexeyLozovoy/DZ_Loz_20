import random

class Dice:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)

class Game:
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.player_score = 0
        self.player_glasses = 0
        self.computer_score = 0
        self.turn = 0

    def roll_dice(self):
        self.dice1.roll()
        self.dice2.roll()
        self.turn += 1

        if self.dice1.value > self.dice2.value:
            self.computer_score += 1
        else:
            self.player_score += 1

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.turn = 0
