# global variables
import libtcodpy as lib
from bearlibterminal import terminal
from Classes.Entity import Entity
from Classes.Tile import Tile
from Classes.Fighter import Fighter
from helpers.player_death import player_death

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 43

PANEL_HEIGHT = 7
PANEL_Y = SCREEN_HEIGHT - PANEL_HEIGHT
BAR_WIDTH = 20

MSG_X = BAR_WIDTH + 2
MSG_WIDTH = SCREEN_WIDTH - BAR_WIDTH - 2
MSG_HEIGHT = PANEL_HEIGHT - 1

# create list of game messages and colors, starts empty
game_msgs = []

ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

FOV_ALGO = 0 # default FOV algorithm
FOV_LIGHT_WALLS = True
TORCH_RADIUS = 10

MAX_ROOM_MONSTERS = 3
MAX_ROOM_ITEMS = 2

inventory = []
INVENTORY_WIDTH = 50

HEAL_AMOUNT = 4

LIGHTNING_DAMAGE = 20
LIGHTNING_RANGE = 5

CONFUSE_NUM_TURNS = 10
CONFUSE_RANGE = 8

FIREBALL_RADIUS = 3
FIREBALL_DAMAGE = 12

# Entities
fighter_component = Fighter(hp=30, defense=2, power=5, death_function=player_death)
player = Entity(25, 23, '@', 'player', 'white', blocks=True, fighter=fighter_component)
stairs = None
entities = [player]

# map stuff
map = [[Tile(True)
        for y in range(MAP_HEIGHT)]
       for x in range(MAP_WIDTH)]

fov_map = lib.map_new(MAP_WIDTH, MAP_HEIGHT)
fov_recompute = True

game_state = 'playing'
player_action = None


