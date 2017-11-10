from bearlibterminal import terminal
import variables as var
from helpers.menu import menu


def options():
    choice = menu('OPTIONS', ['Old School Tiles ' + str(var.old_school_tiles),'Return to Main Menu'], 24)
    if choice == 0:
        var.old_school_tiles = not var.old_school_tiles
        terminal.clear()
        options()
    elif choice == 1:
        terminal.clear()

