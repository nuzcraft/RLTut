# function defining what happens when the player dies
import variables as var
from helpers.message import message


def player_death(player):
    message('You died!', 'red')
    var.game_state = 'dead'
    # for added affect, transform the player into a corpse!
    player.char = '%'
    player.color = 'dark red'
