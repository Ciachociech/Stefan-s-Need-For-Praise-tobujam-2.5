import random

import common.Object


class Stefan():

    def __init__(self, window):
        self.window = window
        self.stefan_body = common.Object("StefanBodyObject", "assets/sprites/stefan_body.png")
        self.stefan_head = common.Object("StefanHeadObject", "assets/sprites/stefan_head.png")
        self.head_shake = (0, 0)
        self.position = (40, 40)

    def update(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            if -5 <= self.head_shake[0] + x <= 5 and -5 <= self.head_shake[1] + y <= 5:
                self.head_shake = (self.head_shake[0] + x, self.head_shake[1] + y)

    def render(self):
        self.stefan_body.render(self.window.window, self.position)
        self.stefan_head.render(self.window.window, (self.position[0] + self.head_shake[0], self.position[1] + self.head_shake[1]))