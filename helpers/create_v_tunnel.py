# create a vertical tunnel
import variables as var


def create_v_tunnel(y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        var.map[x][y].blocked = False
        var.map[x][y].block_sight = False
