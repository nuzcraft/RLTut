import variables as var
from helpers.message import message


def drop_item(item):
    # special case: if the object has the Equipment component, dequip it before dropping
    if item.owner.equipment:
        item.owner.equipment.dequip()
    # put an item on the floor
    var.entities.append(item.owner)
    var.inventory.remove(item.owner)
    item.owner.x = var.player.x
    item.owner.y = var.player.y
    message('You dropped a ' + item.owner.name + '.', 'yellow')