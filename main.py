from bearlibterminal import terminal
from helpers.handle_keys import handle_keys
import helpers.variables as var
from helpers.render_all import render_all
from helpers.make_map import make_map

terminal.open()

# custom colors
terminal.set("palette.color_dark_wall = 0,0,100")
terminal.set("palette.color_dark_ground = 50,50,100")

while var.state != 'exit':
    var.state = handle_keys()
    make_map()
    render_all()
    terminal.refresh()
    for entity in var.entities:
        entity.clear()
    if var.state == 'exit':
        terminal.close()
