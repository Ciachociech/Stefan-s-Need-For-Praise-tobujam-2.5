import common.Object
import game.GameStatistics


class Stefan(common.Object):

    def __init__(self):
        super().__init__("StefanObject", "assets/sprites/WIP32x32.png")
        self.position = (360, 360)

    def render(self, window, position=(0,0)):
        super().render(window, self.position + position)