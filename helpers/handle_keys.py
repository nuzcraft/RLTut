from bearlibterminal import terminal
import variables as var


def handle_keys():
    # movement keys
    if terminal.has_input():
        key = terminal.read()
        # this section is inputs that take a turn
        if key == terminal.TK_RIGHT:
            # move the player right
            var.playerx += 1
            return 'moving'
        elif key == terminal.TK_LEFT:
            var.playerx -= 1
            return 'moving'
        elif key == terminal.TK_UP:
            var.playery -= 1
            return 'moving'
        elif key == terminal.TK_DOWN:
            var.playery += 1
            return 'moving'
        if key == terminal.TK_ESCAPE:
            return 'exit'
