# checks if the location is blocked, returns true or false
import variables as var


def is_blocked(x, y):
    # returns true if the location is blocked
    return var.map[x][y].blocked
