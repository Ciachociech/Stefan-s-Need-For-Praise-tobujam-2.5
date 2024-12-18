import pygame

import audio.Sound
import common.Scene
import drawable.Font


class Gameover(common.Scene):

    def __init__(self, window):
        super().__init__("GameoverScene", window)
        # variables set during restarting scene
        self.input_cooldown = None
        self.options_counter = None
        self.is_option_chosen = None
        self.statistics = None
        # text/options related things
        self.font_bigger = drawable.Font("OptionsFont36")
        self.font_bigger.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 36)
        self.font_smaller = drawable.Font("OptionsFont28")
        self.font_smaller.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 28)
        self.options_texts = ["start over", "exit"]
        self.indicator_animation = 0
        self.gameover_outro = audio.Sound("GameoverSE", "assets/audio/outro.wav")
        self.gameover_outro.sound.set_volume(0.1)
        self.options_se = audio.Sound("OptionsSE", "assets/audio/click.wav")
        # strings
        self.gameover_title = "game over"
        self.gameover_too_bad = ["Stefan has been neglected, so decided to run",
                                 "away and choose its new prophet which will pay",
                                 "more attention and lead to new era of rabbit",
                                 "supremacy. Of course, tides of time can allow you",
                                 "to try again if you dare."]
        self.gameover_too_good = ["Stefan has been cared generously, so decided to",
                                  "conquer the world, soon the era of eternal rabbit",
                                  "supremacy and human extinction (your too) will",
                                  "begin. Of course, tides of time can allow you to",
                                  "try again if you dare."]

    def set(self, statistics):
        self.input_cooldown = 120
        self.options_counter = 0
        self.is_option_chosen = False
        self.statistics = statistics

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.input_cooldown >= 0:
            return

        if keyboard_input[pygame.K_LEFT] or keyboard_input[pygame.K_a]:
            if self.options_counter == 1:
                self.options_se.sound.play()
                self.options_counter = 0
            self.input_cooldown = 30
        elif keyboard_input[pygame.K_RIGHT] or keyboard_input[pygame.K_d]:
            if self.options_counter == 0:
                self.options_se.sound.play()
                self.options_counter = 1
            self.input_cooldown = 30
        elif keyboard_input[pygame.K_UP] or keyboard_input[pygame.K_DOWN] or keyboard_input[pygame.K_w] or keyboard_input[pygame.K_s] or keyboard_input[pygame.K_SPACE] or keyboard_input[pygame.K_z]:
            self.is_option_chosen = True
            self.input_cooldown = 15

    def update(self):
        if self.input_cooldown == 120:
            self.gameover_outro.sound.play()
        self.input_cooldown -= 1
        self.indicator_animation = (0 if self.indicator_animation == 40 else self.indicator_animation + 1)

        if self.is_option_chosen:
            self.is_option_chosen = True
            self.gameover_outro.sound.stop()
            return -2 * self.options_counter + 1

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        # frame background
        pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (60, 180, 600, 360))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),(60, 180, 600, 360), width=8)

        # text rendering
        self.font_bigger.render_text(self.window.window, self.gameover_title, color, (360, 220), "center")
        no_lines = 0
        gameover_text = None
        if self.statistics.check_lose_condition() > 0:
            gameover_text = self.gameover_too_good
        else:
            gameover_text = self.gameover_too_bad
        for text_line in gameover_text:
            self.font_smaller.render_text(self.window.window, text_line, color, (80, 260 + 40 * no_lines))
            no_lines += 1
        self.font_bigger.render_text(self.window.window, self.options_texts[0], color, (210, 500), "center")
        self.font_bigger.render_text(self.window.window, self.options_texts[1], color, (510, 500), "center")

        indicator_position = (80 + 345 * self.options_counter, 470)
        pygame.draw.polygon(self.window.window, pygame.Color(255, 255, 255, 255),
                            ((indicator_position[0] + 4 * self.indicator_animation // 10, indicator_position[1]),
                             (indicator_position[0] + 4 * self.indicator_animation // 10, indicator_position[1] + 48),
                             (indicator_position[0] + 24 + 4 * self.indicator_animation // 10, indicator_position[1] + 24)))
