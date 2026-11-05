# ordered dic redux

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))



print("Rolling a 6-sided die:")
die = Die()

for roll in range(10):
    die.roll_die()



print("\nRolling a 10-sided die:")
die = Die(10)

for roll in range(10):
    die.roll_die()