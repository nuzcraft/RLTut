# send object to the back of the objects list
import variables as var


def send_to_back(entity):
    var.entities.remove(entity)
    var.entities.insert(0, entity)
