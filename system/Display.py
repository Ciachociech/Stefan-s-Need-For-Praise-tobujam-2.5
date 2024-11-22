import pygame


class Display:
    def __init__(self, width, height, name):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        self.frames = 60
        self.clock = pygame.time.Clock()

    def set_icon(self, path):
        img = pygame.image.load(path)
        pygame.display.set_icon(img)

    def display_and_wait(self):
        pygame.display.flip()
        self.clock.tick(60)

    def clear(self):
        self.window.fill("black")
