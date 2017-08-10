# entity class file
from bearlibterminal import terminal
from helpers.is_blocked import is_blocked


class Entity:
    # this is a generic object: the player, a monster, an item, the stairs...
    # it is always represented by a character on screen
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        # move by the given amount
        if not is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def draw(self):
        # set the color and then draw the character that represents this object at its position
        terminal.color(terminal.color_from_name(self.color))
        terminal.put(self.x, self.y, self.char)

    def clear(self):
        # erase the character that represents this object
        terminal.put(self.x, self.y, ' ')
