# function to get the names under the mouse
from bearlibterminal import terminal
import variables as var
from is_in_FOV import is_in_fov


def get_names_under_mouse():
    (x, y) = (terminal.state(terminal.TK_MOUSE_X), terminal.state(terminal.TK_MOUSE_Y))
    print (x, y)
    names = [ent.name for ent in var.entities
             if ent.x == x and ent.y == y and is_in_fov(ent.x, ent.y)]
    names = ', '.join(names) # join the names, separated by commas
    return names.capitalize()

