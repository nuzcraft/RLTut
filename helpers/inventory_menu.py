# function to show the inventory
import variables as var
from helpers.menu import menu


def inventory_menu(header):
    # show a menu with each item of the inventory as an option
    if len(var.inventory) == 0:
        options = ['Inventory is empty.']
    else:
        options = [item.name for item in var.inventory]
    index = menu(header, options, var.INVENTORY_WIDTH)
    # if an item was chosen, return it
    if index is None or len(var.inventory) == 0:
        return None
    return var.inventory[index].item
