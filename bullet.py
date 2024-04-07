import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, player):
        self.image=pygame.image.load('./The Binding of Isaac The King of War/images/poopShot.png')
        super(Bullet,self).__init__()
        self.screen=screen
        
        #设置子弹正确位置
        self.rect= pygame.Rect(0,0,self.image.get_width(),self.image.get_height())
        self.rect.centerx=player.rect.centerx
        self.rect.top=player.rect.top
        
        
        self.y=float(self.rect.y)
        self.speed_factor=ai_settings.bullet_speed_factor
        #store the bullet's position as a decimal value
        
    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
        if self.rect.bottom<0:
          self.kill()
        
    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)