import random
import math

class Character:
    def __init__(self):
        self.charisma = self.ability()
        self.constitution = self.ability()
        self.dexterity = self.ability()
        self.intelligence = self.ability()
        self.strength = self.ability()
        self.wisdom = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        roll = sorted(
            [random.randint(1,6) for _ in range(4)]
        )
        return sum(roll[1:])
    
def modifier(number):
    return math.floor((number-10)/2)