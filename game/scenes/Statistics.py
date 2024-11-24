import pygame

import common.Scene


def get_color_by_value_below_100(value):
    if value <= 20:
        return pygame.Color(255, 0, 0, 255)
    elif value <= 40:
        return pygame.Color(255, 127, 0, 255)
    elif value <= 60:
        return pygame.Color(255, 255, 0, 255)
    elif value <= 80:
        return pygame.Color(127, 255, 0, 255)
    else:
        return pygame.Color(0, 255, 0, 255)

def get_color_by_value_over_100(value):
    if value <= 150:
        return pygame.Color(0, 127, 127, 255)
    else:
        return pygame.Color(0, 0, 255, 255)

def get_fill_bar_length_by_value_below_100(value):
    if value <= 50:
        return 0.8 * value
    elif value <= 100:
        return 40 + 2.4 * (value - 50)
    else:
        return 160

def get_fill_bar_length_by_value_over_100(value):
    if value <= 100:
        return 0
    else:
        return 1.6 * (value - 100)

class Statistics(common.Scene):

    def __init__(self, window, statistics):
        super().__init__("StatisticsScene", window)
        self.is_closing_window = False
        self.animation_frames = 0
        self.statistics = statistics

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if keyboard_input[pygame.K_ESCAPE] or keyboard_input[pygame.K_x]:
            self.is_closing_window = True

    def update(self):
        if self.is_closing_window:
            if self.animation_frames <= 0:
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

        # frame background
        pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (60, frame_shift, 600, 200))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),(60, frame_shift, 600, 200), width=8)

        # needs bars (fill)
        pygame.draw.rect(self.window.window, get_color_by_value_below_100(self.statistics.attention),
                                         (180, frame_shift + 35, get_fill_bar_length_by_value_below_100(self.statistics.attention), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_over_100(self.statistics.attention),
                                         (180, frame_shift + 35, get_fill_bar_length_by_value_over_100(self.statistics.attention), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_below_100(self.statistics.power),
                                         (180, frame_shift + 119, get_fill_bar_length_by_value_below_100(self.statistics.power), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_over_100(self.statistics.power),
                                         (180, frame_shift + 119, get_fill_bar_length_by_value_over_100(self.statistics.power), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_below_100(self.statistics.destruction),
                                         (472, frame_shift + 35, get_fill_bar_length_by_value_below_100(self.statistics.destruction), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_over_100(self.statistics.destruction),
                                         (472, frame_shift + 35, get_fill_bar_length_by_value_over_100(self.statistics.destruction), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_below_100(self.statistics.satisfaction),
                                         (472, frame_shift + 119, get_fill_bar_length_by_value_below_100(self.statistics.satisfaction), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, get_color_by_value_over_100(self.statistics.satisfaction),
                                         (472, frame_shift + 119, get_fill_bar_length_by_value_over_100(self.statistics.satisfaction), 40),
                                         border_top_right_radius=12, border_bottom_right_radius=12)

        # needs bars (frames)
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (180, frame_shift + 35, 160, 40), width=4, border_top_right_radius=12,
                                         border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (180, frame_shift + 119, 160, 40), width=4, border_top_right_radius=12,
                                         border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (472, frame_shift + 35, 160, 40), width=4, border_top_right_radius=12,
                                         border_bottom_right_radius=12)
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (472, frame_shift + 119, 160, 40), width=4, border_top_right_radius=12,
                                         border_bottom_right_radius=12)

        # TODO: replace with icons
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (92, frame_shift + 23, 64, 64))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (92, frame_shift + 107, 64, 64))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (384, frame_shift + 23, 64, 64))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                         (384, frame_shift + 107, 64, 64))
