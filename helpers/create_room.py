# function to create a room
import variables as var


def create_room(room):
    # go through the tiles in the rectangle and make them passable
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            var.map[x][y].blocked = False
            var.map[x][y].block_sight = False

