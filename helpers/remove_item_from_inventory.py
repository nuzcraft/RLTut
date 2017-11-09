import variables as var


def remove_item_from_inventory(item):
    # remove an item from inventory
    var.inventory.remove(item.owner)