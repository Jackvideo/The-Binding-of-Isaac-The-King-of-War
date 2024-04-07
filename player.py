import pygame
import math
class Player():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        
        #玩家生命值
        self.max_health = 1.5
        self.health=self.max_health
        self.full_heart= pygame.image.load('./The Binding of Isaac The King of War/images/full_heart.png')
        self.half_heart= pygame.image.load('./The Binding of Isaac The King of War/images/half_heart.png')
        self.empty_heart= pygame.image.load('./The Binding of Isaac The King of War/images/empty_heart.png')
        #初始化生命值图标
        self.heart_rect=self.full_heart.get_rect()
        self.heart_rect.x=float(self.heart_rect.centerx)
        self.heart_rect.y=float(self.screen.get_height()-self.full_heart.get_height()-10)
                
        
        #加载玩家图像，并获取其矩形
        self.image = pygame.image.load('./The Binding of Isaac The King of War/images/player1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将玩家放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.screen.get_height()-self.image.get_height())
        
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        if self.moving_right and self.rect.x <self.screen_rect.right - self.rect.width:
            self.centerx += self.ai_settings.player_speed_factor
        if self.moving_left  and self.rect.x > self.screen_rect.left:
            self.centerx -= self.ai_settings.player_speed_factor
        if self.moving_up  and self.rect.y > self.screen_rect.top:
            self.centery -= self.ai_settings.player_speed_factor
        if self.moving_down  and self.rect.y < self.screen_rect.bottom - self.rect.height:
            self.centery += self.ai_settings.player_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def isShoot(self):
        self.image= pygame.image.load('./The Binding of Isaac The King of War/images/shooting.png')
        
    def isDead(self):
        self.image= pygame.image.load('./The Binding of Isaac The King of War/images/dead.png')
        
    def isHurt(self):
        self.image= pygame.image.load('./The Binding of Isaac The King of War/images/shooting.png')
        
    #检查生命值
    def check_Health(self):
        if self.health == 0:
            self.isDead()
    
    #绘制生命值
    def draw_Health(self):
        i=1
        health=self.health #1.5
        max_health=self.max_health*2 #3
        while i <= max_health:
            temp_rect=self.full_heart.get_rect()
            temp_rect.x=float(self.heart_rect.x+ (i-1)*self.full_heart.get_width())
            temp_rect.centery=float(self.heart_rect.centery)
            Sub=i-0.5-health
            if Sub<0:
                self.screen.blit(self.full_heart,temp_rect)
            elif Sub==0:
                self.screen.blit(self.half_heart,temp_rect)
            else:
                self.screen.blit(self.empty_heart,temp_rect)
            i+=1
        