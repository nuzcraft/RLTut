from helpers.message import message
from helpers.make_map import make_map
from helpers.initialize_fov import initialize_fov
import variables as var


def next_level():
    # advance to the next level
    message('You take a moment to rest and recover your strength.', 'light violet')
    var.player.fighter.heal(var.player.fighter.max_hp / 2)
    message('After a rare moment of peace, you descend deeper into the heart of the dungeon...', 'red')
    make_map()
    initialize_fov()
