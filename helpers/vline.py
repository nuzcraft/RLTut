# draws a vertical line on the map


def vline(map, x, y1, y2):
    if y1 > y2:
        y1,y2 = y2,y1
    for y in range(y1, y2 + 1):
        map[x][y].blocked = False
        map[y][y].block_sight = False