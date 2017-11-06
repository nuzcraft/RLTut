from random import randint


def random_choice_index(chances):
    # the dice will land on some number between 1 and shte sum of the chances
    dice = randint(0, sum(chances))
    # go through all chances keeping the sum so far
    running_sum = 0
    choice = 0
    for entry in chances:
        running_sum += entry
        # see if the dice landed in the part that corresponds to this choice
        if dice <= running_sum:
            return choice
        choice += 1
