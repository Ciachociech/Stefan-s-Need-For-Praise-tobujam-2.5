import pygame


class Sound:
    def __init__(self, tag, path):
        self.tag = tag
        self.sound = pygame.mixer.Sound(path)
