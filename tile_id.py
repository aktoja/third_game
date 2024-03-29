import pygame as pg
import pygame.freetype
from spritesheet import png
from setting import TILE_SIZE


pg.init()
screen = pg.display.set_mode((544, 256))
font = pygame.freetype.Font(None, 16)
image = pg.image.load('map/rpg_tileset.png')
image = pg.transform.scale(image, (544, 256))

index = 0
for y in range(0, 256, TILE_SIZE):
    for x in range(0, 544, TILE_SIZE):
        font.render_to(image, (x+10, y+10), str(index))
        index += 1




running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(image, (0, 0))
    pg.display.flip()
