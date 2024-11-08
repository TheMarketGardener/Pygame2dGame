from actors import LivingSpriteActor
import pygame as pg
import level_handler

class Button(LivingSpriteActor.LivingSpriteActor):
    def __init__(self, image, default_scale, scale, default_location, name, special):
        super().__init__(image, default_scale, scale, default_location, name, 20)
        self.name
        self.special = special

    def tick(self):
        hit_by = pg.sprite.spritecollide( self, level_handler.level_character, False )
        if len(hit_by) != 0:
            for x in level_handler.level_dynamic_c:
                if x.id() == self.special:
                    print(x.name)
                    x.kill()


        super().tick()