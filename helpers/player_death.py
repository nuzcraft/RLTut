# function defining what happens when the player dies
import variables as var


def player_death(player):
    print 'You died!'
    var.game_state = 'dead'
    # for added affect, transform the player into a corpse!
    player.char = '%'
    player.color = 'dark red'
