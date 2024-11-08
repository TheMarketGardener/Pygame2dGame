from actors import LivingSpriteActor

class TurretActor(LivingSpriteActor.LivingSpriteActor):
    def __init__(self, image, default_scale, scale, default_location, name):
        super().__init__(image, default_scale, scale, default_location, name, 20)
        self.name

    def tick(self):
        print(self.name + ": meow")


        super().tick()