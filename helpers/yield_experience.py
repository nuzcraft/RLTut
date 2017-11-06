import variables as var

def yield_experience(entity):
    # if not the player, yield experience to the player
    if entity.owner != var.player:
        var.player.fighter.xp += entity.xp