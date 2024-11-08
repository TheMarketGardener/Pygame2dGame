from actors import DynamicSpriteActor

class Door(DynamicSpriteActor.DynamicSpriteActor):
    def __init__(self, image, default_scale, scale, default_location, name, special):
        super().__init__(image, default_scale, scale, default_location, name)
        self.name
        self.special = special

    def id(self):
        return self.special