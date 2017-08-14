# main game loop
import libtcodpy as lib
from bearlibterminal import terminal
from helpers.handle_keys import handle_keys
import helpers.variables as var
from helpers.render_all import render_all
from helpers.make_map import make_map

terminal.open()

# initialize variables
var.initializevariables()

make_map()

# set fov_map
for y in range(var.MAP_HEIGHT):
    for x in range(var.MAP_WIDTH):
        lib.map_set_properties(var.fov_map, x, y, not var.map[x][y].block_sight, not var.map[x][y].blocked)

while var.player_action != 'exit':
    var.player_action = handle_keys()
    # let the monsters take their turn
    if var.game_state == 'playing' and var.player_action != 'didnt-take-turn':
        for entity in var.entities:
            if entity != var.player:
                print 'The ' + entity.name + ' growls!'
    render_all()
    terminal.refresh()
    for entity in var.entities:
        entity.clear()
    if var.player_action == 'exit':
        terminal.close()
