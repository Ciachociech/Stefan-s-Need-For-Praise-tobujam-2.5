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
        self.font_bigger = drawable.Font("OptionsFont36")
        self.font_bigger.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 36)
        self.font_smaller = drawable.Font("OptionsFont28")
        self.font_smaller.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 20)
        self.upgrades_title = "upgrades shop"
        self.currency_title = "poops: 0"
        self.needs_description = ["Time dilation", "With increase of Stefan's power, the time is slowing down", "Decrease 2x a tempo of decaying needs", "cost: 10"]
        self.feeding_description = ["Better hay quality", "Instead of eliminate world hunger, better hay is discovered", "Feeding is 2x more effective", "cost: 10"]
        self.petting_description = ["Petting army", "Hired more followers to praising Stefan", "Petting is 2x more effective", "cost: 10"]
        self.cleaning_description = ["Poop stock market", "Stefan's poops are getting more and more valuable", "Cleaning is 2x more effective and each poop gives 2 currency", "cost: 20"]


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
        frame_shift = 11 * self.animation_frames / 2 - 620

        # frame background
        pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (60, frame_shift, 600, 620))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),(60, frame_shift, 600, 620), width=8)

        # text rendering
        self.font_bigger.render_text(self.window.window, self.upgrades_title, color, (80, frame_shift + 20),
                                     "topleft")
        self.font_bigger.render_text(self.window.window, self.currency_title, color, (640, frame_shift + 20),
                                     "topright")

        self.font_bigger.render_text(self.window.window, self.needs_description[0], color, (120, frame_shift + 100),
                                     "topleft")
        self.font_smaller.render_text(self.window.window, self.needs_description[1], color, (120, frame_shift + 148),
                                     "topleft")
        self.font_smaller.render_text(self.window.window, self.needs_description[2], color, (120, frame_shift + 180),
                                     "topleft")
        self.font_bigger.render_text(self.window.window, self.needs_description[3], color, (640, frame_shift + 100),
                                     "topright")

        self.font_bigger.render_text(self.window.window, self.feeding_description[0], color, (120, frame_shift + 220),
                                     "topleft")
        self.font_smaller.render_text(self.window.window, self.feeding_description[1], color, (120, frame_shift + 268),
                                      "topleft")
        self.font_smaller.render_text(self.window.window, self.feeding_description[2], color, (120, frame_shift + 300),
                                      "topleft")
        self.font_bigger.render_text(self.window.window, self.feeding_description[3], color, (640, frame_shift + 220),
                                     "topright")

        self.font_bigger.render_text(self.window.window, self.petting_description[0], color, (120, frame_shift + 340),
                                     "topleft")
        self.font_smaller.render_text(self.window.window, self.petting_description[1], color, (120, frame_shift + 388),
                                      "topleft")
        self.font_smaller.render_text(self.window.window, self.petting_description[2], color, (120, frame_shift + 420),
                                      "topleft")
        self.font_bigger.render_text(self.window.window, self.petting_description[3], color, (640, frame_shift + 340),
                                     "topright")

        self.font_bigger.render_text(self.window.window, self.cleaning_description[0], color, (120, frame_shift + 460),
                                     "topleft")
        self.font_smaller.render_text(self.window.window, self.cleaning_description[1], color, (120, frame_shift + 508),
                                      "topleft")
        self.font_smaller.render_text(self.window.window, self.cleaning_description[2], color, (120, frame_shift + 540),
                                      "topleft")
        self.font_bigger.render_text(self.window.window, self.cleaning_description[3], color, (640, frame_shift + 460),
                                     "topright")