# main game loop
import libtcodpy as lib
from bearlibterminal import terminal
from helpers.handle_keys import handle_keys
import helpers.variables as var
from helpers.render_all import render_all
from helpers.make_map import make_map
from helpers.message import message

from Classes.Item import Item
from helpers.cast_fireball import cast_fireball
from Classes.Entity import Entity

terminal.open()

# initialize variables
var.initializevariables()

make_map()

message('Welcome stranger! Prepare to perish in the Tombs of the Ancient Kings.', 'red')
item_component = Item(use_function=cast_fireball)
item = Entity(0, 0, '#', 'scroll of fireball', 'light yellow'
              , item=item_component)
var.entities.append(item)
item.item.pick_up()
# set fov_map
for y in range(var.MAP_HEIGHT):
    for x in range(var.MAP_WIDTH):
        lib.map_set_properties(var.fov_map, x, y, not var.map[x][y].block_sight, not var.map[x][y].blocked)

while var.player_action != 'exit':
    var.player_action = handle_keys()
    # let the monsters take their turn
    if var.game_state == 'playing' and var.player_action != 'didnt-take-turn':
        for entity in var.entities:
            if entity.ai:
                entity.ai.take_turn()
    terminal.clear()
    render_all()
    terminal.refresh()
    if var.player_action == 'exit':
        terminal.close()
