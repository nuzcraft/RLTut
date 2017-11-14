# draws a vertical line down on a map
import variables as var


def vline_down(map, x, y):
    while y < var.MAP_HEIGHT and map[x][y].blocked:
        map[x][y].blocked = False
        map[x][y].block_sight = False
        y += 1
