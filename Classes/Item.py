# class for items
import helpers.variables as var
from helpers.message import message


class Item:
    # an item that can be picked up and used
    def __init__(self, use_function=None):
        self.use_function = use_function

    def pick_up(self):
        # add to the player's inventory and remove from the map
        if len(var.inventory) >= 26:
            message('Your inventory is full, cannot pick up '
                    + self.owner.name + '.', 'red')
        else:
            var.inventory.append(self.owner)
            var.entities.remove(self.owner)
            message('You picked up a ' + self.owner.name
                    + '!', 'green')

    def use(self):
        # just call the "use_function" if defined
        if self.use_function is None:
            message('The ' + self.owner.name + ' cannot be used.')
        else:
            if self.use_function() != 'cancelled':
                var.inventory.remove(self.owner) # destroy after use, unless cancelled

    def drop(self):
        # add to the map and remove from the player's inventory. Also, place it at the player's coordinates
        var.entities.append(self.owner)
        var.inventory.remove(self.owner)
        self.owner.x = var.player.x
        self.owner.y = var.player.y
        message('You dropped a ' + self.owner.name + '.', 'yellow')
