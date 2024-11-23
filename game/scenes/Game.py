import math
import random

import pygame

import common.Scene
import drawable.Font
import game.objects.Indicator
import game.objects.Stefan


class Game(common.Scene):

    def __init__(self, window):
        super().__init__("GameMainScene", window)
        # variables set during restarting scene
        self.input_cooldown = None
        self.main_options_counter = None
        self.action_options_counter = None
        self.is_option_chosen = None
        self.poops_locations = None
        # objects
        self.stefan = game.objects.Stefan()
        self.indicator = game.objects.Indicator("OptionsIndicator")
        # text/options related things
        self.font = drawable.Font("OptionsFont")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 48)
        self.main_options_texts = ["actions", "statistics", "upgrades", "save & exit"]
        self.action_options_texts = ["feed", "pet", "clean", "snack ball", "hide & seek", "toy", "bowling", "back"]


    def set(self, statistics):
        self.stefan.set(statistics)
        self.input_cooldown = 0
        self.main_options_counter = 0
        self.action_options_counter = -1
        self.is_option_chosen = False
        self.poops_locations = []

    def add_new_poop_location(self):
        location_x = random.randint(0, 256)
        location_y = random.randint(0, 256)
        if location_x >= 128:
            location_x += 448
        else:
            location_x += 16
        if location_y >= 128:
            location_y += 448
        else:
            location_y += 16
        self.poops_locations.append((location_x, location_y))

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
        if self.stefan.statistics.check_lose_condition() != 0:
            return 0
        if self.stefan.statistics.poops > 0 and len(self.poops_locations) < math.log2(self.stefan.statistics.poops + 1):
            self.add_new_poop_location()

        self.input_cooldown -= 1
        if self.is_option_chosen:
            self.is_option_chosen = False

            # if actions option from main menu is chosen
            if self.main_options_counter == 0:
                self.main_options_counter = -1
                self.action_options_counter = 0
                return
            # any other option from main menu is chosen
            elif self.main_options_counter >= 1:
                return self.main_options_counter + 1

            match self.action_options_counter:
                # if back option from actions menu is chosen
                case 7: # len(self.action_options_texts) - 1 - but Python doesn't allow this
                    pass
                # simple actions (first three) from actions menu is chosen
                case 0:
                    self.stefan.statistics.update_needs((10, 10, 0, 30))
                case 1:
                    self.stefan.statistics.update_needs((20, 20, 0, 10))
                case 2:
                    self.stefan.statistics.update_needs((10, 10, -10, 0))
                    self.stefan.statistics.change_poops_to_currency()
                    self.poops_locations = []
                # any other option (mini-games) from actions menu is chosen
                case _:
                    return -self.action_options_counter - 1
            # go back to main menu anyway
            self.main_options_counter = 0
            self.action_options_counter = -1


    def render(self, color = pygame.Color(255, 255, 255, 255)):
        for poop in self.poops_locations:
            pygame.draw.circle(self.window.window, pygame.Color(155, 103, 60, 255), poop, 16)
            pygame.draw.circle(self.window.window, pygame.Color(102, 70, 40, 255), poop, 16, 2)

        self.stefan.render(self.window.window)
        self.indicator.render(self.window.window)

        for i in range(3):
            text_position = (120 + 240 * i, 600)
            if self.main_options_counter >= 0:
                self.font.render_text(self.window.window, self.main_options_texts[
                    (self.main_options_counter + i - 1) % len(self.main_options_texts)], color, text_position, "center")
            elif self.action_options_counter >= 0:
                self.font.render_text(self.window.window, self.action_options_texts[
                    (self.action_options_counter + i - 1) % len(self.action_options_texts)], color, text_position, "center")
