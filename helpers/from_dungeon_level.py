import variables as var


def from_dungeon_level(table):
    # returns a value that depends on level.
    # The table specifies what value occurs after each level, default is 0
    for (value, level) in reversed(table):
        if var.dungeon_level >= level:
            return value
    return 0
