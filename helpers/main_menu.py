# function to handle the main menu
from bearlibterminal import terminal
import variables as var
from helpers.menu import menu
from helpers.new_game import new_game
from helpers.play_game import play_game
from helpers.load_game import load_game
from helpers.msgbox import msgbox
from helpers.options import options


def main_menu():
    quit = False
    # function to handle the main menu
    while not quit:
        # show the background
        terminal.printf(0, 0, '[0xEFFF]')
        # show the game's title and some credits
        terminal.color(terminal.color_from_name('light yellow'))
        terminal.bkcolor(terminal.color_from_name('transparent'))
        title = 'TOMBS OF THE ANCIENT KINGS'
        terminal.printf(var.SCREEN_WIDTH / 2 - len(title) / 2 - 1, var.SCREEN_HEIGHT / 2 - 4, title)
        credits = 'By Nuzcraft'
        terminal.printf(var.SCREEN_WIDTH / 2 - len(credits) / 2 - 1, var.SCREEN_HEIGHT - 2, credits)
        # show options and wait for the player's choice
        choice = menu('', ['Play a new game', 'Continue last game', 'Options', 'Quit'], 24)

        if choice == 0:  # new game
            new_game()
            play_game()
            terminal.clear()
        elif choice == 1: # load game
            try:
                load_game()
            except:
                terminal.clear()
                msgbox('\n No saved game to load. \n', 24)
                terminal.clear()
                continue
            play_game()
        elif choice == 2:  # options
            terminal.clear()
            options()
        elif choice == 3:  # quit
            quit = True



