import pygame as pg
from spritesheet import png
from setting import *
from player import Player
from map import Map
class Game:
    def __init__(self) -> None:
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('') 
        self.running = True

    def new(self):
        '''Creates game objects and groups.'''
        player = Player(png/'player.png', (123, 462))
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player)
        self.map = Map(self, 'map/map.csv', 'map/rpg_tileset.png')

    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False
    
    def _update(self):
        self.all_sprites.update()

    def _draw(self):
        self.screen.fill((0,0,0))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()
    
if __name__ == '__main__':
    game = Game()
    game.new()
    game.run() 