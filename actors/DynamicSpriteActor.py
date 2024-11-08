import pygame as pg
import weakref
import game_data_handler
import os

class DynamicSpriteActor(pg.sprite.Sprite):
    _ticking_actor = weakref.WeakSet()
    def __init__(self, image, default_scale, scale, default_location, name):
        super().__init__()

        self.__class__.add_actor(self)
        self.name = name

        self.startx = default_location[0]
        self.starty = default_location[1]

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


    def tick(self):
        pass

    @classmethod
    def add_actor(cls, ticking_actor):
        cls._ticking_actor.add(ticking_actor)
        return ticking_actor  # Return the added actor instance

    @classmethod
    def tick_all(cls):
        for actor in cls._ticking_actor:
            actor.tick()