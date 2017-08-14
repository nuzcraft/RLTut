# handles the player moving or attacking
import variables as var


def player_move_or_attack(dx, dy):
    # the coordinates the player is moving to/attacking
    x = var.player.x + dx
    y = var.player.y + dy

    # try to find an attackable object there
    target = None
    for entity in var.entities:
        if entity.x == x and entity.y == y:
            target = entity
            break

    # attack if target was found, move otherwise
    if target is not None:
        print 'The ' + target.name + ' laughs at your puny efforts to attack it!'
    else:
        var.player.move(dx, dy)
        var.fov_recompute = True
