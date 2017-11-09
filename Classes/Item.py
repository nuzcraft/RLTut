# class for items
from helpers.drop_item import drop_item
from helpers.message import message
from helpers.pick_up_item import pick_up_item
from helpers.remove_item_from_inventory import remove_item_from_inventory


class Item:
    # an item that can be picked up and used
    def __init__(self, use_function=None):
        self.use_function = use_function

    def pick_up(self):
        # add to the player's inventory and remove from the map
        pick_up_item(self)

    def use(self):
        # special case: if the object has the Equipment component, the "use"
        # action is to equip/dequip
        if self.owner.equipment:
            self.owner.equipment.toggle_equip()
            return
        # just call the "use_function" if defined
        if self.use_function is None:
            message('The ' + self.owner.name + ' cannot be used.')
        else:
            if self.use_function() != 'cancelled':
                remove_item_from_inventory(self) # destroy after use, unless cancelled

    def drop(self):
        # add to the map and remove from the player's inventory. Also, place it at the player's coordinates
        drop_item(self)
