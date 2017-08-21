# function defining what happens when a monster dies
from helpers.send_to_back import send_to_back
from helpers.message import message


def monster_death(monster):
    # transform it into a nasty corpse! it doesn't block
    # can't be attacked and doesn't move
    message( monster.name.capitalize() + ' is dead', 'orange')
    monster.char = '%'
    monster.color = 'dark red'
    monster.blocks = False
    monster.fighter = None
    monster.ai = None
    monster.name = 'remains of ' + monster.name
    send_to_back(monster)
