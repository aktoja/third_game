import pygame as pg


class SpriteSheet():
    def __init__(self, filepath):
        self.sheet = pg.image.load(filepath).convert_alpha()

    def cut(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)
        