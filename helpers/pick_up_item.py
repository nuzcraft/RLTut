import variables as var
from helpers.message import message


def pick_up_item(item):
    # add to the player's inventory and remove from the map
    if len(var.inventory) >= 26:
        message('Your inventory is full, cannot pick up '
                + item.owner.name + '.', 'red')
    else:
        var.inventory.append(item.owner)
        var.entities.remove(item.owner)
        message('You picked up a ' + item.owner.name
                + '!', 'green')