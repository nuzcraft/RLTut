# function to cast a fireball
from helpers.message import message
import variables as var
from helpers.target_tile import target_tile


def cast_fireball():
    # as the player for a target tile to throw a fireball at
    message('left-click a target tile for the fireball, or right-click to cancel', 'light cyan')
    (x, y) = target_tile()
    if x is None:
        return 'cancelled'
    message('The fireball explodes, burning everything within ' + str(var.FIREBALL_RADIUS)
            + ' tiles!', 'orange')
    for ent in var.entities: # damage every figter in range, including the player
        if ent.distance_to(x, y) <= var.FIREBALL_RADIUS and ent.fighter:
            message('The ' + ent.name + ' gets burned for ' + str(var.FIREBALL_DAMAGE)
                    + 'hit points.', 'orange')
            ent.fighter.take_damage(var.FIREBALL_DAMAGE)
