# function to render everything
import libtcodpy as lib
from bearlibterminal import terminal
import variables as var


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

    # draw all objects in the list
    for entity in var.entities:
        entity.draw()

    # show the players stats
    terminal.color(terminal.color_from_name('white'))
    terminal.bkcolor(terminal.color_from_name('black'))
    terminal.printf(1, var.SCREEN_HEIGHT - 2, 'HP: ' + str(var.player.fighter.hp) +
                    '/' + str(var.player.fighter.max_hp))

