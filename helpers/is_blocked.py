# checks if the location is blocked, returns true or false
import variables as var


def is_blocked(x, y):
    # first test the map tile
    if var.map[x][y].blocked:
        return True
    # now check for any blocking objects
    for entity in var.entities:
        if entity.blocks and entity.x == x and entity.y == y:
            return True
    return False
