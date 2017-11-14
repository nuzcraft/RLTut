# start a new game
from initialize_variables import initialize_variables
from helpers.make_map import make_map
from helpers.message import message
from helpers.initialize_fov import initialize_fov
import variables as var
from helpers.make_bsp import make_bsp


def new_game():
    # initialize variables
    initialize_variables()
    var.dungeon_level = 1
    # make_map()
    make_bsp()
    initialize_fov()
    message('Welcome stranger! Prepare to perish in the Tombs of the Ancient Kings.', 'red')

