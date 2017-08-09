# global variables
from bearlibterminal import terminal
from Classes.Entity import Entity

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

state = 'idle'

# colors
white = terminal.color_from_name('white')

# Entities
player = Entity(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, '@', white)
