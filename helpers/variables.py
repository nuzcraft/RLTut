# global variables
from bearlibterminal import terminal
from Classes.Entity import Entity
from Classes.Tile import Tile

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 45

state = 'idle'

# Entities
player = Entity(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, '@', 'white')
npc = Entity(SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2, '@', 'yellow')
entities = [npc, player]

# map stuff
map = [[Tile(False)
        for y in range(MAP_HEIGHT)]
       for x in range(MAP_WIDTH)]

