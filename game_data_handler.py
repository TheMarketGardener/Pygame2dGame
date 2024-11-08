import os
import pygame as pg

#__Modes__
#Debug mode
DEBUG = False
#Editor mode
EDITOR = False


#Game world size
WIDTH = 1920
HEIGHT = 1080
game_world_size_ratio = WIDTH / HEIGHT
game_world_size_ratio_i = HEIGHT / WIDTH
#Misc
WINDOWNAME = "Engineer simulator"
PATH = os.path.abspath(__file__)[:-20]

#Icon
if DEBUG:
  icon = "/textures/misc/logo_debug.png"
elif EDITOR:
    icon = "/textures/misc/logo_editor.png"
else:
     icon = "/textures/misc/logo.png"

#Level
selected_level = "level"

#Delta and frame time
frame_time = 0.0
delta_time = 1.0

#Display and surfaces
display_win = pg.display
win = pg.Surface
static_win = pg.Surface


