import pygame

import audio.Sound
import common.Scene
import drawable.Font


class Upgrades(common.Scene):

    def __init__(self, window, statistics):
        super().__init__("UpgradesScene", window)
        self.is_closing_window = False
        self.animation_frames = 0
        self.statistics = statistics
        self.input_cooldown = 0
        self.options_counter = 0
        self.is_option_chosen = False
        self.indicator_animation = 0
        self.options_se = audio.Sound("OptionsSE", "assets/audio/click.wav")
        # text related things
        self.font_bigger = drawable.Font("OptionsFont36")
        self.font_bigger.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 36)
        self.font_smaller = drawable.Font("OptionsFont20")
        self.font_smaller.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 20)
        self.upgrades_title = "upgrades shop"
        self.currency_title = "poops(Þ): 0"
        # descriptions
        self.needs_description = []
        self.feeding_description = []
        self.petting_description = []
        self.cleaning_description = []
        self.snack_ball_description = []
        self.refresh_texts()

    def refresh_texts(self):
        self.needs_description = ["Time dilation" + ("" if self.statistics.needs_upgrade == 0 else "+" + str(self.statistics.needs_upgrade)),
                                  "With increase of Stefan's power, the time is slowing down",
                                  ("Decrease " + str(2 ** (self.statistics.needs_upgrade + 1)) + "x a tempo of decaying needs"),
                                  str(10 * (2 ** (self.statistics.needs_upgrade + 1))) + "Þ"]
        self.feeding_description = ["Better hay quality" + ("" if self.statistics.feeding_upgrade == 0 else "+" + str(self.statistics.feeding_upgrade)),
                                    "Instead of eliminate world hunger, better hay is discovered",
                                    "Feeding will be " + str(self.statistics.feeding_upgrade + 2) + "x more effective",
                                    str(10 * ((self.statistics.feeding_upgrade + 1) ** 2)) + "Þ"]
        self.petting_description = ["Petting army" + ("" if self.statistics.petting_upgrade == 0 else "+" + str(self.statistics.petting_upgrade)),
                                    "Hired more followers to praising Stefan",
                                    "Petting will be " + str(self.statistics.petting_upgrade + 2) + "x more effective",
                                    str(10 * ((self.statistics.petting_upgrade + 1) ** 2)) + "Þ"]
        self.cleaning_description = ["Poop stock market" + ("" if self.statistics.cleaning_upgrade == 0 else "+" + str(self.statistics.cleaning_upgrade)),
                                     "Stefan's poops are getting more and more valuable",
                                     ("Cleaning will be " + str(self.statistics.cleaning_upgrade + 2) +
                                      "x more effective, each poop will give " + ("2" if self.statistics.cleaning_upgrade == 0
                                      else str(2 * self.statistics.cleaning_upgrade + 2)) + "Þ"),
                                     str(10 * (2 ** (self.statistics.cleaning_upgrade + 1))) + "Þ"]
        self.snack_ball_description = ["Physics bending" + ("" if self.statistics.snack_ball_upgrade == 0 else "+" + str(self.statistics.snack_ball_upgrade)),
                                    "Compress snacks using a gravity, may create a black hole",
                                    "Snack ball will be " + str(self.statistics.snack_ball_upgrade + 2) + "x more effective",
                                    str(10 * ((self.statistics.snack_ball_upgrade + 1) ** 2)) + "Þ"]

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.input_cooldown >= 0 or self.animation_frames < 120:
            return

        if keyboard_input[pygame.K_ESCAPE] or keyboard_input[pygame.K_x]:
            self.is_closing_window = True
        elif keyboard_input[pygame.K_UP] or keyboard_input[pygame.K_w]:
            if self.options_counter > 0:
                self.options_counter -= 1
                self.input_cooldown = 30
                self.options_se.sound.play()
        elif keyboard_input[pygame.K_DOWN] or keyboard_input[pygame.K_s]:
            if self.options_counter < 4:
                self.options_counter += 1
                self.input_cooldown = 30
                self.options_se.sound.play()
        elif keyboard_input[pygame.K_RIGHT] or keyboard_input[pygame.K_d]:
            self.is_option_chosen = True
            self.input_cooldown = 15
            self.options_se.sound.play()

    def update(self):
        self.input_cooldown -= 1
        self.indicator_animation = (0 if self.indicator_animation == 40 else self.indicator_animation + 1)
        self.currency_title = "poops(Þ): " + str(self.statistics.currency)

        if self.is_closing_window:
            if self.animation_frames <= 0:
                self.is_closing_window = False
                return True
            else:
                self.animation_frames -= 2
        elif self.animation_frames < 120:
                self.animation_frames += 1
        elif self.is_option_chosen:
            match self.options_counter:
                case 0:
                    cost = 10 * (2 ** (self.statistics.needs_upgrade + 1))
                    if self.statistics.currency >= cost:
                        self.statistics.currency -= cost
                        self.statistics.needs_upgrade += 1
                case 1:
                    cost = 10 * ((self.statistics.feeding_upgrade + 1) ** 2)
                    if self.statistics.currency >= cost:
                        self.statistics.currency -= cost
                        self.statistics.feeding_upgrade += 1
                case 2:
                    cost = 10 * ((self.statistics.petting_upgrade + 1) ** 2)
                    if self.statistics.currency >= cost:
                        self.statistics.currency -= cost
                        self.statistics.petting_upgrade += 1
                case 3:
                    cost = 10 * (2 ** (self.statistics.cleaning_upgrade + 1))
                    if self.statistics.currency >= cost:
                        self.statistics.currency -= cost
                        self.statistics.cleaning_upgrade += 1
                case 4:
                    cost = 10 * ((self.statistics.snack_ball_upgrade + 1) ** 2)
                    if self.statistics.currency >= cost:
                        self.statistics.currency -= cost
                        self.statistics.snack_ball_upgrade += 1
                case _:
                    pass
            self.refresh_texts()
            self.is_option_chosen = False
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

        # indicators
        if self.options_counter < 4:
            pygame.draw.polygon(self.window.window, pygame.Color(255, 255, 255, 255), ((320, frame_shift + 580), (400, frame_shift + 580), (360, frame_shift + 600)))

            self.font_bigger.render_text(self.window.window, self.needs_description[0], color, (120, frame_shift + 100),
                                         "topleft")
            self.font_smaller.render_text(self.window.window, self.needs_description[1], color,
                                          (120, frame_shift + 148), "topleft")
            self.font_smaller.render_text(self.window.window, self.needs_description[2], color,
                                          (120, frame_shift + 180), "topleft")
            self.font_bigger.render_text(self.window.window, self.needs_description[3], color, (640, frame_shift + 100),
                                         "topright")

            self.font_bigger.render_text(self.window.window, self.feeding_description[0], color,
                                         (120, frame_shift + 220), "topleft")
            self.font_smaller.render_text(self.window.window, self.feeding_description[1], color,
                                          (120, frame_shift + 268), "topleft")
            self.font_smaller.render_text(self.window.window, self.feeding_description[2], color,
                                          (120, frame_shift + 300), "topleft")
            self.font_bigger.render_text(self.window.window, self.feeding_description[3], color,
                                         (640, frame_shift + 220), "topright")

            self.font_bigger.render_text(self.window.window, self.petting_description[0], color,
                                         (120, frame_shift + 340), "topleft")
            self.font_smaller.render_text(self.window.window, self.petting_description[1], color,
                                          (120, frame_shift + 388), "topleft")
            self.font_smaller.render_text(self.window.window, self.petting_description[2], color,
                                          (120, frame_shift + 420), "topleft")
            self.font_bigger.render_text(self.window.window, self.petting_description[3], color,
                                         (640, frame_shift + 340), "topright")

            self.font_bigger.render_text(self.window.window, self.cleaning_description[0], color,
                                         (120, frame_shift + 460), "topleft")
            self.font_smaller.render_text(self.window.window, self.cleaning_description[1], color,
                                          (120, frame_shift + 508), "topleft")
            self.font_smaller.render_text(self.window.window, self.cleaning_description[2], color,
                                          (120, frame_shift + 540), "topleft")
            self.font_bigger.render_text(self.window.window, self.cleaning_description[3], color,
                                         (640, frame_shift + 460), "topright")
        else:
            pygame.draw.polygon(self.window.window, pygame.Color(255, 255, 255, 255), ((320, frame_shift + 100), (400, frame_shift + 100), (360, frame_shift + 80)))

            self.font_bigger.render_text(self.window.window, self.snack_ball_description[0], color, (120, frame_shift + 100),
                                         "topleft")
            self.font_smaller.render_text(self.window.window, self.snack_ball_description[1], color,
                                          (120, frame_shift + 148), "topleft")
            self.font_smaller.render_text(self.window.window, self.snack_ball_description[2], color,
                                          (120, frame_shift + 180), "topleft")
            self.font_bigger.render_text(self.window.window, self.snack_ball_description[3], color, (640, frame_shift + 100),
                                         "topright")

        indicator_position = (76, frame_shift + 124 + 120 * (self.options_counter % 4))
        pygame.draw.polygon(self.window.window, pygame.Color(255, 255, 255, 255),
                            ((indicator_position[0] + 4 * self.indicator_animation // 10, indicator_position[1]),
                             (indicator_position[0] + 4 * self.indicator_animation // 10, indicator_position[1] + 48),
                             (indicator_position[0] + 24 + 4 * self.indicator_animation // 10, indicator_position[1] + 24)))