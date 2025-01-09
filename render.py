import level_handler
import pygame as pg
import game_data_handler
import pygame_widgets
import os

game_data_handler.display_win = pg.display.set_mode((960, 540), pg.RESIZABLE, 8)
game_data_handler.static_win = pg.Surface((game_data_handler.WIDTH, game_data_handler.HEIGHT), pg.OPENGL, 16)
game_data_handler.win = pg.Surface((game_data_handler.WIDTH, game_data_handler.HEIGHT), pg.OPENGL, 16)
display_win = game_data_handler.display_win
static_win = game_data_handler.static_win
win = game_data_handler.win
render_menu = True


#Renders static actors and the skybox
def RenderStatic():
    global static_win

    skybox = game_data_handler.PATH + level_handler.skybox

    if os.path.isfile(skybox):
            skybox = pg.image.load(skybox).convert()
    else:
        skybox = pg.image.load(game_data_handler.PATH + "/textures/misc/missing.png").convert()

    static_win.blit(skybox, (0, 0))
    level_handler.level_background.draw(static_win)
    level_handler.level_static.draw(static_win)

#Renders dynamic actors
def MainRender():
    global win
    global static_win
    global display_win
    global render_menu

    win.blit(static_win, (0, 0))

    level_handler.level_dynamic.draw(win)
    level_handler.level_dynamic_c.draw(win)

    for i in level_handler.level_character:
         
        pg.draw.rect(win, [255, 0, 0, 50], i.rect.copy())

    level_handler.level_character.draw(win)

    win_width, win_height = display_win.get_size()

    window_aspect_ratio = win_width / win_height

    if window_aspect_ratio > game_data_handler.game_world_size_ratio:
        scaled_win = pg.transform.scale(win, (int(win_height * game_data_handler.game_world_size_ratio), win_height))
    else:
        scaled_win = pg.transform.scale(win, (win_width, int(win_width / game_data_handler.game_world_size_ratio)))

    if render_menu:
        pygame_widgets.update(scaled_win)
    display_win.blit(scaled_win, scaled_win.get_rect(center = display_win.get_rect().center))
    

    pg.display.flip()