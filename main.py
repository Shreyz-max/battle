from classes.game import Person
from classes.game import BColor
from classes.magic import Spell
from classes.inventory import Item

print('\n\n')


# Create black magic
fire = Spell('Fire', 10, 100, 'Black')
thunder = Spell('Thunder', 10, 100, 'Black')
blizzard = Spell('Blizzard', 10, 100, 'Black')
meteor = Spell('Meteor', 20, 200, 'Black')
quake = Spell('Quake', 14, 140, 'Black')

# Create white magic
cure = Spell('Cure', 10, 100, 'White')
heal = Spell('Heal', 10, 100, 'White')

# Inventory items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hi_elixir = Item("MegaElixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, heal]
player_items = [{"item": potion, "quantity": 15}, {"item": hi_potion, "quantity": 5},
                {"item": super_potion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": hi_elixir, "quantity": 2}, {"item": grenade, "quantity": 5}]
player = Person(460, 60, 65, player_spells, 34, player_items)
enemy = Person(1800, 60, 65, [], 25, [])
x = player.generate_damage()
print(x)

running = 1
while running:
    print("======================")

    print("\n\n")
    print("NAME                 HP                                     MP")
    player.choose_action()
    choice = int(input('Choose action'))
    index = choice-1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for ', str(dmg), 'damage points. ' + 'Enemy HP: ', enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input('\nChoose magic spell')) - 1
        if magic_choice == -1:
            continue
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_magic_damage()

        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(BColor.FAIL + "\nYou do not have enough magic points" + BColor.END_C)
            continue
        else:
            player.reduce_mp(spell.cost)
            if spell.type == 'white':
                player.heal(spell.dmg)
                print('You healed for ', str(spell.dmg), ' points')
            else:
                enemy.take_damage(magic_dmg)
            print('\nYou used magic for ', str(magic_dmg), 'damage points costing you  ' + str(player.get_mp()) + 'cost points.')
    elif index == 2:
        player.choose_items()
        item_choice = int(input('Choose item: ')) - 1
        if item_choice == -1:
            continue
        item = player.items[item_choice]['item']
        if player.items[item_choice]['quantity'] == 0:
            print(BColor.FAIL + 'You do not have enough' + player_items[item_choice]['item'])
            continue
        player.items[item_choice]['quantity'] -= 1
        if item.type == 'potion':
            player.heal(item.prop)
        if item.type == 'elixir':
            player.mp = player.max_mp
            player.hp = player.max_hp

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('\nEnemy attacked for ', str(enemy_dmg), 'damage points. ')
    print(BColor.FAIL + 'Enemy HP: ', enemy.get_hp())
    print(BColor.OK_GREEN + 'Your HP:', player.get_hp())
    print(BColor.OK_GREEN + 'Your MP', player.get_mp())

    if enemy.get_hp() == 0:
        print(BColor.OK_GREEN + " You win" + BColor.END_C)
        running = False
    elif player.get_hp() == 0:
        print(BColor.FAIL + " You Lose" + BColor.END_C)
        running = False