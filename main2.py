from bearlibterminal import terminal

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

playerx = SCREEN_WIDTH / 2
playery = SCREEN_HEIGHT / 2

state = 'idle'

def handle_keys():
    global playerx, playery
    # movement keys
    if terminal.has_input():
        key = terminal.read()
        # this section is inputs that take a turn
        if key == terminal.TK_RIGHT:
            # move the player right
            playerx += 1
            return 'moving'
        elif key == terminal.TK_LEFT:
            playerx -= 1
            return 'moving'
        elif key == terminal.TK_UP:
            playery -= 1
            return 'moving'
        elif key == terminal.TK_DOWN:
            playery += 1
            return 'moving'
        if key == terminal.TK_ESCAPE:
            return 'exit'

terminal.open()
# terminal.printf(1, 1, 'Hello, world!')
# terminal.refresh()

while state != 'exit':
    terminal.color(terminal.color_from_name('white'))
    state = handle_keys()
    terminal.put(playerx, playery, '@')
    terminal.refresh()
    terminal.put(playerx, playery, ' ')
    if state == 'exit':
        terminal.close()
