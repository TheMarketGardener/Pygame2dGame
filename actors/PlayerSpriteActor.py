import pygame as pg
import level_handler
import game_data_handler
from actors import LivingSpriteActor
from actors import StaticSpriteActor
import render

class PlayerSpriteActor(LivingSpriteActor.LivingSpriteActor):
    def __init__(self, image, default_scale, scale, default_location, name, special):
        super().__init__(image, default_scale, scale, default_location, name, 30)
        self.special = special
        self.delay = 0
        self.vel = 1

    def tick(self):
        if game_data_handler.DEBUG == True:
            print(self.name + " tick")

        key = pg.key.get_pressed()

        if key[pg.K_f] and self.delay >= 120:
            level_handler.level_static.add(StaticSpriteActor.StaticSpriteActor(game_data_handler.PATH + "/textures/static/metal_box.png", [40.0, 40.0], [2.0, 1.0], [self.x, self.y + 62]))
            render.RenderStatic()
            self.delay = 0

        self.delay += 1

        if key[pg.K_a] and not key[pg.K_d]:
            self.xvel -= (self.vel - min(max(self.xvel, self.vel), self.vel * -1)) * game_data_handler.delta_time
            self.apply_friction = False

        if key[pg.K_d] and not key[pg.K_a]:
            self.xvel += (self.vel - min(max(self.xvel, self.vel), self.vel * -1)) * game_data_handler.delta_time
            self.apply_friction = False

        if not key[pg.K_a] and not key[pg.K_d]:
            self.apply_friction = True

        if not self.falling:
            if key[pg.K_SPACE]:
                self.falling = True
                self.yvel = -18

        #Run physics from LivingSpriteActor
        super().tick()

