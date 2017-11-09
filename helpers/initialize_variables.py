# function to initialize variables
from bearlibterminal import terminal
import libtcodpy as lib
import helpers.variables as var
from Classes.Tile import Tile
from Classes.Fighter import Fighter
from Classes.Entity import Entity
from helpers.player_death import player_death


def initialize_variables():

    # custom colors
    terminal.set("palette.color_dark_wall = 0,0,100")
    terminal.set("palette.color_dark_ground = 50,50,100")
    terminal.set("palette.color_light_wall = 130,110,50")
    terminal.set("palette.color_light_ground = 200,180,50")
    terminal.set('palette.desaturated_green = 63,127,63')

    # inputs
    terminal.set('input.filter = [keyboard, mouse]')

    var.game_state = 'playing'
    var.player_action = None

    # Entities
    var.fighter_component = Fighter(hp=100, defense=1, power=4, xp=0, death_function=player_death)
    var.player = Entity(25, 23, '@', 'player', 'white', blocks=True, fighter=var.fighter_component)
    var.player.level = 1
    var.entities = [var.player]

    # # map stuff
    # var.map = [[Tile(True)
    #         for y in range(var.MAP_HEIGHT)]
    #        for x in range(var.MAP_WIDTH)]
    #
    # var.fov_map = lib.map_new(var.MAP_WIDTH, var.MAP_HEIGHT)
    # var.fov_recompute = True

    # inventory
    var.inventory = []

    # game messages
    var.game_msgs = []
