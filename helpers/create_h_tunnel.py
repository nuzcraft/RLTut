# create a horizontal tunnel
import variables as var


def create_h_tunnel(x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        var.map[x][y].blocked = False
        var.map[x][y].block_sight = False
