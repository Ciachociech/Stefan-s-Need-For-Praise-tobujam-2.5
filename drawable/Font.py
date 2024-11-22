import pygame


class Font:
    def __init__(self, tag):
        self.font = None
        self.tag = tag

    def load_system_font(self, font_name, size, bold=False, italic=False):
        self.font = pygame.font.SysFont(font_name, size, bold, italic)

    def load_font_from_file(self, path, size):
        self.font = pygame.font.Font(path, size)

    def render_text(self, window, text, color, position=None, is_centered=False):
        text_surface = self.font.render(text, True, color)
        if position is None:
            position = text_surface.get_rect()
        elif is_centered:
            position = text_surface.get_rect(center=position)
        window.blit(text_surface, position)
