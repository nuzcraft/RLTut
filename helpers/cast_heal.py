# function that heals the player
import variables as var
from helpers.message import message


def cast_heal():
    # heal the player
    if var.player.fighter.hp == var.player.fighter.max_hp:
        message('You are already at full health.', 'red')
        return 'cancelled'
    message('Your wounds start to feel better!', 'light violet')
    var.player.fighter.heal(var.HEAL_AMOUNT)

