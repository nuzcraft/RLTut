import libtcodpy as lib

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

lib.console_set_custom_font('arial10x10.png', lib.FONT_TYPE_GRAYSCALE | lib.FONT_LAYOUT_TCOD)

lib.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)

lib.sys_set_fps(LIMIT_FPS)

while not lib.console_is_window_closed():
    lib.console_set_default_foreground(0, lib.white)
    lib.console_put_char(0, 1, 1, '@', lib.BKGND_NONE)
    lib.console_flush()