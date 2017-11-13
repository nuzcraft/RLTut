import helpers.variables as var
from helpers.message import message
from helpers.menu import menu


def check_level_up():
    # see if the player's experience is enough to level-up
    level_up_exp = var.LEVEL_UP_BASE + var.player.level * var.LEVEL_UP_FACTOR
    if var.player.fighter.xp >= level_up_exp:
        # it is! level up
        var.player.level += 1
        var.player.fighter.xp -= level_up_exp
        message('Your battle skills grow stronger! You reached level ' + str(var.player.level) + '!', 'yellow')
        choice = None
        while choice is None:
            # keep asking until a choice is made
            choice = menu('Level up! Choose a stat to raise:\n',
                          ['Constitution (+20 HP, from ' + str(var.player.fighter.base_max_hp) + ')',
                           'Strength (+1 attack, from ' + str(var.player.fighter.base_power) + ')',
                           'Agility (+1 defense, from ' + str(var.player.fighter.base_defense) + ')'],
                          var.LEVEL_SCREEN_WIDTH)
        if choice == 0:
            var.player.fighter.base_max_hp += 20
            var.player.fighter.hp += 20
        elif choice == 1:
            var.player.fighter.base_power += 1
        elif choice == 2:
            var.player.fighter.base_defense += 1
