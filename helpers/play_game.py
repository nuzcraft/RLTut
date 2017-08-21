# main game loop
import variables as var
from helpers.handle_keys import handle_keys
from bearlibterminal import terminal
from helpers.render_all import render_all


def play_game():
    # main game loop
    while var.player_action != 'exit':
        var.player_action = handle_keys()
        # let the monsters take their turn
        if var.game_state == 'playing' and var.player_action != 'didnt-take-turn':
            for entity in var.entities:
                if entity.ai:
                    entity.ai.take_turn()
        terminal.clear()
        render_all()
        terminal.refresh()
        if var.player_action == 'exit':
            terminal.close()