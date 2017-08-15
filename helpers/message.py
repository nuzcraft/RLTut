# adds messages to the game_msg box
import textwrap
import variables as var


def message(new_msg, color='white'):
    # split the message if necessary, among multiple lines
    new_msg_lines = textwrap.wrap(new_msg, var.MSG_WIDTH)
    for line in new_msg_lines:
        # if the bugger is full, remove the first line to make room for the new one
        if len(var.game_msgs) == var.MSG_HEIGHT:
            del var.game_msgs[0]
        # add the new line as a tuple, with the text and the color
        var.game_msgs.append((line, color))
