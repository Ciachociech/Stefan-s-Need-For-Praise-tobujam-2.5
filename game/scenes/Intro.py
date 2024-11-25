import pygame

import common.Scene
import drawable.Font


class Intro(common.Scene):

    def __init__(self, window):
        super().__init__("IntroScene", window)
        self.skip_intro = False
        self.line_advance = 0
        self.input_cooldown = 15
        self.advance_cooldown = 180
        # text related things
        self.font = drawable.Font("OptionsFont28")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 28)
        self.introduction = ["You have been chosen to care of mighty rabbit Stefan.",
                             "Keep its needs in good shape or it will run away.",
                             "You can pet, feed or do another activities to care Stefan.",
                             "Moreover, its poops are valuable resource which can be used",
                             "to increase quality of your service. Good luck!"]

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.input_cooldown > 0:
            return

        if keyboard_input[pygame.K_z] or keyboard_input[pygame.K_SPACE]:
            self.line_advance += 1
            self.input_cooldown = 30
            self.advance_cooldown = 180
            if self.line_advance >= len(self.introduction):
                self.skip_intro = True
        elif keyboard_input[pygame.K_ESCAPE]:
            self.skip_intro = True

    def update(self):
        self.input_cooldown -= 1
        self.advance_cooldown -= 1

        if self.advance_cooldown <= 0:
            self.advance_cooldown = 180
            self.line_advance += 1
        if self.skip_intro:
            return True

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        for i in range(0, min(self.line_advance + 1, len(self.introduction))):
            self.font.render_text(self.window.window, self.introduction[i], color, (20, 360 + 40 * i), "topleft")

        if self.line_advance >= len(self.introduction):
            self.font.render_text(self.window.window, "press SPACE to start a game", color, (360, 660), "center")