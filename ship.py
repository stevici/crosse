import pygame
from settings import Settings

class Ship():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.rect.top = self.screen_rect.top
        
        #store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        #MOVEMENT FLAG
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #print("top: " + str(self.rect.top))
        #print("Bottom: " + str(self.rect.bottom))
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor
        

        self.rect.centerx = self.center
        self.rect.centery = self.center_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
