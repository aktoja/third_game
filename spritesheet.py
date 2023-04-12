import pygame as pg
from pathlib import Path
import sys

class SpriteSheet():
    def __init__(self, filepath, scale=1):
        sheet = pg.image.load(filepath).convert_alpha()
        w, h = sheet.get_size()
        final_size = (int(w*scale), int(h*scale))
        self.sheet = pg.transform.scale(sheet, final_size)
        self.w, self.h = self.sheet.get_size()
    def cut(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)

png = Path(sys.argv[0]).parent/'png'
        