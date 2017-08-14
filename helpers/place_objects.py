# function to place objects in dungeon
from random import randint
import variables as var
from is_blocked import is_blocked
from Classes.Entity import Entity


def place_objects(room):
    # choose random number of monsters
    num_monsters = randint(0, var.MAX_ROOM_MONSTERS)

    for i in range(num_monsters):
        # choose a random spot for the monster
        x = randint(room.x1, room.x2)
        y = randint(room.y1, room.y2)
        if randint(0, 100) < 80: # 80% chance Orc
            # create an orc
            monster = Entity(x, y, 'o', 'orc', 'desaturated_green', blocks=True)
        else:
            # create a troll
            monster = Entity(x, y, 'T', 'troll', 'darker_green', blocks=True)

        # only place if  the tile is not blocked
        if not is_blocked(x, y):
            var.entities.append(monster)