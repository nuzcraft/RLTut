# function to place objects in dungeon
from random import randint
import variables as var
from is_blocked import is_blocked
from Classes.Entity import Entity
from Classes.Fighter import Fighter
from Classes.BasicMonster import BasicMonster
from Classes.Item import Item
from helpers.monster_death import monster_death
from helpers.send_to_back import send_to_back
from helpers.cast_heal import cast_heal
from helpers.cast_lightning import cast_lightning
from helpers.cast_confuse import cast_confuse
from helpers.cast_fireball import cast_fireball
from helpers.random_choice import random_choice


def place_objects(room):
    # choose random number of monsters
    num_monsters = randint(0, var.MAX_ROOM_MONSTERS)

    for i in range(num_monsters):
        # choose a random spot for the monster
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)
        choice = random_choice(var.monster_chances)
        if choice == 'orc': # 80% chance Orc
            # create an orc
            fighter_component = Fighter(hp=10, defense=0, power=3, xp=35, death_function=monster_death)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'o', 'orc', 'desaturated_green', blocks=True
                             , fighter=fighter_component, ai=ai_component)
        elif choice == 'troll':
            # create a troll
            fighter_component = Fighter(hp=16, defense=1, power=4, xp=100, death_function=monster_death)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'T', 'troll', 'darker green', blocks=True
                             , fighter=fighter_component, ai=ai_component)

        # only place if  the tile is not blocked
        if not is_blocked(x, y):
            var.entities.append(monster)

    num_items = randint(0, var.MAX_ROOM_ITEMS)
    for i in range(num_items):
        # choose random spot for this item
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)
        # only place it if the tile is not blocked
        if not is_blocked(x, y):
            choice = random_choice(var.item_chances)
            if choice == 'heal':
                # create a healing potion 70%
                item_component = Item(use_function=cast_heal)
                item = Entity(x, y, '!', 'healing potion', 'violet'
                              , item=item_component, always_visible=True)
            elif choice == 'lightning':
                # create a lighting bolt scroll 10%
                item_component = Item(use_function=cast_lightning)
                item = Entity(x, y, '#', 'scroll of lightning bolt', 'light yellow'
                              , item=item_component, always_visible=True)
            elif choice == 'confuse':
                # create a confuse scroll (10%) chance
                item_component = Item(use_function=cast_confuse)
                item = Entity(x, y, '#', 'scroll of confusion', 'light yellow'
                              , item=item_component, always_visible=True)
            elif choice == 'fireball':
                # create a fireball scroll (10%) chance
                item_component = Item(use_function=cast_fireball)
                item = Entity(x, y, '#', 'scroll of fireball', 'light yellow'
                              , item=item_component, always_visible=True)

            var.entities.append(item)
            send_to_back(item) # items appear below other objects
