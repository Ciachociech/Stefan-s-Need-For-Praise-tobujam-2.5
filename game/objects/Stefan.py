import random

import pygame

import common.Object


class Stefan():

    def __init__(self, window):
        self.window = window
        self.stefan_body = common.Object("StefanBodyObject", "assets/sprites/stefan_body.png")
        self.stefan_body.img.image = pygame.transform.scale(self.stefan_body.img.image, (480, 480))
        self.stefan_head = common.Object("StefanHeadObject", "assets/sprites/stefan_head.png")
        self.stefan_head.img.image = pygame.transform.scale(self.stefan_head.img.image, (480, 480))
        self.head_shake = (0, 0)
        self.position = (120, 60)

    def update(self):
            x = random.randint(-1, 1)
            y = random.randint(-1, 1)
            if -15 <= self.head_shake[0] + x <= 15 and -15 <= self.head_shake[1] + y <= 15:
                self.head_shake = (self.head_shake[0] + x, self.head_shake[1] + y)

    def render(self):
        self.stefan_body.render(self.window.window, self.position)
        self.stefan_head.render(self.window.window, (self.position[0] + self.head_shake[0], self.position[1] + self.head_shake[1]))