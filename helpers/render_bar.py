# render a bar (like health or experience) horizontal
from bearlibterminal import terminal


def render_bar(x, y, total_width, name, value, maximum, bar_color, back_color):
    # render a bar (HP, exp, etc.) first calculate the width of the bar
    bar_width = int(float(value) / maximum * total_width)
    # render the background
    terminal.bkcolor(back_color)
    for i in range(total_width):
        terminal.put(x + i, y, ' ')
    # now render the bar on top
    terminal.bkcolor(bar_color)
    for i in range(bar_width):
        terminal.put(x + i, y, ' ')
    # finally, some text with the values
    text = name + ': ' + str(value) + '/' + str(maximum)
    # find the offset for the text
    new_x = total_width / 2 - len(text) / 2
    terminal.color('white')
    terminal.bkcolor(terminal.color_from_name('transparent'))
    terminal.printf(new_x, y, text)


