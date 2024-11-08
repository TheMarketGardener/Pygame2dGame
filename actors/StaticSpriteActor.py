import pygame as pg
import os
import game_data_handler

class StaticSpriteActor(pg.sprite.Sprite):
    def __init__(self, image, default_scale, scale, default_location):
        super().__init__()
        
        if os.path.isfile(image):
            self.image = pg.transform.scale(pg.image.load(image).convert(), [(default_scale[0] * scale[0]), (default_scale[1] * scale[1])])
        else:
            self.image = pg.transform.scale(pg.image.load(game_data_handler.PATH + "/textures/misc/missing.png").convert(),
                                            [(default_scale[0] * scale[0]), (default_scale[1] * scale[1])])

        self.rect = self.image.get_rect()

        self.rect.center = default_location

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)