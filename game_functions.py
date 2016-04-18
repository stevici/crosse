import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type  == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(event, ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True    
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            if event.key == pygame.K_UP:
                ship.moving_up = True 

def check_keyup_events(event, ship):
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False    
            if event.key == pygame.K_DOWN:
                ship.moving_down = False
            if event.key == pygame.K_UP:
                ship.moving_up = False  
