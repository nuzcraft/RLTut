# function to show a list of options
import textwrap
from bearlibterminal import terminal
import variables as var


def menu(header, options, width):
    if len(options) > 26:
        raise ValueError('Cannot have a menu with more than 26 options.')
    header_text = textwrap.wrap(header, width)
    header_height = len(header_text)
    if header == '':
        header_height = 0
    height = len(options) + header_height

    # top left corner of menu
    x = var.SCREEN_WIDTH / 2 - width / 2
    y = var.SCREEN_HEIGHT / 2 - height / 2

    terminal.color(terminal.color_from_name('white'))
    terminal.bkcolor(terminal.color_from_name('transparent'))
    y_location = 0
    letter_index = ord('a')
    for line in header_text:
        terminal.printf(x, y + y_location, line)
        y_location += 1
    for option_text in options:
        text = '(' + chr(letter_index) + ')' + option_text
        terminal.printf(x, y + y_location, text)
        y_location += 1
        letter_index += 1
    terminal.refresh()

    key = terminal.read()

    # if key == terminal.TK_MOUSE_LEFT:
    #     (menu_x, menu_y) = (terminal.state(terminal.TK_MOUSE_X), terminal.state(terminal.TK_MOUSE_Y))
    #     # check if click is within the menu and on a choice
    #     if menu_x >= x and menu_x < x + width and menu_y >= y + header_height and menu_y < y + height - header_height:
    #         return menu_y
    #
    # if key == terminal.TK_MOUSE_RIGHT or key == terminal.TK_ESCAPE:
    #     return None # cancel if the player right-clicked or pressed escape
    if key == terminal.TK_ENTER and terminal.check(terminal.TK_ALT):
        # alt+enter changes fullscreen
        fullscreen = terminal.check(terminal.TK_FULLSCREEN)
        fullscreen = not fullscreen
        terminal.set('window.fullscreen=' + fullscreen)

    if terminal.check(terminal.TK_WCHAR):
        index = terminal.state(terminal.TK_WCHAR) - ord('a')
        if index >=0 and index < len(options):
            return index
        return None


    terminal.clear()
    return None

