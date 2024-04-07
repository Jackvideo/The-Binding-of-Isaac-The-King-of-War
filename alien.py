from random import randint
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        
        #加载外星人图像
        self.image=pygame.image.load('./The Binding of Isaac The King of War/images/enemy.png')
        self.rect=self.image.get_rect()
        self.rect.x=randint(self.rect.width, self.screen.get_width()-self.rect.width)
        self.rect.y=self.rect.height
        
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        
    def draw(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        """Move the alien based on the speed value."""
        self.x += float(randint(-25, 25))/100
        self.y += self.settings.alien_speed_factor
        self.rect.x = self.x
        self.rect.y = self.y
        if(self.y>self.screen.get_height()):
            self.kill()
            