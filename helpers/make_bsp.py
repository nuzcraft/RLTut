import variables as var
import libtcodpy as lib
from Classes.Tile import Tile
from Classes.Entity import Entity
from Classes.Rect import Rect
import random
from helpers.send_to_back import send_to_back
from helpers.place_objects import place_objects
from helpers.initialize_fov import initialize_fov


def make_bsp():
    # map stuff
    var.map = [[Tile(True)
                for y in range(var.MAP_HEIGHT)]
               for x in range(var.MAP_WIDTH)]

    var.fov_map = lib.map_new(var.MAP_WIDTH, var.MAP_HEIGHT)
    var.fov_recompute = True

    # empty list for storing room coordinates
    bsp_rooms = []

    # new root node
    bsp = lib.bsp_new_with_size(0, 0, var.MAP_WIDTH, var.MAP_HEIGHT)

    # split into nodes
    lib.bsp_split_recursive(bsp, 0, var.DEPTH, var.MIN_SIZE + 1, var.MIN_SIZE + 1, 1.5, 1.5)

    # traverse the nodes and create rooms
    lib.bsp_traverse_inverted_level_order(bsp, traverse_node)

    # Random room for the stairs
    stairs_location = random.choice(bsp_rooms)
    bsp_rooms.remove(stairs_location)
    var.stairs = Entity(stairs_location[0], stairs_location[1], '<', 'stairs', 'white', always_visible=True)
    var.entities.append(var.stairs)
    send_to_back(var.stairs)

    # Random room for player start
    player_room = random.choice(bsp_rooms)
    bsp_rooms.remove(player_room)
    var.player.x = player_room[0]
    var.player.y = player_room[1]

    # add monsters and items
    for room in bsp_rooms:
        new_room = Rect(room[0], room[1], 2, 2)
        place_objects(new_room)

    initialize_fov()