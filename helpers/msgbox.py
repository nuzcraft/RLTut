# function that relys on the menu function to display a simple message box
from helpers.menu import menu


def msgbox(text, width=50):
    menu(text, [], width) # use menu as a sort of message box
