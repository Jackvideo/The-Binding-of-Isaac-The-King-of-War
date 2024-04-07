import sys
import pygame
from setting import Settings
from player import Player
from pygame.sprite import Group
from alien import Alien
import game_functions

def run_game():
    #初始化游戏，创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("The Binding of Isaac: The King of War")
    #背景音乐
    pygame.mixer.music.load('./The Binding of Isaac The King of War/sounds/title screen intro.ogg')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    #背景
    background= ai_settings.background
    #子弹
    bullets = Group()
    #创建玩家飞船
    player=Player(ai_settings,screen)
    
    #创建敌人
    aliens = Group()
    #开始游戏主循环
    if ai_settings.game_state=="start":
        game_functions.initialize_game(ai_settings, screen)
    while True:
        playing_game(ai_settings, screen, player, bullets, aliens)

def playing_game(ai_settings, screen, player, bullets, aliens):
    while True:
        game_functions.check_events(ai_settings, screen, player, bullets)
        if ai_settings.game_state =="running":
            player.update()
            game_functions.check_Hit(ai_settings,aliens, bullets)
            game_functions.check_Hurt(ai_settings,player,aliens)
            bullets.update()
            aliens.update()
            game_functions.update_screen(ai_settings, screen, player,aliens,bullets)
        if ai_settings.game_state=="gameover":
            screen.blit(pygame.image.load("./The Binding of Isaac The King of War/images/gameover.png"),(0,0))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

run_game()
