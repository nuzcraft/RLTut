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

inventory = []
INVENTORY_WIDTH = 50

HEAL_AMOUNT = 40

LIGHTNING_DAMAGE = 40
LIGHTNING_RANGE = 5

CONFUSE_NUM_TURNS = 10
CONFUSE_RANGE = 8

FIREBALL_RADIUS = 3
FIREBALL_DAMAGE = 25

# experience and level-ups
LEVEL_UP_BASE = 200
LEVEL_UP_FACTOR = 150
LEVEL_SCREEN_WIDTH = 40

# character screen
CHARACTER_SCREEN_WIDTH = 30

# Entities
fighter_component = None
player = None
stairs = None
entities = None
dungeon_level = None

# map stuff
map = None

fov_map = None
fov_recompute = True

# bsp map stuff
DEPTH = 10
MIN_SIZE = 5
FULL_ROOMS = False

game_state = 'playing'
player_action = None

# options
old_school_tiles = False


