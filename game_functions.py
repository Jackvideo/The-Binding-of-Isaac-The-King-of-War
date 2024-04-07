import sys
import pygame
from alien import Alien
from bullet import Bullet

def check_events(ai_settings, screen, player, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, player, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings, screen, player, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN and ai_settings.game_state == "start":
            ai_settings.play_game()
            pygame.mixer.music.load('./The Binding of Isaac The King of War/sounds/basic boss fight.ogg')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
        
            
            
def update_screen(ai_settings, screen, player,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.blit(ai_settings.background, (0,0))
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.blitme()
    player.draw_Health()
    ai_settings.clock += 1
    if ai_settings.clock % 20 == 0:
        player.image= pygame.image.load('./The Binding of Isaac The King of War/images/player1.png')
    if ai_settings.clock>ai_settings.alien_start and ai_settings.clock % ai_settings.alien_summon_speed == 1:
        summon_aliens(ai_settings, screen, aliens)
    aliens.draw(screen)
    #让最近绘制的屏幕可见
    score_text=ai_settings.score_font.render("Score: "+str(ai_settings.score), True, (255,255,255))
    screen.blit(score_text, (screen.get_rect().centerx-100,10))
    pygame.display.flip()
    
def check_keydown_events(event,ai_settings, screen, player, bullets):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, player, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
        
def check_keyup_events(event,ai_settings, screen, player, bullets):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False
    elif event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False
    elif event.key == pygame.K_SPACE:
        player.image= pygame.image.load('./The Binding of Isaac The King of War/images/player1.png')

        
def fire_bullet(ai_settings, screen, player, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, player)
        bullets.add(new_bullet)
        player.isShoot()
        ai_settings.shoot_sound.play()
        
def summon_aliens(ai_settings, screen, aliens):
    """创建外星人群"""
    # 创建一个外星人，并将其加入到编组aliens中
    if len(aliens) < ai_settings.alien_allowed:
        alien = Alien(ai_settings, screen)
        aliens.add(alien)
        
def check_Hit(ai_settings,aliens, bullets):
    """响应子弹和外星人碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(collisions) >0:
        ai_settings.hit_sound.play()
        ai_settings.score +=10

def check_Hurt(ai_settings,player,aliens):
    """响应玩家被击中"""
    if pygame.sprite.spritecollide(player, aliens,True):
        player.health -= 0.5
        player.isHurt()
        ai_settings.score-=20
        if player.health == 0:
            ai_settings.dead_sound.play()
            ai_settings.game_state = "gameover"
        elif player.health % 1 == 0:
            ai_settings.hurt_sound1.play()
        else:
            ai_settings.hurt_sound2.play()


def initialize_game(ai_settings, screen):
    """初始化游戏并创建开始界面"""
    start_img= pygame.image.load('./The Binding of Isaac The King of War/images/start.png')
    screen.blit(start_img, (0,0))
    pygame.display.flip()