import pygame as pg
from spritesheet import png
from setting import *
from player import Player
from map import Map, Camera
from npc import Npc, Button


class Game:
    def __init__(self) -> None:
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.running = True



    def new(self):
        '''Creates game objects and groups.'''
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.all_walls = pg.sprite.Group()
        self.player = Player(self, png/'player.png', (123, 462))
        self.map = Map(self, 'map/map.csv', 'map/rpg_tileset.png', 16)
        self.camera = Camera(self.map.width, self.map.height)
        self.npc = Npc(self, (200, 300), self.map.image_list[123], 3)
        self.answer_button = Button(game, (50, 300), 'а мне прописали')
        

    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN and self.answer_button.rect.collidepoint(event.pos):
                self.npc.message.change_text('повезло тебе...')
                self.answer_button.change_text('...')
            
    
    def _update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def _draw(self):
        self.screen.fill((0,0,0))
        current_fps = int(self.clock.get_fps())
        pg.display.set_caption(f'fps {current_fps}') 
        for i in self.all_sprites:
            self.screen.blit(i.image, self.camera.apply(i))
        pg.display.flip()

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS)/1000
            self._events()
            self._update()
            self._draw()
    
if __name__ == '__main__':
    game = Game()
    game.new()
    game.run() 