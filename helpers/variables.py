# global variables
import libtcodpy as lib
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

FOV_ALGO = 0 # default FOV algorithm
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

MAX_ROOM_MONSTERS = 3

game_state = 'playing'
player_action = None

# Entities
player = Entity(25, 23, '@', 'player', 'white', blocks=True)
entities = [player]

# map stuff
map = [[Tile(True)
        for y in range(MAP_HEIGHT)]
       for x in range(MAP_WIDTH)]

fov_map = lib.map_new(MAP_WIDTH, MAP_HEIGHT)
fov_recompute = True

def initializevariables():

    # custom colors
    terminal.set("palette.color_dark_wall = 0,0,100")
    terminal.set("palette.color_dark_ground = 50,50,100")
    terminal.set("palette.color_light_wall = 130,110,50")
    terminal.set("palette.color_light_ground = 200,180,50")
    terminal.set('palette.desaturated_green = 63,127,63')
    terminal.set('palette.darker_green = 0,127,0')


