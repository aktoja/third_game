import pygame as pg
import csv
from spritesheet import png
from setting import *

class Map:
    def __init__(self, game, csv_path, image_path, space=0) -> None:
        data_list = self._csv_to_list(csv_path)
        image_list = self._image_to_list(image_path, space)
        self._load_tiles(game, data_list, image_list)
        



    def _csv_to_list(self, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    
    def _image_to_list(self, image_path, space):
        images_list = []
        image = pg.image.load(image_path).convert()
        w, h = image.get_size()
        for y in range(0, h, TILE_SIZE + space):
            for x in range(0, w, TILE_SIZE + space):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                images_list.append(tile)
        return images_list
    
    def _load_tiles(self, game, data_list, image_list):
        for y, row in enumerate(data_list):
            for x, index in enumerate(row):
                Tile(game, x, y, image_list[int(index)])


class Tile(pg.sprite.Sprite):
    def __init__(self, game, x, y, image) -> None:
        super().__init__(game.all_sprites)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE