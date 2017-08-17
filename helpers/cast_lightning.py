# function to cast lightning
import variables as var
from helpers.closest_monster import closest_monster
from helpers.message import message


def cast_lightning():
    # find closest enemy (inside max range) and damage it
    monster = closest_monster(var.LIGHTNING_RANGE)
    if monster is None:
        message('No enemy is close enough to strike.', 'red')
        return 'cancelled'
    # zap it!
    message('A lightning bolt strikes the ' + monster.name + ' with booming thunder! The damage is '
            + str(var.LIGHTNING_DAMAGE) + ' hit points.', 'light blue')
    monster.fighter.take_damage(var.LIGHTNING_DAMAGE)
