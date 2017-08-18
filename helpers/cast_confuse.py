# function to cast confuse spell
import variables as var
from helpers.closest_monster import closest_monster
from helpers.message import message
from Classes.ConfusedMonster import ConfusedMonster
from helpers.target_monster import target_monster


def cast_confuse():
    # ask a player for a target to confuse
    message('Left-click an enemy to confuse it, or right-click to cancel.', 'light cyan')
    monster = target_monster(var.CONFUSE_RANGE)
    if monster is None:
        return 'cancelled'
    # replace the monsters AI withe a 'confused' one
    old_ai = monster.ai
    monster.ai = ConfusedMonster(old_ai)
    monster.ai.owner = monster  # tell the new component who owns it
    message('The eyes of the ' + monster.name + ' look vacant, as it starts to stumble around!', 'light green')
