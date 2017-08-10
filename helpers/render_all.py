# function to render everything
from bearlibterminal import terminal
import variables as var


def render_all():
    # draw the map first
    for y in range(var.MAP_HEIGHT):
        for x in range(var.MAP_WIDTH):
            wall = var.map[x][y].block_sight
            if wall:
                terminal.bkcolor(terminal.color_from_name('color_dark_wall'))
                terminal.put(x, y, ' ')
            else:
                terminal.bkcolor(terminal.color_from_name('color_dark_ground'))
                terminal.put(x, y, ' ')

    # draw all objects in the list
    for entity in var.entities:
        entity.draw()

