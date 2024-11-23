import pygame

import common.Scene
import drawable


class Upgrades(common.Scene):

    def __init__(self, window, statistics):
        super().__init__("UpgradesScene", window)
        self.is_closing_window = False
        self.animation_frames = 0
        self.statistics = statistics
        # text related things
        self.font = drawable.Font("OptionsFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 28)
        self.upgrades_title = "upgrades shop"
        self.currency_title = "poops: 0"

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if keyboard_input[pygame.K_ESCAPE] or keyboard_input[pygame.K_x]:
            self.is_closing_window = True

    def update(self):
        self.currency_title = "poops: " + str(self.statistics.currency)

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

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        frame_shift = 4 * self.animation_frames / 2 - 200

        # frame background
        pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (60, frame_shift, 600, 200))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),(60, frame_shift, 600, 200), width=8)

        # text rendering
        self.font.render_text(self.window.window, self.upgrades_title, color, (80, frame_shift + 20), "topleft")
        self.font.render_text(self.window.window, self.currency_title, color, (640, frame_shift + 20), "topright")