# function to place objects in dungeon
from random import randint
import variables as var
from is_blocked import is_blocked
from Classes.Entity import Entity
from Classes.Fighter import Fighter
from Classes.BasicMonster import BasicMonster


def place_objects(room):
    # choose random number of monsters
    num_monsters = randint(0, var.MAX_ROOM_MONSTERS)

    for i in range(num_monsters):
        # choose a random spot for the monster
        x = randint(room.x1, room.x2)
        y = randint(room.y1, room.y2)
        if randint(0, 100) < 80: # 80% chance Orc
            # create an orc
            fighter_component = Fighter(hp=10, defense=0, power=3)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'o', 'orc', 'desaturated_green', blocks=True
                             , fighter=fighter_component, ai=ai_component)
        else:
            # create a troll
            fighter_component = Fighter(hp=16, defense=1, power=4)
            ai_component = BasicMonster()
            monster = Entity(x, y, 'T', 'troll', 'darker_green', blocks=True
                             , fighter=fighter_component, ai=ai_component)

        # only place if  the tile is not blocked
        if not is_blocked(x, y):
            var.entities.append(monster)