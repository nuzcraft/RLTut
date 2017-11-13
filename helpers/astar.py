import variables as var
import libtcodpy as lib


def astar(source, target):
    # create a FOV map that has the dimensions of the map
    fov = lib.map_new(var.MAP_WIDTH, var.MAP_HEIGHT)

    # scan the current map each turn and set all walls as unwalkable
    for y1 in range(var.MAP_HEIGHT):
        for x1 in range(var.MAP_WIDTH):
            lib.map_set_properties(fov, x1, y1, not var.map[x1][y1].block_sight, not var.map[x1][y1].blocked)

    # scan all objects to see if there are objects that must be navigated around
    # check also that the object isn't self or the target (start and end points are free)
    # the ai class handles the situation if self is next to the target, so it will not use this A* function anyway
    for ent in var.entities:
        if ent.blocks and ent != var.player and ent != target:
            # set the tile as a wall so it must be navigated around
            lib.map_set_properties(fov, ent.x, ent.y, True, False)
    # allocate the A* path
    # The 1.41 is the normal diagonal cost of moving, set to 0 if diagonals are prohibited
    my_path = lib.path_new_using_map(fov, 1.41)
    # compute the path between self's coordinates and the targets
    lib.path_compute(my_path, source.x, source.y, target.x, target.y)

    # check if the path exists, and in this case, also the path is shorter than 25 tiles
    if not lib.path_is_empty(my_path) and lib.path_size(my_path) < 25:
        # find the next coordinates in the computed full path
        (x, y) = lib.path_walk(my_path, True)
    else:
        (x, y) = (None, None)

    # delete the path
    lib.path_delete(my_path)
    return x, y