import pygame as pg
from setting import *
from player import Player

pg.init()

clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('') 

player = Player('png/player.png', (123, 462))
all_sprites = pg.sprite.Group()
all_sprites.add(player)


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running = False

    all_sprites.draw(screen)

    clock.tick(FPS)
    pg.display.flip()