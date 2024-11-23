import pygame

import common.Scene
import drawable.Font
import game.objects.Indicator
import game.objects.Stefan


class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)
        # variables set during restarting game
        self.input_cooldown = None
        self.main_options_counter = None
        self.action_options_counter = None
        self.is_option_chosen = None
        # objects
        self.stefan = game.objects.Stefan()
        self.indicator = game.objects.Indicator("OptionsIndicator")
        # text/options related things
        self.font = drawable.Font("OptionsFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 48)
        self.main_options_texts = ["actions", "statistics", "upgrades", "save & exit"]
        self.action_options_texts = ["feed", "pet", "snack ball", "clean", "hide & seek", "toy", "bowling", "back"]


    def set(self, statistics):
        self.stefan.set(statistics)
        self.input_cooldown = 0
        self.main_options_counter = 0
        self.action_options_counter = -1
        self.is_option_chosen = False

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.input_cooldown >= 0:
            return
        if keyboard_input[pygame.K_LEFT] or keyboard_input[pygame.K_a]:
            if self.main_options_counter >= 0:
                self.main_options_counter = (self.main_options_counter - 1) % len(self.main_options_texts)
            elif self.action_options_counter >= 0:
                self.action_options_counter = (self.action_options_counter - 1) % len(self.action_options_texts)
            self.input_cooldown = 30
        elif keyboard_input[pygame.K_RIGHT] or keyboard_input[pygame.K_d]:
            if self.main_options_counter >= 0:
                self.main_options_counter = (self.main_options_counter + 1) % len(self.main_options_texts)
            elif self.action_options_counter >= 0:
                self.action_options_counter = (self.action_options_counter + 1) % len(self.action_options_texts)
            self.input_cooldown = 30
        elif keyboard_input[pygame.K_UP] or keyboard_input[pygame.K_DOWN] or keyboard_input[pygame.K_w] or keyboard_input[pygame.K_s]:
            self.is_option_chosen = True
            self.input_cooldown = 15

    def update(self):
        self.stefan.update()
        if self.stefan.statistics.check_lose_condition():
            return 0

        self.input_cooldown -= 1
        if self.is_option_chosen:
            self.is_option_chosen = False
            if self.main_options_counter == 0:
                self.main_options_counter = -1
                self.action_options_counter = 0
            elif self.main_options_counter >= 1:
                return self.main_options_counter + 1
            elif self.action_options_counter == len(self.action_options_texts) - 1:
                self.main_options_counter = 0
                self.action_options_counter = -1
            elif self.action_options_counter >= 0:
                return -self.action_options_counter - 1

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.stefan.render(self.window.window)
        self.indicator.render(self.window.window)

        for i in range(3):
            text_position = (120 + 240 * i, 600)
            if self.main_options_counter >= 0:
                self.font.render_text(self.window.window, self.main_options_texts[
                    (self.main_options_counter + i - 1) % len(self.main_options_texts)], color, text_position, True)
            elif self.action_options_counter >= 0:
                self.font.render_text(self.window.window, self.action_options_texts[
                    (self.action_options_counter + i - 1) % len(self.action_options_texts)], color, text_position, True)