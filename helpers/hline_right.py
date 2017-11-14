# draw a horizontal line right
import variables as var


def hline_right(map, x, y):
    while x < var.MAP_WIDTH and map[x][y].blocked:
        map[x][y].blocked = False
        map[x][y].block_sight = False
        x += 1

