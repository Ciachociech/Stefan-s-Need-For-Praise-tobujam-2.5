import pygame


class Scene:
    def __init__(self, tag, window):
        self.tag = tag
        self.window = window

    # TODO: add input parameters
    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        pass

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        pass
