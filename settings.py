import pygame as pg
import random as R

class Settings():
    def __init__(self):
        self.screen_width = 1050
        self.screen_height = 630
        self.bg_color=pg.image.load('images/background.png')
        self.bg_color=pg.transform.scale(self.bg_color,(1050,630))

        self.mouth_speed_factor=1.5
        self.mouth_n_limit=2

        self.bullet_speed_factor=3
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 200,200,0
        self.bullets_allowed =4

        self.garbage_speed_factor=1
        self.fleet_drop_speed=R.randint(1, 20)
        self.fleet_direction = 1#-1:left +:right