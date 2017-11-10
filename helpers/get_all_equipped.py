import variables as var


def get_all_equipped(entity):
    # returns a list of equipped items
    if entity == var.player:
        equipped_list = []
        for item in var.inventory:
            if item.equipment and item.equipment.is_equipped:
                equipped_list.append(item.equipment)
        return equipped_list
    else:
        return [] # no equipment equipped
