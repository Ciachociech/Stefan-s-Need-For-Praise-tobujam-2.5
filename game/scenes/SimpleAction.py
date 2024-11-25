import pygame

import common.Scene
import drawable.Font


class SimpleAction(common.Scene):

    def __init__(self, window):
        super().__init__("SimpleActionScene", window)
        self.action_number = None
        self.cooldown = 120
        # font and graphics
        self.font = drawable.Font("OptionsFont20")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 20)
        self.attention_image = common.Object("AttentionImage", "assets/sprites/attention32.png")
        self.power_image = common.Object("PowerImage", "assets/sprites/power32.png")
        self.saturation_image = common.Object("SaturationImage", "assets/sprites/saturation32.png")

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        pass

    def update(self):
        self.cooldown -= 1

        if self.cooldown == 1:
            self.__init__(self.window)
            return (0, 0, 0, 0)
        return None

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (270, 180, 180, 180))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255), (270, 180, 180, 180), width=4)

        match self.action_number:
            case 1:
                self.font.render_text(self.window.window, "feeding results", color, (360, 200), "midtop")

                self.attention_image.render(self.window.window, (320, 235, 32, 32))
                self.power_image.render(self.window.window, (320, 275, 32, 32))
                self.saturation_image.render(self.window.window, (320, 315, 32, 32))
                self.font.render_text(self.window.window, "+", color, (360, 251), "midleft")
                self.font.render_text(self.window.window, "+", color, (360, 291), "midleft")
                self.font.render_text(self.window.window, "+++", color, (360, 331), "midleft")
            case 2:
                self.font.render_text(self.window.window, "petting results", color, (360, 200), "midtop")

                self.attention_image.render(self.window.window, (320, 235, 32, 32))
                self.power_image.render(self.window.window, (320, 275, 32, 32))
                self.saturation_image.render(self.window.window, (320, 315, 32, 32))
                self.font.render_text(self.window.window, "++", color, (360, 251), "midleft")
                self.font.render_text(self.window.window, "++", color, (360, 291), "midleft")
                self.font.render_text(self.window.window, "+", color, (360, 331), "midleft")
            case 3:
                self.font.render_text(self.window.window, "cleaning results", color, (360, 200), "midtop")

                self.attention_image.render(self.window.window, (320, 235, 32, 32))
                self.power_image.render(self.window.window, (320, 275, 32, 32))
                self.saturation_image.render(self.window.window, (320, 315, 32, 32))
                self.font.render_text(self.window.window, "+", color, (360, 251), "midleft")
                self.font.render_text(self.window.window, "+", color, (360, 291), "midleft")
                self.font.render_text(self.window.window, "-", color, (360, 331), "midleft")
            case _:
                pass