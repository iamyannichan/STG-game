import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,setting,screen,mouth):
        super().__init__()
        self.screen=screen

        self.rect=pg.Rect(
            0,0,setting.bullet_width,setting.bullet_height
        )
        self.color=setting.bullet_color
        self.rect.centerx=mouth.rect.centerx
        self.rect.top=mouth.rect.top
        self.y=float(self.rect.y)
        self.speed_factor=setting.bullet_speed_factor

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_b(self):
        pg.draw.rect(self.screen,self.color,self.rect)