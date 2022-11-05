import pygame as pg

class Mouth():
    def __init__(self,screen,setting):
        self.screen=screen
        self.setting=setting

        self.mouth_image=pg.image.load('images/mouth.png')
        self.mouth_image=pg.transform.scale(self.mouth_image,(180,130))
        self.rect=self.mouth_image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx =self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.centre = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        self.y = float(self.rect.y)

        self.moving_right=False
        self.moving_left=False

        self.moving_up=False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:#=1000(screenwigh)
            self.centre+=self.setting.mouth_speed_factor
        if self.moving_left and self.rect.left>0:
            self.centre-=self.setting.mouth_speed_factor
        if self.moving_up and self.rect.top >= 0:
            self.y -= self.setting.mouth_speed_factor
        if self.moving_down and self.rect.bottom <= 630:
            self.y += self.setting.mouth_speed_factor

        self.rect.centerx = self.centre

        self.rect.y = self.y

    def center_mouth(self):
        self.centre=self.screen_rect.centerx
        self.y=630-130#bottom
        #?unsolve for understanding

    def blitme(self):
        self.screen.blit(self.mouth_image,self.rect)