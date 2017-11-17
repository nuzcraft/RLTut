# entity class file
from bearlibterminal import terminal
from Classes.Item import Item
from helpers.is_blocked import is_blocked
from helpers.is_in_FOV import is_in_fov
from helpers.is_explored import is_explored
from helpers.astar import astar
import math


class Entity:
    # this is a generic object: the player, a monster, an item, the stairs...
    # it is always represented by a character on screen
    def __init__(self, x, y, char, name, color, blocks=False, always_visible=False
                 , fighter=None, ai=None, item=None, equipment=None):
        self.x = x
        self.y = y
        self.char = char
        self.name = name
        self.color = color
        self.blocks = blocks
        self.always_visible = always_visible
        self.fighter = fighter
        if self.fighter: # let the fighter component know who owns it
            self.fighter.owner = self
        self.ai = ai
        if self.ai: # let the ai component know who owns it
            self.ai.owner = self
        self.item = item
        if self.item:
            self.item.owner = self
        self.equipment = equipment
        if self.equipment:
            self.equipment.owner = self
            self.item = Item()
            self.item.owner = self


    def move(self, dx, dy):
        # move by the given amount
        if not is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def draw(self):
        # only draw if in FOV
        if is_in_fov(self.x, self.y) or (self.always_visible and is_explored(self.x, self.y)):
            # get the background color
            terminal.bkcolor(terminal.color_from_name('transparent'))
            # set the color and then draw the character that represents this object at its position
            terminal.color(terminal.color_from_name(self.color))
            terminal.printf(self.x, self.y, self.char)

    def clear(self):
        # erase the character that represents this object
        terminal.bkcolor(terminal.color_from_name('transparent'))
        terminal.put(self.x, self.y, ' ')

    def move_towards(self, target_x, target_y):
        # vector from this object to the target, and distance
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # normalize it to length 1(preserving direction) then round it and
        # convert to integer so the movement is restricted to map grid
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy)

    def distance_to(self, other):
        # return the distance to another object
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def distance(self, x, y):
        # returns distance to x and y
        return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)

    def move_astar(self, target):
        # more advanced pathfinding to the target
        x, y = astar(self, target)
        if x or y:
            # set self's coordinates to the next path tile
            self.x = x
            self.y = y
        else:
            # keep the old move function as a backup
            self.move_towards(target.x, target.y)
