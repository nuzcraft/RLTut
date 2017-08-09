from bearlibterminal import terminal
from helpers.handle_keys import handle_keys
import helpers.variables as var

terminal.open()

while state != 'exit':
    terminal.color(var.white)
    state = handle_keys()
    terminal.put(var.playerx, var.playery, '@')
    terminal.refresh()
    terminal.put(var.playerx, var.playery, ' ')
    if state == 'exit':
        terminal.close()
