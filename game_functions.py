import sys
import pygame as pg
from bullet import Bullet
from gabage import Garbage
from time import sleep

def fire_b(setting, screen, mouth, bullets):
    if len(bullets) <= setting.bullets_allowed:  # 1more than allowed
        new_bullet1 = Bullet(setting, screen, mouth)
        bullets.add(new_bullet1)

def check_keydown_events(e, setting, screen, mouth, bullets):
    if e.key == pg.K_SLASH:
        sys.exit()
    if e.key == pg.K_RIGHT:
        mouth.moving_right = True
    if e.key == pg.K_LEFT:
        mouth.moving_left = True
    if e.key == pg.K_SPACE:
        fire_b(setting, screen, mouth, bullets)
    if e.key == pg.K_UP:
        mouth.moving_up = True
    if e.key == pg.K_DOWN:
        mouth.moving_down = True

def check_keyup_events(e, mouth):
    if e.key == pg.K_RIGHT:
        mouth.moving_right = False
    if e.key == pg.K_LEFT:
        mouth.moving_left = False
    if e.key == pg.K_UP:
        mouth.moving_up = False
    if e.key == pg.K_DOWN:
        mouth.moving_down = False

def check_events(setting, screen, stats, play_button, mouth, bullets):
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit()
        elif e.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
        elif e.type == pg.KEYDOWN:
            check_keydown_events(e, setting, screen, mouth, bullets)
        elif e.type == pg.KEYUP:
            check_keyup_events(e, mouth)


# 2
def update_bullets(setting,screen,garbage1,bullets):
    for b in bullets.copy():
        if b.rect.bottom <= 0:
            bullets.remove(b)
    bullets.update()
    check_bullet_alien_collisions(setting,screen,garbage1,bullets)

def check_bullet_alien_collisions(setting,screen,garbage1,bullets):
    collisions= pg.sprite.groupcollide(bullets,garbage1,False,True)

    if len(garbage1)==0:
        bullets.empty()
        create_fleet(setting,screen,garbage1)

def mouth_hit(setting,stats,screen,mouth,garbages,bullets):
    if stats.mouth_left>0:
        stats.mouth_left-=1

        garbages.empty()
        bullets.empty()

        create_fleet(setting,screen,garbages)
        mouth.center_mouth()

        sleep(0.3)
    else:
        stats.game_active=False

def check_g_bottom(setting,stats,screen,mouth,garbages,bullets):
    screen_rect=screen.get_rect()
    for g in garbages.sprites():
        if g.rect.bottom>=screen_rect.bottom:
            mouth_hit(setting,stats,screen,mouth,garbages,bullets)
            break
# 3
def get_number_garbage_x(setting,garbage1):
    b = 2 * garbage1.rect.width
    aa = setting.screen_width - b
    return int(aa / b)  # 5.25

def get_number_garbage_y(setting, garbage1):
    av_y=setting.screen_height-2*garbage1.rect.height-130#mouth height
    row_number=int(av_y/(1.05*garbage1.rect.height))
    print(av_y,row_number)
    return row_number

def create_garbage(setting,screen,garbages,g_number,row_number):
    garbage2 = Garbage(setting, screen)
    garbage2_width = garbage2.rect.width
    garbage2.x = garbage2_width + g_number * 2 * garbage2_width
    garbage2.rect.x = garbage2.x
    garbage2.rect.y =50+row_number * 1.25* garbage2.rect.height #50is upper space
    garbages.add(garbage2)

def create_fleet(setting, screen,garbages):
    garbage1 = Garbage(setting, screen)  # only for calculate, not include in group

    number_garbages_x = get_number_garbage_x(setting,garbage1)
    number_rows = get_number_garbage_y(setting,garbage1)

    for row_n in range(number_rows):
        for g_number in range(number_garbages_x):
            create_garbage(setting,screen,garbages,g_number,row_n)

def check_fleet_edges(setting,garbages):
    for garbage in garbages.sprites():
        if garbage.check_edges():
            change_fleet_direction(setting,garbages)
            break

def change_fleet_direction(setting,garbages):
    for g in garbages.sprites():
        g.rect.y  +=  setting.fleet_drop_speed
    setting.fleet_direction*=-1

def update_garbages(setting,mouth,garbage1,stats,screen,bullets):
    check_fleet_edges(setting,garbage1)
    garbage1.update()

    if pg.sprite.spritecollideany(mouth,garbage1):
        mouth_hit(setting,stats,screen,mouth,garbage1,bullets)

    check_g_bottom(setting, stats, screen, mouth, garbage1, bullets)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active=True

def update_screen(screen, setting, mouth, garbages, bullets,buttom,stats):
    screen.blit(setting.bg_color, setting.bg_color.get_rect())
    for b in bullets.sprites():
        b.draw_b()
    mouth.blitme()
    garbages.draw(screen)

    if not stats.game_active:
        buttom.draw_ib()
    pg.display.flip()