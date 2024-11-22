import pygame


class Image:

    def __init__(self, tag, path):
        self.tag = tag
        self.image = pygame.image.load(path)