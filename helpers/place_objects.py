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


def place_objects(room):
    # choose random number of monsters
    num_monsters = randint(0, var.MAX_ROOM_MONSTERS)

    for i in range(num_monsters):
        # choose a random spot for the monster
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)
        if randint(0, 100) < 80: # 80% chance Orc
            # create an orc
            fighter_component = Fighter(hp=10, defense=0, power=3, death_function=monster_death)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'o', 'orc', 'desaturated_green', blocks=True
                             , fighter=fighter_component, ai=ai_component)
        else:
            # create a troll
            fighter_component = Fighter(hp=16, defense=1, power=4, death_function=monster_death)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'T', 'troll', 'darker_green', blocks=True
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
            # create a healing potion
            item_component = Item(use_function=cast_heal)
            item = Entity(x, y, '!', 'healing potion', 'violet'
                          , item=item_component)
            var.entities.append(item)
            send_to_back(item) # items appear below other objects
