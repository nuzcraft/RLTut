# function to cast confuse spell
import variables as var
from helpers.closest_monster import closest_monster
from helpers.message import message
from Classes.ConfusedMonster import ConfusedMonster


def cast_confuse():
    # find closest enemy in-range and confuse it
    monster = closest_monster(var.CONFUSE_RANGE)
    if monster is None:
        message('No enemy is close enough to confuse.', 'red')
    # replace the monsters AI withe a 'confused' one
    old_ai = monster.ai
    monster.ai = ConfusedMonster(old_ai)
    monster.ai.owner = monster # tell the new component who owns it
    message('The eyes of the ' + monster.name + ' look vacant, as it starts to stumble around!', 'light green')
