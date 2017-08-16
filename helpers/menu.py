# function to show a list of options
import textwrap
from bearlibterminal import terminal
import variables as var


def menu(header, options, width):
    if len(options) > 26:
        raise ValueError('Cannot have a menu with more than 26 options.')
    header_text = textwrap.wrap(header, width)
    header_height = len(header_text)
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
    if terminal.check(terminal.TK_WCHAR):
        index = terminal.state(terminal.TK_WCHAR) - ord('a')
        if index >=0 and index < len(options):
            return index
        return None
    return None

