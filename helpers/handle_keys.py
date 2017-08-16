from bearlibterminal import terminal
import variables as var
from player_move_or_attack import player_move_or_attack
from helpers.inventory_menu import inventory_menu

def handle_keys():
    # movement keys
    if terminal.has_input():
        key = terminal.read()
        if var.game_state == 'playing':
            # this section is inputs that take a turn
            if key == terminal.TK_RIGHT:
                # move the player right
                player_move_or_attack(1, 0)
                var.fov_recompute = True
                return
            elif key == terminal.TK_LEFT:
                player_move_or_attack(-1, 0)
                var.fov_recompute = True
                return
            elif key == terminal.TK_UP:
                player_move_or_attack(0, -1)
                var.fov_recompute = True
                return
            elif key == terminal.TK_DOWN:
                player_move_or_attack(0, 1)
                var.fov_recompute = True
                return
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
        if key == terminal.TK_ESCAPE:
            return 'exit'
    return 'didnt-take-turn'
