import libtcodpy as lib
import variables as var


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