import random


class BColor:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'


class Person:
    def __init__(self, hp, mp, atk, magic, df, items):
        self.max_hp = hp
        self.hp = hp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.max_mp = mp
        self.mp = mp
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        return self.hp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0

    def get_max_hp(self):
        return self.max_hp

    def get_max_mp(self):
        return self.max_mp

    def choose_action(self):
        print("\n" + "    " + BColor.HEADER + 'Action' + BColor.END_C)
        i = 1
        for action in self.actions:
            print('   ' + str(i) + action)
            i += 1

    def choose_magic(self):
        i = 1
        print('\n' + '   ' + BColor.HEADER + 'Magic' + BColor.END_C)
        for spell in self.magic:
            print('   ' + str(i) + '\t' + spell.name + ' cost: ' + str(spell.cost))
            i += 1

    def choose_items(self):
        i=1
        print(BColor.HEADER + 'Items' + BColor.END_C)
        for item in self.items:
            print('   ' + str(i) + '\t' + item['item'].name + ' cost: ' + item['item'].description
                  + ' X' + str(item['quantity']))
            i += 1

    def get_stats(self):
