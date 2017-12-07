from bearlibterminal import terminal
import variables as var
from helpers.menu import menu


def options():
    choice = menu('OPTIONS', ['Old School Tiles   | ' + str(var.old_school_tiles)
                              , 'Graphical Tiles    | ' + str(var.graphical_tiles)
                              , 'BSP Map Generation | ' + str(var.bsp_map_gen)
                              , 'BSP Full Rooms     | ' + str(var.FULL_ROOMS)
                              , 'Return to Main Menu'], 24)
    if choice == 0:
        var.old_school_tiles = not var.old_school_tiles
        terminal.clear()
        options()
    elif choice == 1:
        var.graphical_tiles = not var.graphical_tiles
        terminal.clear()
        options()
    elif choice == 2:
        var.bsp_map_gen = not var.bsp_map_gen
        terminal.clear()
        options()
    elif choice == 3:
        var.FULL_ROOMS = not var.FULL_ROOMS
        terminal.clear()
        options()
    elif choice == 4:
        terminal.clear()

