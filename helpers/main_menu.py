# function to handle the main menu
from bearlibterminal import terminal
import variables as var
from helpers.menu import menu
from helpers.new_game import new_game
from helpers.play_game import play_game


def main_menu():
    quit = False
    # function to handle the main menu
    while not quit:
        # show the game's title and some credits
        terminal.color(terminal.color_from_name('light yellow'))
        terminal.bkcolor(terminal.color_from_name('transparent'))
        title = 'TOMBS OF THE ANCIENT KINGS'
        terminal.printf(var.SCREEN_WIDTH / 2 - len(title) / 2 - 1, var.SCREEN_HEIGHT / 2 - 4, title)
        credits = 'By Nuzcraft'
        terminal.printf(var.SCREEN_WIDTH / 2 - len(credits) / 2 - 1, var.SCREEN_HEIGHT - 2, credits)
        # show options and wait for the player's choice
        choice = menu('', ['Play a new game', 'Continue last game', 'Quit'], 24)

        if choice == 0:  # new game
            new_game()
            play_game()
            terminal.clear()
        elif choice == 2:  # quit
            quit = True



