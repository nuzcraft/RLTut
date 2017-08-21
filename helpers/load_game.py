# load the previously saved game
import variables as var
import shelve
from helpers.initialize_fov import initialize_fov
from helpers.initialize_variables import initialize_variables


def load_game():
    # first, initialize variables (includes custom terminal settings)
    initialize_variables()
    # open the previously saved shelve and load the game data
    file = shelve.open('savegame', 'r')
    var.map = file['map']
    var.entities = file['entities']
    var.player = var.entities[file['player_index']] # get index of player in entity list
    var.inventory = file['inventory']
    var.game_msgs = file['game_msgs']
    var.game_state = file['game_state']
    file.close()

    initialize_fov()

