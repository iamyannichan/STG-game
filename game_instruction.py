import pygame as pg
import pygame.font

text='Play !'

class Instruct_buttom():
    def __init__(self,setting,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width,self.height=180,45
        self.buttom_color=(170,100,255)
        self.text_color=(255,255,255)
        self.font=pg.font.SysFont(None,40)#type,size of letter

        self.rect=pg.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image=self.font.render(msg,True,self.text_color,self.buttom_color)

        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_ib(self):
        self.screen.fill(self.buttom_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)