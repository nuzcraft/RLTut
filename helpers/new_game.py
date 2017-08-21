# start a new game
import variables as var
from helpers.make_map import make_map
from helpers.message import message
from helpers.initialize_fov import initialize_fov


def new_game():
    # initialize variables
    var.initializevariables()
    make_map()
    initialize_fov()
    message('Welcome stranger! Prepare to perish in the Tombs of the Ancient Kings.', 'red')

