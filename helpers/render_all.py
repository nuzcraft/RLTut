# function to render everything
import libtcodpy as lib
from bearlibterminal import terminal
import variables as var
from helpers.render_bar import render_bar
from helpers.get_names_under_mouse import get_names_under_mouse


def render_all():
    # check if we need to recompute the fov
    if var.fov_recompute:
        # recompute the fov if needed (the player moved or something)
        var.fov_recompute = False
        lib.map_compute_fov(var.fov_map, var.player.x, var.player.y, var.TORCH_RADIUS, var.FOV_LIGHT_WALLS, var.FOV_ALGO)
    # draw the map first
    for y in range(var.MAP_HEIGHT):
        for x in range(var.MAP_WIDTH):
            visible = lib.map_is_in_fov(var.fov_map, x, y)
            wall = var.map[x][y].block_sight
            if not visible:
                # its out of the players FOV
                if var.map[x][y].explored:
                    # if its been seen before
                    if wall:
                        terminal.bkcolor(terminal.color_from_name('color_dark_wall'))
                        terminal.put(x, y, ' ')
                    else:
                        terminal.bkcolor(terminal.color_from_name('color_dark_ground'))
                        terminal.put(x, y, ' ')
            else:
                # it's visible
                var.map[x][y].explored = True
                if wall:
                    terminal.bkcolor(terminal.color_from_name('color_light_wall'))
                    terminal.put(x, y, ' ')
                else:
                    terminal.bkcolor(terminal.color_from_name('color_light_ground'))
                    terminal.put(x, y, ' ')

    # draw all objects in the list, player last
    for entity in var.entities:
        if entity != var.player:
            entity.draw()
    var.player.draw()

    # show the players stats
    render_bar(1, var.PANEL_Y + 1, var.BAR_WIDTH, 'HP', var.player.fighter.hp
               , var.player.fighter.max_hp, 'light red', 'darker red')

    # print the game messages
    y = var.PANEL_Y
    for (line, color) in var.game_msgs:
        terminal.color(terminal.color_from_name(color))
        terminal.bkcolor(terminal.color_from_name('transparent'))
        terminal.printf(var.MSG_X, y, line)
        y += 1

    # print the names of entities under the mouse
    terminal.color(terminal.color_from_name('light grey'))
    terminal.bkcolor(terminal.color_from_name('transparent'))
    terminal.printf(1, var.PANEL_Y, get_names_under_mouse())
