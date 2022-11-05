import pygame as pg
from pygame.sprite import Sprite


class Garbage(Sprite):
    def __init__(self,setting,screen):
        super().__init__()
        self.screen = screen
        self.setting = setting

        self.image = pg.image.load('images/garbage.png')#name image for .draw(screen) work((or else can't search the image!
        self.image = pg.transform.scale(self.image, (80, 95))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  # 80
        self.rect.y = self.rect.height  # 95
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left<= 0:
            return True

    def update(self):
        self.x+= self.setting.garbage_speed_factor*self.setting.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.garbage_image, self.rect)
