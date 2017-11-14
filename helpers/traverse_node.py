import libtcodpy as lib
import variables as var
import random
from helpers.vline import vline
from helpers.vline_up import vline_up
from helpers.vline_down import vline_down
from helpers.hline import hline
from helpers.hline_left import hline_left
from helpers.hline_right import hline_right


def traverse_node(node, dat):
    # create rooms
    if lib.bsp_is_leaf(node):
        minx = node.x + 1
        maxx = node.x + node.w - 1
        miny = node.y + 1
        maxy = node.y + node.h - 1

        if maxx == var.MAP_WIDTH - 1:
            maxx -= 1
        if maxy == var.MAP_HEIGHT - 1:
            maxy -= 1

        # if its false, the room sizes are random, else the rooms are filled to the node's size
        if var.FULL_ROOMS == False:
            minx = random.randint(minx, maxx - var.MIN_SIZE + 2)
            miny = random.randint(miny, maxy - var.MIN_SIZE + 2)
            maxx = random.randint(minx + var.MIN_SIZE - 2, maxx)
            maxy = random.randint(miny + var.MIN_SIZE - 2, maxy)

        node.x = minx
        node.y = miny
        node.w = maxx - minx + 1
        node.h = maxy - miny + 1

        # Dig room
        for x in range(minx, maxx + 1):
            for y in range(miny, maxy + 1):
                var.map[x][y].blocked = False
                var.map[x][y].block_sight = False

        # add center coordinates to the list of rooms
        var.bsp_rooms.append(((minx + maxx) / 2, (miny + maxy) / 2))

    # create corridors
    else:
        left = lib.bsp_left(node)
        right = lib.bsp_right(node)
        node.x = min(left.x, right.x)
        node.y = min(left.y, right.y)
        node.w = max(left.x + left.w, right.x + right.w) - node.x
        node.h = max(left.y + left.h, right.y + right.h) - node.y
        if node.horizontal:
            if left.x + left.w - 1 < right.x or right.x + right.w - 1 < left.x:
                x1 = random.randint(left.x, left.x + left.w - 1)
                x2 = random.randint(right.x, right.x + right.w - 1)
                y = random.randint(left.y + left.h, right.y)
                vline_up(var.map, x1, y - 1)
                hline(var.map, x1, y, x2)
                vline_down(var.map, x2, y + 1)
            else:
                minx = max(left.x, right.x)
                maxx = min(left.x + left.w - 1, right.x + right.w - 1)
                x = random.randint(minx, maxx)
                # catch out of bounds attempts
                while x > var.MAP_WIDTH - 1:
                    x -= 1
                vline_down(var.map, x, right.y)
                vline_up(var.map, x, right.y - 1)
        else:
            if left.y + left.h - 1 < right.y or right.y + right.h - 1 < left.y:
                y1 = random.randint(left.y, left.y + left.h - 1)
                y2 = random.randint(right.y, right.y + right.h - 1)
                x = random.randint(left.x + left.w, right.x)
                hline_left(var.map, x - 1, y1)
                vline(var.map, x, y1, y2)
                hline_right(var.map, x + 1, y2)
            else:
                miny = max(left.y, right.y)
                maxy = min(left.y + left.h - 1, right.y + right.h - 1)
                y = random.randint(miny, maxy)

                # catch out of bounds attempts
                while y > var.MAP_HEIGHT - 1:
                    y -= 1
                hline_left(var.map, right.x - 1, y)
                hline_right(var.map, right.x, y)
    return True