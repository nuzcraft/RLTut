# function to place objects in dungeon
from random import randint
import variables as var
from is_blocked import is_blocked
from Classes.Entity import Entity
from Classes.Fighter import Fighter
from Classes.BasicMonster import BasicMonster
from Classes.Item import Item
from Classes.Equipment import Equipment
from helpers.monster_death import monster_death
from helpers.send_to_back import send_to_back
from helpers.cast_heal import cast_heal
from helpers.cast_lightning import cast_lightning
from helpers.cast_confuse import cast_confuse
from helpers.cast_fireball import cast_fireball
from helpers.random_choice import random_choice
from helpers.from_dungeon_level import from_dungeon_level


def place_objects(room):
    # set max_monsters
    max_monsters = from_dungeon_level([[2, 1], [3, 4], [5, 6]])
    # choose random number of monsters
    num_monsters = randint(0, max_monsters)

    for i in range(num_monsters):
        # choose a random spot for the monster
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)
        monster_chances = {}
        monster_chances['orc'] = 80 # orc always shows up, even if other monsters have a 0% chance
        monster_chances['troll'] = from_dungeon_level([[15, 3], [30, 5], [60, 7]])
        choice = random_choice(monster_chances)
        if choice == 'orc':
            # create an orc
            fighter_component = Fighter(hp=20, defense=0, power=4, xp=35, death_function=monster_death)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'o', 'orc', 'desaturated_green', blocks=True
                             , fighter=fighter_component, ai=ai_component, graphical_char='[0xE0A3]')
        elif choice == 'troll':
            # create a troll
            fighter_component = Fighter(hp=30, defense=2, power=8, xp=100, death_function=monster_death)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'T', 'troll', 'darker green', blocks=True
                             , fighter=fighter_component, ai=ai_component, graphical_char='[0xE0A4]')

        # only place if  the tile is not blocked
        if not is_blocked(x, y):
            var.entities.append(monster)
    max_items = from_dungeon_level([[1, 1], [2, 4]])
    num_items = randint(0, max_items)
    for i in range(num_items):
        # choose random spot for this item
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)
        # only place it if the tile is not blocked
        if not is_blocked(x, y):
            item_chances = {}
            item_chances['heal'] = 35  # healing potion always shows up
            item_chances['lightning'] = from_dungeon_level([[25, 4]])
            item_chances['fireball'] = from_dungeon_level([[25, 6]])
            item_chances['confuse'] = from_dungeon_level([[10, 2]])
            item_chances['sword'] = from_dungeon_level([[5, 4]])
            item_chances['shield'] = from_dungeon_level([[15, 8]])
            choice = random_choice(item_chances)
            if choice == 'heal':
                # create a healing potion 70%
                item_component = Item(use_function=cast_heal)
                item = Entity(x, y, '!', 'healing potion', 'violet'
                              , item=item_component, always_visible=True, graphical_char='[0xE0A6]')
            elif choice == 'lightning':
                # create a lighting bolt scroll 10%
                item_component = Item(use_function=cast_lightning)
                item = Entity(x, y, '#', 'scroll of lightning bolt', 'light yellow'
                              , item=item_component, always_visible=True, graphical_char='[0xE0A5]')
            elif choice == 'confuse':
                # create a confuse scroll (10%) chance
                item_component = Item(use_function=cast_confuse)
                item = Entity(x, y, '#', 'scroll of confusion', 'light yellow'
                              , item=item_component, always_visible=True, graphical_char='[0xE0A5]')
            elif choice == 'fireball':
                # create a fireball scroll (10%) chance
                item_component = Item(use_function=cast_fireball)
                item = Entity(x, y, '#', 'scroll of fireball', 'light yellow'
                              , item=item_component, always_visible=True, graphical_char='[0xE0A5]')
            elif choice == 'sword':
                # create a sword
                equipment_component = Equipment(slot='right hand', power_bonus=3)
                item = Entity(x, y, '/', 'sword', 'light blue'
                              , equipment=equipment_component, graphical_char='[0xE0A7]')
            elif choice == 'shield':
                # create a shield
                equipment_component = Equipment(slot='left hand', defense_bonus=1)
                item = Entity(x, y, '[', 'shield', 'darker orange'
                              , equipment=equipment_component, graphical_char='[0xE0A8]')

            var.entities.append(item)
            send_to_back(item) # items appear below other objects
