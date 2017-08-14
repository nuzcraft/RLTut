# class file for Tiles


class Tile:
    # a tile of the map an its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
        self.explored = False

        # by default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked
            self.block_sight = block_sight
