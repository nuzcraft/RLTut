from bearlibterminal import terminal
import variables as var
from player_move_or_attack import player_move_or_attack

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
        if key == terminal.TK_ESCAPE:
            return 'exit'
    return 'didnt-take-turn'
