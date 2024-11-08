import pygame as pg
import game_data_handler
import level_handler as level_handler
import render
import json
import time
import actor_registery
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
import pygame_widgets

display_win = game_data_handler.display_win
win = game_data_handler.win

clock = pg.time.Clock()
run = True
icon = pg.image.load(game_data_handler.PATH + game_data_handler.icon)
name = game_data_handler.WINDOWNAME
delta_time_old = time.time()

def main():
    pg.display.set_caption(name)
    pg.display.set_icon(icon)

    pg.init()
    
    pg.time.delay(100)

    global run
    global delta_time_old

    def level_load():
        render.render_menu = False

        #Temp variables
        level_static = pg.sprite.Group()
        level_background = pg.sprite.Group()
        level_dynamic = pg.sprite.Group()
        level_dynamic_c = pg.sprite.Group()
        level_character = pg.sprite.Group()

        #Read level json
        with open(game_data_handler.PATH + '/levels/'+ game_data_handler.selected_level + '.json') as data_file:    
            levelfile = json.load(data_file)

            #Load Settings
            level_handler.skybox = levelfile['settings']['skybox']
            level_handler.gravity = levelfile['settings']['gravity']

            #Load Actors
            for actor in levelfile['static']:
                level_static.add(getattr(actor_registery, actor['type'])(actor['location'], actor['scale']))
            for actor in levelfile['background']:
                level_background.add(getattr(actor_registery, actor['type'])(actor['location'], actor['scale']))
            for actor in levelfile['dynamic']:
                level_dynamic.add(getattr(actor_registery, actor['type'])(actor['location'], actor['scale'], actor['name'], actor['special']))
            for actor in levelfile['dynamic_c']:
                level_dynamic_c.add(getattr(actor_registery, actor['type'])(actor['location'], actor['scale'], actor['name'], actor['special']))
            for actor in levelfile['character']:
                level_character.add(getattr(actor_registery, actor['type'])(actor['location'], actor['scale'], actor['name'], actor['special']))
        
        #Set json data into level handler
        level_handler.level_static = level_static
        level_handler.level_background = level_background
        level_handler.level_dynamic = level_dynamic
        level_handler.level_dynamic_c = level_dynamic_c
        level_handler.level_character = level_character

        #Clear memory
        del level_static
        del level_background
        del level_dynamic
        del level_dynamic_c
        del level_character

        #Render level
        render.RenderStatic()

    play_button = Button(
    win,  #Surface
    100,  #X
    100,  #Y
    100,  #W
    50,  #H
    text='Play',
    fontSize=30,
    margin=20,
    inactiveColour=(150, 150, 160),
    hoverColour=(170, 170, 175),
    pressedColour=(120, 120, 125),
    radius=0,
    onClick=lambda: level_load()
    )
    exit_button = Button(
    win,  #Surface
    100,  #X
    200,  #Y
    100,  #W
    50,  #H
    text='Exit',
    fontSize=30,
    margin=20,
    inactiveColour=(150, 150, 160),
    hoverColour=(170, 170, 175),
    pressedColour=(120, 120, 125),
    radius=0,
    onClick=lambda: quit()
    )

    def quit():
        global run
        run = False
    
    level_load()
    if not game_data_handler.EDITOR: #__Main loop__
        while run:
            pg.event.pump()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            render.MainRender()

            key = pg.key.get_pressed()
            if key[pg.K_r]:
                level_load()
        
            if game_data_handler.DEBUG == True:
                print("Main tick")

            for x in level_handler.level_dynamic:
                x.tick()
            for x in level_handler.level_character:
                x.tick()

            #Delta Time
            game_data_handler.delta_time = clock.tick()/20
            print("Dynamic Actors: " + str(len(level_handler.level_dynamic) + len(level_handler.level_character) + len(level_handler.level_dynamic_c)) + "  Static Actors: " + str(len(level_handler.level_static)) + "  FPS: " + str(clock.get_fps()))
    else: #__Editor loop__
        while run:
            pg.event.pump()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            level_load()
            render.MainRender()

            #Delta Time
            game_data_handler.delta_time = clock.tick()/20
    pg.quit()


if __name__ == "__main__":
    main()

