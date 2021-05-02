"""
Two fighters, one winner. (7Kyu)
https://www.codewars.com/kata/577bd8d4ae2807c64b00045b

Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Example:
class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__
"""

Flag = True


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__ = __str__


def checkHealth(fighter1, fighter2):
    global Flag
    if fighter1.health <= 0:
        Flag = False
        return fighter2.name
    if fighter2.health <= 0:
        Flag = False
        return fighter1.name


def declare_winner(fighter1, fighter2, first_attacker):

    while Flag:
        if first_attacker == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack
            checkHealth(fighter1, fighter2)
            fighter1.health -= fighter2.damage_per_attack
            checkHealth(fighter1, fighter2)
        if first_attacker == fighter2.name:
            fighter1.health -= fighter2.damage_per_attack
            checkHealth(fighter1, fighter2)
            fighter2.health -= fighter1.damage_per_attack
            checkHealth(fighter1, fighter2)

        print(str(fighter1.health) + fighter1.name + " --> " + str(fighter2.health) + " " + fighter2.name)

    return fighter1.name if fighter1.health > fighter2.health else fighter2.name


# if attacker is adam, adam attacks first, check if liam is below zero, if he is return adam as winner.
# if attacker is liam, ***

print(declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew"))
