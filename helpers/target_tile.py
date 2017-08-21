# function to target a tile within a range
from bearlibterminal import terminal
from helpers.render_all import render_all
from helpers.is_in_FOV import is_in_fov
import variables as var


def target_tile(max_range=None):
    # return the position of a tile left-clicked in player's FOV
    # optionally in a rnage, or None, None
    while True:
        # render the screen, this erases the inventory
        terminal.clear()
        render_all()
        terminal.refresh()
        mouse = terminal.read()
        (x, y) = (terminal.state(terminal.TK_MOUSE_X), terminal.state(terminal.TK_MOUSE_Y))
        if mouse == terminal.TK_MOUSE_LEFT and is_in_fov(x, y) and \
                (max_range is None or var.player.distance(x, y) <= max_range):
            return (x, y)
        if mouse == terminal.TK_MOUSE_RIGHT or mouse == terminal.TK_ESCAPE:
            return (None, None)
