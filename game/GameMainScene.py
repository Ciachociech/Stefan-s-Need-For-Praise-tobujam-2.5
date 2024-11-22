import pygame

import common.Scene
import drawable.Font
import game.Stefan


class GameMainScene(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)
        self.stefan = game.Stefan()
        self.input_cooldown = 0
        # text/options related things
        self.font = drawable.Font("OptionsFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 48)
        self.options_texts = ["ACTIONS", "STATISTICS", "UPGRADES", "SAVE & EXIT"]
        self.options_counter = 0
        self.is_option_chosen = False


    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.input_cooldown >= 0:
            return
        if keyboard_input[pygame.K_LEFT] or keyboard_input[pygame.K_a]:
            self.options_counter = (self.options_counter - 1) % len(self.options_texts)
            self.input_cooldown = 30
        elif keyboard_input[pygame.K_RIGHT] or keyboard_input[pygame.K_d]:
            self.options_counter = (self.options_counter + 1) % len(self.options_texts)
            self.input_cooldown = 30
        elif keyboard_input[pygame.K_SPACE]:
            self.is_option_chosen = True

    def update(self):
        self.input_cooldown -= 1
        if self.is_option_chosen:
            self.is_option_chosen = False
            return self.options_counter + 1

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        self.stefan.render(self.window.window, (100, 100))
        for i in range(3):
            self.font.render_text(self.window.window,
                                  self.options_texts[(self.options_counter + i - 1) % len(self.options_texts)], color, (120 + 240 * i, 600), True)

