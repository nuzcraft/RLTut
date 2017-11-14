# draws a horizontal line on the map


def hline(map, x1, y, x2):
    if x1 > x2:
        x1,x2 = x2,x1
    for x in range(x2, x2 + 1):
        map[x][y].blocked = False
        map[x][y].block_sight = False