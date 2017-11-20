import variables as var


def swap_graphical_tiles():
    if var.graphical_tiles:
        var.player_char = '[0xE02C]'  # '@'
    else:
        var.player_char = '@'  # '[0xE02C]'
