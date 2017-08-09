import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

playerx = SCREEN_WIDTH / 2
playery = SCREEN_HEIGHT / 2

def handle_keys():
    global playerx, playery
    key = lib.console_wait_for_keypress(True)
    if key.vk == lib.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        lib.console_set_fullscreen(not lib.console_is_fullscreen())
    elif key.vk == lib.KEY_ESCAPE:
        # exit game
        return True

    # movement keys
    if lib.console_is_key_pressed(lib.KEY_UP):
        playery -= 1
    elif lib.console_is_key_pressed(lib.KEY_DOWN):
        playery += 1
    elif lib.console_is_key_pressed(lib.KEY_LEFT):
        playerx -= 1
    elif lib.console_is_key_pressed(lib.KEY_RIGHT):
        playerx += 1

lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GRAYSCALE | lib.FONT_LAYOUT_TCOD)

lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)

lib.sys_set_fps(LIMIT_FPS)

while not lib.console_is_window_closed():
    lib.console_set_default_foreground(0, lib.white)
    lib.console_put_char(0, playerx, playery, '@', lib.BKGND_NONE)
    lib.console_flush()
    lib.console_put_char(0, playerx, playery, ' ', lib.BKGND_NONE)
    # handle keys and exit if needed
    exit = handle_keys()
    if exit:
        break
