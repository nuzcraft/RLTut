import libtcodpy as lib
import variables as var


def is_in_fov(x, y):
    return lib.map_is_in_fov(var.fov_map, x, y)
