# checks if the location is blocked, returns true or false
import variables as var


def is_explored(x, y):
    # first test the map tile
    if var.map[x][y].explored:
        return True
    else:
        return False
