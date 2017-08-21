# function to save the game to a 'savegame' file
import shelve
import variables as var


def save_game():
    # open a new empty shelve (possibly overwriting an old one) to write the game data
    file = shelve.open('savegame', 'n')
    file['map'] = var.map
    file['entities'] = var.entities
    file['player_index'] = var.entities.index(var.player)
    file['inventory'] = var.inventory
    file['game_msgs'] = var.game_msgs
    file['game_state'] = var.game_state
    file.close
