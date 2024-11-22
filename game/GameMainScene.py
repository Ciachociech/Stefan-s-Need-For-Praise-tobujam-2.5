import pygame

import common.Scene
import game.Stefan


class GameMainScene(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)
        self.stefan = game.Stefan()


    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        pass

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.stefan.render(self.window.window, (100, 100))