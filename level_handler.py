import pygame as pg

skybox = "/textures/skybox/.png"

level_character = pg.sprite.Group()

level_static = pg.sprite.Group()
level_background = pg.sprite.Group()
level_dynamic = pg.sprite.Group()
level_dynamic_c = pg.sprite.Group()


#Gravity (Default 1)
gravity = 1