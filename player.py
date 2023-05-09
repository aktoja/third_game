import pygame as pg
from spritesheet import SpriteSheet
from pygame.math import Vector2
import math
from setting import *


class Player(pg.sprite.Sprite):
     speed = 200
     def __init__(self, game, sppath, pos):
        self._layer = PLAYER_LAYER
        super().__init__(game.all_sprites)
        self.game = game
        spritesheet = SpriteSheet(sppath, 2)
        self._load_img(spritesheet)
        self.image = self.walk_u[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.frame = 0
        self.hitbox = pg.Rect(self.rect.x, self.rect.y, self.rect.w/2, self.rect.h/4)
        self.hitbox.centerx = self.rect.centerx
        self.hitbox.bottom = self.rect.bottom - 5
        self.anim_len = 4
    
     def _move(self):
            '''Changes player`s velocity vector.'''
            self.velocity = Vector2((0, 0))
            keys = pg.key.get_pressed()
            if keys[pg.K_w]:
                 self.velocity.y = -1
            if keys[pg.K_s]:
                 self.velocity.y = 1
            if keys[pg.K_a]:
                 self.velocity.x = -1
            if keys[pg.K_d]:
                 self.velocity.x = 1
            
            if self.velocity.length() > 1:
              self.velocity.x = 0

            self.velocity *= math.ceil(self.speed * self.game.dt)
            
            if not self._wall_collide():
               self.rect.center += self.velocity
               self.hitbox.center += self.velocity

     def update(self):
         '''Applies other metods.'''
         self._move()
         self._anim_on()


     def _load_img(self, sheet):
          '''Selects animation.'''
          self.walk_r = []
          self.walk_l = []
          self.walk_d = []
          self.walk_u = []

          w, h = sheet.w//4, sheet.h//4
          for i in range(0, w*4, w):
               self.walk_d.append(sheet.cut(i, 0, w, h))
               self.walk_l.append(sheet.cut(i, h, w, h))
               self.walk_r.append(sheet.cut(i, h*2, w, h))
               self.walk_u.append(sheet.cut(i, h*3, w, h))
     
     def _anim_on(self):
          '''Animates player.'''
          if self.velocity.length() > 0:
               if self.velocity.y > 0:
                    self.animation_list = self.walk_d
               elif self.velocity.y < 0:
                    self.animation_list = self.walk_u
               elif self.velocity.x > 0:
                    self.animation_list = self.walk_r
               elif self.velocity.x < 0:
                    self.animation_list = self.walk_l
               self.frame = (self.frame + self.game.dt * self.speed) % self.anim_len
               self.image = self.animation_list[int(self.frame)]

     def _wall_collide(self):
          tar_rect = self.hitbox.move(self.velocity)
          for tile in self.game.all_walls:
               if tar_rect.colliderect(tile.rect):
                    return True
          return False


class Player(pg.sprite.Sprite):
    def __init__(self, sppath, pos):
        super().__init__()

        self.spitesheet = SpriteSheet(sppath)
        self.image = self.spitesheet.cut(0, 0, 32, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

