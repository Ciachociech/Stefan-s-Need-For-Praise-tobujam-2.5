import math
import random

import pygame

import common.Scene
import drawable.Font


class SnackBall(common.Scene):

    def __init__(self, window):
        super().__init__("SnackBallScene", window)
        self.ball_position = (360, 270)
        self.angle = 2 * math.pi * random.random()
        self.velocity = random.randint(0, 150)
        self.is_set_angle = False
        self.is_set_velocity = False
        self.cooldown = 0
        self.score = 0
        #
        self.font = drawable.Font("OptionsFont20")
        self.font.load_font_from_file("assets/fonts/NerkoOne-Regular.ttf", 20)

    def process_input(self, keyboard_input, joystick, mouse_input, mouse_position):
        if self.cooldown >= 0:
            return
        if keyboard_input[pygame.K_z] or keyboard_input[pygame.K_SPACE]:
            if not self.is_set_angle:
                self.is_set_angle = True
                self.cooldown = 15
            else:
                self.is_set_velocity = True

    def check_collision(self):
        if self.ball_position[0] < 196:
            self.score += 1
            self.ball_position = (392 - self.ball_position[0], self.ball_position[1])
            self.angle = math.pi - self.angle if self.angle <= math.pi else 3 * math.pi - self.angle
        elif self.ball_position[0] > 524:
            self.score += 1
            self.ball_position = (1048 - self.ball_position[0], self.ball_position[1])
            self.angle = math.pi - self.angle if self.angle <= math.pi else 3 * math.pi - self.angle
        if self.ball_position[1] < 106:
            self.score += 1
            self.ball_position = (self.ball_position[0], 212 - self.ball_position[1])
            self.angle = 2 * math.pi - self.angle
        elif self.ball_position[1] > 434:
            self.score += 1
            self.ball_position = (self.ball_position[0], 868 - self.ball_position[1])
            self.angle = 2 * math.pi - self.angle


    def update(self):
        self.cooldown -= 1

        if self.is_set_angle and self.is_set_velocity:
            self.ball_position = (self.ball_position[0] + 0.1 * self.velocity * math.cos(self.angle), self.ball_position[1] + 0.1 * self.velocity * math.sin(self.angle))
            self.velocity -= (1 if self.cooldown <= 0 else 0)
            self.check_collision()
            if self.velocity <= 0:
                if self.cooldown <= 0:
                    self.cooldown = 90
                elif self.cooldown == 1:
                    return_value = (0, 0, 4 * self.score, 6 * self.score)
                    self.__init__(self.window)
                    return return_value
            return None

        if not self.is_set_angle:
            self.angle += math.pi / 180
        elif self.velocity < 150:
            self.velocity += 1
        else:
            self.velocity = 0
        return None

    def render(self, color = pygame.Color(255, 255, 255, 255)):
        # frame background
        pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (180, 90, 360, 360))
        pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255), (180, 90, 360, 360), width=8)

        # draw ball
        pygame.draw.circle(self.window.window, pygame.Color(255, 255, 255, 255), self.ball_position, 8, 2)
        if not self.is_set_angle:
            pygame.draw.line(self.window.window, pygame.Color(255, 255, 255, 255), self.ball_position,
                             (self.ball_position[0] + 75 * math.cos(self.angle), self.ball_position[1] + 75 * math.sin(self.angle)), 4)
        elif not self.is_set_velocity:
            pygame.draw.line(self.window.window, pygame.Color(255, 255, 255, 255), self.ball_position,
                               (self.ball_position[0] + self.velocity * math.cos(self.angle), self.ball_position[1] + self.velocity * math.sin(self.angle)), 4)

        if self.is_set_angle and self.is_set_velocity and self.velocity <= 0:
            pygame.draw.rect(self.window.window, pygame.Color(0, 0, 0, 191), (270, 180, 180, 180))
            pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255), (270, 180, 180, 180), width=4)

            self.font.render_text(self.window.window, "bounces: " + str(self.score), color, (360, 200), "midtop")
            if self.score > 0:
                # TODO: replace with icons
                pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                 (320, 250, 32, 32))
                pygame.draw.rect(self.window.window, pygame.Color(255, 255, 255, 255),
                                 (320, 300, 32, 32))

                self.font.render_text(self.window.window, "+" + "+" * int(0.35 * self.score), color, (360, 266), "midleft")
                self.font.render_text(self.window.window, "+" + "+" * int(0.5 * self.score), color,(360, 316), "midleft")
            else:
                self.font.render_text(self.window.window, "Better luck", color, (360, 276), "center")
                self.font.render_text(self.window.window, "next time!", color, (360, 306), "center")