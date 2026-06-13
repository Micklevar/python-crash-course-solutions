# 9-13. Dice:
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides 

    def roll_die(self):
        number =  randint(1, self.sides)
        print(number)


first_dice = Die(10)
first_dice.roll_die()
