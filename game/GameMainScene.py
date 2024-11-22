import pygame

import common.Scene

class GameMainScene(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)
        self.main_sprite = common.Object("main_sprite", "assets/sprites/WIP32x32.png")


    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        pass

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.main_sprite.render(self.window.window, (100, 100))
