from bearlibterminal import terminal
import variables as var

def handle_keys():
    # movement keys
    if terminal.has_input():
        key = terminal.read()
        # this section is inputs that take a turn
        if key == terminal.TK_RIGHT:
            # move the player right
            var.player.move(1, 0)
            var.fov_recompute = True
            return 'moving'
        elif key == terminal.TK_LEFT:
            var.player.move(-1, 0)
            var.fov_recompute = True
            return 'moving'
        elif key == terminal.TK_UP:
            var.player.move(0, -1)
            var.fov_recompute = True
            return 'moving'
        elif key == terminal.TK_DOWN:
            var.player.move(0, 1)
            var.fov_recompute = True
            return 'moving'
        if key == terminal.TK_ESCAPE:
            return 'exit'
