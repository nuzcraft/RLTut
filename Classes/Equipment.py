from helpers.message import message
from Classes.Item import Item


class Equipment:
    # an object that can be equipped, yielding bonuses.
    # automatically adds the Item component
    def __init__(self, slot):
        self.slot = slot
        self.is_equipped = False

    def toggle_equip(self): # toggle equip, unequip status
        if self.is_equipped:
            self.dequip()
        else:
            self.equip()

    def equip(self):
        # equip an object and show a message about it
        self.is_equipped = True
        message('Equipped ' + self.owner.name + ' on ' + self.slot + '.', 'light green')

    def dequip(self):
        # dequip object and show a message about it
        if not self.is_equipped: return
        self.is_equipped = False
        message('Dequipped ' + self.owner.name + ' from ' + self.slot + '.', 'light yellow')
