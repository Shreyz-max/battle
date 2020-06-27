import random


class Spell:
    def __init__(self, name, cost, dmg, kind):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.kind = kind

    def generate_magic_damage(self):
        dmg_h = self.dmg + 5
        dmg_l = self.dmg - 5
        return random.randrange(dmg_l, dmg_h)
