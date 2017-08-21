# initialize the FOV
from bearlibterminal import terminal
import libtcodpy as lib
import variables as var


def initialize_fov():
    terminal.clear()
    # set fov_map
    for y in range(var.MAP_HEIGHT):
        for x in range(var.MAP_WIDTH):
            lib.map_set_properties(var.fov_map, x, y, not var.map[x][y].block_sight, not var.map[x][y].blocked)

