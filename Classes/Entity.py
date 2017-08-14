# entity class file
import libtcodpy as lib
from bearlibterminal import terminal
from helpers.is_blocked import is_blocked
from helpers.is_in_FOV import is_in_fov


class Entity:
    # this is a generic object: the player, a monster, an item, the stairs...
    # it is always represented by a character on screen
    def __init__(self, x, y, char, name, color, blocks=False):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.blocks = blocks

    def move(self, dx, dy):
        # move by the given amount
        if not is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def draw(self):
        # only draw if in FOV
        if is_in_fov(self.x, self.y):
            # get the background color
            bkcolor = terminal.pick_bkcolor(self.x, self.y)
            terminal.bkcolor(bkcolor)
            # set the color and then draw the character that represents this object at its position
            terminal.color(terminal.color_from_name(self.color))
            terminal.put(self.x, self.y, self.char)

    def clear(self):
        # erase the character that represents this object
        bkcolor = terminal.pick_bkcolor(self.x, self.y)
        terminal.bkcolor(bkcolor)
        terminal.put(self.x, self.y, ' ')
