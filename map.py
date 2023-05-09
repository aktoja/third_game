import pygame as pg
import csv
from spritesheet import png
from setting import *


class Map:
    '''Creates map.'''

    WALL_LIST = [1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                18, 19, 20, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
                35, 36, 37, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                52, 53, 54, 58, 59, 60, 61, 52, 53, 54, 65, 66, 67,
                69, 70, 75, 76, 77, 78, 79, 81, 82, 83, 84,
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101,
                107, 108, 109, 110, 11, 112, 113, 114, 115, 116, 227, 118,
                119, 120, 121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135]
    
    NPC_LIST = list(range(119, 126))
    
    def __init__(self, game, csv_path, image_path, tile_size, space=0) -> None:
        data_list = self._csv_to_list(csv_path)
        self.image_list = self._image_to_list(image_path, tile_size, space)
        self._load_tiles(game, data_list, self.image_list)
        self.width = len(data_list[0]) * TILE_SIZE
        self.height = len(data_list) * TILE_SIZE



    def _csv_to_list(self, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            data = list(reader)
        return data
    
    def _image_to_list(self, image_path, tile_size, space):
        '''Adds tiles to list.'''
        images_list = []
        image = pg.image.load(image_path).convert()
        if tile_size != TILE_SIZE:
            scale = TILE_SIZE // tile_size
            space *= scale
            c_size = image.get_size()
            tar_size = tuple(i * scale for i in c_size)
            image = pg.transform.scale(image, tar_size)
        w, h = image.get_size()
        for y in range(0, h, TILE_SIZE + space):
            for x in range(0, w, TILE_SIZE + space):
                tile = image.subsurface(x, y, TILE_SIZE, TILE_SIZE)
                images_list.append(tile)
        return images_list
    
    def _load_tiles(self, game, data_list, image_list):
        '''Creates Tile object.'''
        for y, row in enumerate(data_list):
            for x, index in enumerate(row):
                is_collide = int(index) in Map.WALL_LIST
                Tile(game, x, y, image_list[int(index)], is_collide)


class Tile(pg.sprite.Sprite):
    '''Creates objects for map.'''
    def __init__(self, game, x, y, image, is_wall=False) -> None:
        if is_wall:
            groups = game.all_sprites, game.all_walls
        else:
            groups = game.all_sprites
        self._layer = GROUND_LAYER
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Camera:
    '''Creates camera object.'''
    def __init__(self, map_width, map_height) -> None:
        self.offset = (0, 0)
        self.map_height = map_height
        self.map_width = map_width


    def apply(self, object):
        return object.rect.move(self.offset)
    
    def update(self, target):
        '''Makes camera follow player.'''
        x = -target.rect.x + WIDTH//2
        y = -target.rect.y + HEIGHT//2
        x = min(x, 0)
        y = min(y, 0)
        x = max(x, -self.map_width + WIDTH)
        y = max(y, -self.map_height + HEIGHT)
        self.offset = (x, y)
        