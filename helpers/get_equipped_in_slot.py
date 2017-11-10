import variables as var


def get_equipped_in_slot(slot):
    for ent in var.inventory:
        if ent.equipment and ent.equipment.slot == slot and ent.equipment.is_equipped:
            return ent.equipment
    return None