# function to target a specific monster
from helpers.target_tile import target_tile
import variables as var


def target_monster(max_range = None):
    # returns a clicked monster inside FOV up to a range, or Non if right-clicked
    while True:
        (x, y) = target_tile(max_range)
        if x is None: # player cancelled
            return None

        # return the first clicked monster, otherwise continue looping
        for ent in var.entities:
            if ent.x == x and ent.y == y and ent.fighter and ent != var.player:
                return ent
