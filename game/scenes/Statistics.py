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
        frame_shift = 4 * self.animation_frames / 2 - 200
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 255), (60, frame_shift, 600, 200))
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (60, frame_shift, 600, 200), width=8)
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (180, frame_shift + 35, 160, 40), width=4, border_radius=12)
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (180, frame_shift + 119, 160, 40), width=4, border_radius=12)
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (472, frame_shift + 35, 160, 40), width=4, border_radius=12)
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (472, frame_shift + 119, 160, 40), width=4, border_radius=12)

        # TODO: replace with icons
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (92, frame_shift + 23, 64, 64))
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (92, frame_shift + 107, 64, 64))
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (384, frame_shift + 23, 64, 64))
        frame_surface = pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (384, frame_shift + 107, 64, 64))
