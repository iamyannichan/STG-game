
#import sys
import pygame as pg
from selfstudy.game_invation.settings import Settings
from mouth import Mouth
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from game_instruction import Instruct_buttom
from game_instruction import text

def run_game():
    pg.init()
    setting1=Settings()
    screen=pg.display.set_mode(
        (setting1.screen_width,setting1.screen_height))
    pg.display.set_caption('CUTEY INVASION')
    mouth1 = Mouth(screen,setting1)
    bullets=Group()
    garbages=Group()
    stats=GameStats(setting1)

    button=Instruct_buttom(setting1,screen,text)

    gf.create_fleet(setting1,screen,garbages)

    while True:
        gf.check_events(setting1, screen, stats, button, mouth1, bullets)#close game should active still

        if stats.game_active:

            mouth1.update()
            gf.update_bullets(setting1,screen,garbages,bullets)
            gf.update_garbages(setting1,mouth1,garbages,stats,screen,bullets)

        gf.update_screen(screen,setting1,mouth1,garbages,bullets,button,stats)

run_game()