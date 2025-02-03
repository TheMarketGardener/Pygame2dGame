import pygame as pg
from actors import DynamicSpriteActor
import level_handler
import game_data_handler

class LivingSpriteActor(DynamicSpriteActor.DynamicSpriteActor):
    def __init__(self, image, default_scale, scale, default_location, name, max_speed):
        super().__init__(image, default_scale, scale, default_location, name)
        self.x = default_location[0]
        self.y = default_location[1]
        self.falling = True
        self.yvel = 0
        self.xvel = 0
        self.max_speed = max_speed
        self.apply_friction = True

    def collide(self, xvel, yvel):
        for i in pg.sprite.spritecollide(self, level_handler.level_static, False):
            if xvel > 0:
                self.rect.right = i.rect.left
                self.xvel = 0
            if xvel < 0:
                self.rect.left = i.rect.right
                self.xvel = 0
            if yvel > 0:
                self.rect.bottom = i.rect.top
                self.falling = False
                self.yvel = 0
            if yvel < 0:
                self.rect.top = i.rect.bottom
                self.yvel = 0
        for i in pg.sprite.spritecollide(self, level_handler.level_dynamic_c, False):
            if xvel > 0:
                self.rect.right = i.rect.left
                self.xvel = 0
            if xvel < 0:
                self.rect.left = i.rect.right
                self.xvel = 0
            if yvel > 0:
                self.rect.bottom = i.rect.top
                self.falling = False
                self.yvel = 0
            if yvel < 0:
                self.rect.top = i.rect.bottom
                self.yvel = 0

    def tick(self):
        if not self.xvel == 0 and self.apply_friction:
            if self.xvel < 0:
                self.xvel += 8 * game_data_handler.delta_time
                self.xvel = min(self.xvel, 0)
            else:
                self.xvel -= 8 * game_data_handler.delta_time
                self.xvel = max(self.xvel, 0)

        #Gravity
        self.yvel += level_handler.gravity * game_data_handler.delta_time

        #Global Forced Max Speed
        self.xvel = max(min(self.xvel, self.max_speed), self.max_speed * -1)
        self.yvel = max(min(self.yvel, self.max_speed), self.max_speed * -1)

        #Collision
        self.rect.left += self.xvel * game_data_handler.delta_time
        self.collide(self.xvel, 0)

        self.rect.top += self.yvel * game_data_handler.delta_time
        self.falling = True
        self.collide(0, self.yvel)

        self.rect.clamp_ip(game_data_handler.win.get_rect())
        if self.rect.bottom == game_data_handler.win.get_rect().bottom:
            self.yvel = 0
            self.falling = False

        #Set new position
        self.x, self.y = self.rect.center