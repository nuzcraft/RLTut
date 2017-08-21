# main game loop
from bearlibterminal import terminal
from helpers.new_game import new_game
from helpers.play_game import play_game

terminal.open()

new_game()
play_game()
