import pygame as pg
from spritesheet import SpriteSheet


class Player(pg.sprite.Sprite):
    def __init__(self, sppath, pos):
        super().__init__()

        self.spitesheet = SpriteSheet(sppath)
        self.image = self.spitesheet.cut(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

