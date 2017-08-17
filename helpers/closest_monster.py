# function to find the closest monster
import variables as var
from helpers.is_in_FOV import is_in_fov


def closest_monster(max_range):
    # find closest enemy, up to a max range, and in the player's fov
    closest_enemy = None
    closest_dist = max_range + 1 # start with (slightly more than) max range
    for ent in var.entities:
        if ent.fighter and not ent == var.player and is_in_fov(ent.x, ent.y):
            # calculate the distance between this object and the player
            dist = var.player.distance_to(ent)
            if dist < closest_dist: # its closer, so remember it
                closest_enemy = ent
                closest_dist = dist
    return closest_enemy

