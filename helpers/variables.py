# global variables
from bearlibterminal import terminal
from Classes.Entity import Entity
from Classes.Tile import Tile

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

state = 'idle'

# Entities
player = Entity(25, 23, '@', 'white')
npc = Entity(SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2, '@', 'yellow')
entities = [npc, player]

# map stuff
map = [[Tile(True)
        for y in range(MAP_HEIGHT)]
       for x in range(MAP_WIDTH)]

