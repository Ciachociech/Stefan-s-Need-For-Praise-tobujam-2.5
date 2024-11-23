import common.Object


class Indicator(common.Object):

    def __init__(self, tag):
        super().__init__(tag, "assets/sprites/WIP32x32.png")
        self.position = (360, 650)


    def render(self, window, position=(0, 0)):
        super().render(window, (self.position[0] + position[0] - 16, self.position[1] + position[1] - 16))