# class for a confused monster ai
from random import randint
import helpers.variables as var
from helpers.message import message


class ConfusedMonster:
    # AI for temporarily confused monster (reverts to previous AI after a while)
    def __init__(self, old_ai, num_turns=var.CONFUSE_NUM_TURNS):
        self.old_ai = old_ai
        self.num_turns = num_turns

    def take_turn(self):
        if self.num_turns > 0: # still confused
            # move in a random direction and decrease the number of turns confused
            self.owner.move(randint(-1, 1), randint(-1, 1))
            self.num_turns -= 1
        else: # restore the previous AI (this one will be deleted because it isn't referenced anymore)
            self.owner.ai = self.old_ai
            message('The ' + self.owner.name + ' is no longer confused!', 'red')
