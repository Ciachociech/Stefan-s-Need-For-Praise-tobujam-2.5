import common.Object


class Stefan(common.Object):

    def __init__(self):
        super().__init__("StefanObject", "assets/sprites/WIP32x32.png")
        self.deference = 50
        self.sway = 50
        self.annihilation = 50
        self.satisfaction = 50
        self.position = (100, 100)

    def render(self, window, position=(0,0)):
        super().render(window, self.position + position)