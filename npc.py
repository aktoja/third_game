import pygame as pg
import random as rm
import pygame.freetype
from setting import *



class Npc(pg.sprite.Sprite):
    def __init__(self, game, pos, image, hp, text=['они не прописали мне текст']) -> None:
        self._layer = GROUND_LAYER
        groups = game.all_sprites, game.all_walls
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.hp = hp
        self.game = game
        self.message = Message(game, (pos[0]-50, pos[1]-50), text)
        

    def update(self):
        if self.hp > 0:
            time = pg.time.get_ticks()
            if time%32 == 0:
                turn = rm.randint(1, 4)
                if turn == 1:
                    self.rect.y += -5
                if turn == 2:
                    self.rect.y += 5
                if turn == 3 :
                    self.rect.x += -5
                if turn == 4:
                    self.rect.x += 5
        if self.rect.colliderect(self.game.player):
            self.message.print()
        elif self.message.groups():
            self.message.unprint()



class Message(pg.sprite.Sprite):
    def __init__(self, game, pos, text, font=None):
        self._layer = MESSAGE_LAYER
        super().__init__(game.all_sprites)
        self.game = game
        self.text = text
        self.text_pos = (10, 10)
        self.font = pygame.freetype.Font(font, 15)
        self.display_text = ''
        self.pseudo_frame = 0
        surf_text, rect_text = self.font.render(self.text)
        if rect_text.h < 40:
            rect_text.h = 40
        self.image = pg.Surface((rect_text.w + 30, rect_text.h), pg.SRCALPHA)
        self.rect = self.image.get_rect(center=pos)
        self.border = pg.Rect((0, 0), self.rect.size)
        self.border.w = rect_text.w + 20

    def print(self):
        self.pseudo_frame += 0.45
        self.display_text = self.text[:int(self.pseudo_frame)]
        self.add(self.game.all_sprites)
        surf_text, rect_text = self.font.render(self.display_text)
        self.image.fill((255, 255, 255, 0))
        self.image.blit(surf_text, self.text_pos)
        pg.draw.rect(self.image, (0, 0, 0,), self.border, width=2, border_radius=10)

    def unprint(self):
        self.pseudo_frame = 0
        self.display_text = ''
        self.kill()

    def change_text(self, new_text):
        self.text = new_text

class Button(pg.sprite.Sprite):
    def __init__(self, game, pos, text, font):
        self._layer = MESSAGE_LAYER
        super().__init__(game.all_sprites)
        self.image = pg.Surface(())
        self.rect = self.image.get_rect(center=pos)
        self.text_surf, self.text_rect = font.render(text, size=32)
        self.text_rect.center = self.rect.center
