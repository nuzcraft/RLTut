from bearlibterminal import terminal
import variables as var
from player_move_or_attack import player_move_or_attack
from helpers.inventory_menu import inventory_menu
from helpers.next_level import next_level
from helpers.msgbox import msgbox


def handle_keys():
    # movement keys
    if terminal.has_input():
        key = terminal.read()
        if var.game_state == 'playing':
            # this section is inputs that take a turn
            if key == terminal.TK_RIGHT or key == terminal.TK_KP_6:
                # move the player right
                player_move_or_attack(1, 0)
                var.fov_recompute = True
                return
            elif key == terminal.TK_LEFT or key == terminal.TK_KP_4:
                player_move_or_attack(-1, 0)
                var.fov_recompute = True
                return
            elif key == terminal.TK_UP or key == terminal.TK_KP_8:
                player_move_or_attack(0, -1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_DOWN or key == terminal.TK_KP_2:
                player_move_or_attack(0, 1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_HOME or key == terminal.TK_KP_7:
                # move the player up-left
                player_move_or_attack(-1, -1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_PAGEUP or key == terminal.TK_KP_9:
                player_move_or_attack(1, -1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_END or key == terminal.TK_KP_1:
                player_move_or_attack(-1, 1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_PAGEDOWN or key == terminal.TK_KP_3:
                player_move_or_attack(1, 1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_KP_5:
                var.fov_recompute = True
                return # do nothing
            elif key == terminal.TK_G:
                # pick up an item
                for ent in var.entities: # look for an item at the players tile
                    if ent.x == var.player.x and ent.y == var.player.y and ent.item:
                        ent.item.pick_up()
                        break
            elif key == terminal.TK_I:
                # show the inventory
                chosen_item = inventory_menu('Press the key next to an item to use it, or any other to cancel. \n')
                if chosen_item is not None:
                    chosen_item.use()
            elif key == terminal.TK_D:
                # show the inventory, if an item is selected, drop it
                chosen_item = inventory_menu('Press the key next to an item to drop it, or any other to cancel.\n')
                if chosen_item is not None:
                    chosen_item.drop()
        if key == terminal.TK_C:
            # show character info
            level_up_xp = var.LEVEL_UP_BASE + var.player.level * var.LEVEL_UP_FACTOR
            msgbox('Character Information\n\nLevel: ' + str(var.player.level) + '\nExperience: '
                   + str(var.player.fighter.xp) + '\nExperience to level up: ' + str(level_up_xp) + '\n\nMaximum HP: '
                   + str(var.player.fighter.max_hp) + '\nAttack: ' + str(var.player.fighter.power) + '\nDefense: '
                   + str(var.player.fighter.defense), var.CHARACTER_SCREEN_WIDTH)
        if key == terminal.TK_COMMA and terminal.check(terminal.TK_SHIFT):
            # go down stairs if the player is on them
            if var.stairs.x == var.player.x and var.stairs.y == var.player.y:
                next_level()
        if key == terminal.TK_ENTER and terminal.check(terminal.TK_ALT):
            # alt+enter swaps fullscreen
            fullscreen = terminal.check(terminal.TK_FULLSCREEN)
            fullscreen = not fullscreen
            terminal.set('window.fullscreen=' + fullscreen)
        if key == terminal.TK_ESCAPE or key == terminal.TK_CLOSE:
            return 'exit'
    return 'didnt-take-turn'
