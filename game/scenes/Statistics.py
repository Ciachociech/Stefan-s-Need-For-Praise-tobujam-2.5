import pygame

import common.Scene


class Statistics(common.Scene):

    def __init__(self, window):
        super().__init__("StatisticsScene", window)
        self.is_closing_window = False
        self.animation_frames = 0

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if keyboard_input[pygame.K_ESCAPE] or keyboard_input[pygame.K_x]:
            self.is_closing_window = True

    def update(self):
        if self.is_closing_window:
            if self.animation_frames == 0:
                self.is_closing_window = False
                return True
            else:
                self.animation_frames -= 2
        else:
            if self.animation_frames < 120:
                self.animation_frames += 1
        return False

    def render(self, color=pygame.Color(255, 255, 255, 255)):
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 255), (60, 5 * self.animation_frames / 2 - 240, 600, 240))
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255), (60, 5 * self.animation_frames / 2 - 240, 600, 240),
                                         width=8)