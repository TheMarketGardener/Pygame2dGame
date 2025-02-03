import game_data_handler
from actors import StaticSpriteActor
from actors import PlayerSpriteActor
from actors import Button
from actors import Door

#_____Registered Actors For Level Loading_____

#__Static__

class WoodenBox(StaticSpriteActor.StaticSpriteActor):
    def __init__(self, default_location, scale):
        super().__init__(game_data_handler.PATH + "/textures/static/wooden_box.png", [40, 40], scale, default_location)

class Ramp(StaticSpriteActor.StaticSpriteActor):
    def __init__(self, default_location, scale):
        super().__init__(game_data_handler.PATH + "/textures/static/ramp.png", [40, 40], scale, default_location)
        
class Planks(StaticSpriteActor.StaticSpriteActor):
    def __init__(self, default_location, scale):
        super().__init__(game_data_handler.PATH + "/textures/static/planks.png", [40, 40], scale, default_location)

class MetalBox(StaticSpriteActor.StaticSpriteActor):
    def __init__(self, default_location, scale):
        super().__init__(game_data_handler.PATH + "/textures/static/metal_box.png", [40, 40], scale, default_location)

#__Dynamic__

class Button(Button.Button):
    def __init__(self, default_location, scale, name, special):
        super().__init__(game_data_handler.PATH + "/textures/dynamic/button/red.png", [40, 40], scale, default_location, name, special)

class Door(Door.Door):
    def __init__(self, default_location, scale, name, special):
        super().__init__(game_data_handler.PATH + "/textures/dynamic/door/red.png", [40, 80], scale, default_location, name, special)

#__Living__

class Player(PlayerSpriteActor.PlayerSpriteActor):
    def __init__(self, default_location, scale, name, special):
        super().__init__(game_data_handler.PATH + "/textures/dynamic/player/engi.png", [40, 80], scale, default_location, name, special)