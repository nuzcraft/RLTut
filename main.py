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

while var.state != 'exit':
    var.state = handle_keys()
    render_all()
    terminal.refresh()
    for entity in var.entities:
        entity.clear()
    if var.state == 'exit':
        terminal.close()
