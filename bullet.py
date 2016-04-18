import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):


    def __init__(self, ai_settings, screen, ship)
    """Create bullet objects at shipts current possition"""
    super(Bullet, self).__init__()
    self.screen = screen

    #Create bullet rect at (0,0) and then set correct position
    self.rect = pygame.rect(0, 0, aisettings.bullet_width, aisettings.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.rect.top = ship.rect.top


    #store bullets position as decimal value
    self.y = float(self.rect.y)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor
