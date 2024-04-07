import pygame
class Settings():
    
    def __init__(self):
        self.clock = 0
        self.screen_width = 600
        self.screen_height = 900
        self.background= pygame.image.load('./The Binding of Isaac The King of War/images/background.png')
        #游戏状态
        self.game_state= "start"
        
        #玩家速度
        self.player_speed_factor = 2.5
        
        #得分统计
        self.score = 0
        self.score_font= pygame.font.SysFont("Arial", 36)
        
        #子弹设置
        self.bullet_speed_factor = 5
        self.bullets_allowed = 5
        
        #敌人设置
        self.alien_start = 100
        self.alien_summon_speed = 100
        self.alien_speed_factor = 1.5
        self.alien_allowed = 15
        
        #游戏音效
        self.shoot_sound = pygame.mixer.Sound('./The Binding of Isaac The King of War/sounds/shoot.wav')
        self.shoot_sound.set_volume(1)
        self.hit_sound = pygame.mixer.Sound('./The Binding of Isaac The King of War/sounds/hit.wav')
        self.hit_sound.set_volume(1)
        self.hurt_sound1 = pygame.mixer.Sound('./The Binding of Isaac The King of War/sounds/hurt1.wav')
        self.hurt_sound1.set_volume(1)
        self.hurt_sound2 = pygame.mixer.Sound('./The Binding of Isaac The King of War/sounds/hurt2.wav')
        self.hurt_sound2.set_volume(1)
        self.dead_sound = pygame.mixer.Sound('./The Binding of Isaac The King of War/sounds/hurt and die.wav')
        
    def play_game(self):
        self.game_state = "running"