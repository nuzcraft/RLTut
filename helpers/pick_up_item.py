import variables as var
from helpers.message import message
from helpers.get_equipped_in_slot import get_equipped_in_slot


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
        # special case: automatically equip equipment if slot is available
        equipment = item.owner.equipment
        if equipment and get_equipped_in_slot(equipment.slot) is None:
            equipment.equip()