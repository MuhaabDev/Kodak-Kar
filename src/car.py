import pygame
from src.settings import Setting

class Kar:
   """ A Class To manage the Car """
   
   def __init__(self , kar_game):
       """Initialize the car and set its starting position."""
       self.setting = Setting()
       self.screen = kar_game.screen
       self.screen_rect = kar_game.screen.get_rect()
       
       # Load the car image and get its rect
       self.image = pygame.image.load('assets/player_cars/red_porsche.bmp')
       self.image = pygame.transform.scale(self.image,(self.setting.car_width,self.setting.car_height ))
       self.rect = self.image.get_rect()
       
       #Start car at the bottom center of the screen.
       self.rect.midbottom = self.screen_rect.midbottom
       
       # Store a float for the ship's exact horizontal position.
       self.x = float(self.rect.x)
       
       # Movement flag; start with a car that's not moving.
       self.moving_right = False
       self.moving_left = False
       
       
   def blitme(self):
        """Draw the car at its current location."""
        self.screen.blit(self.image , self.rect)
       
        
   def update(self):
        """Update the car's position based on the movement flag."""
        if self.moving_right and self.rect.x < self.setting.screen_width - 245 :
            self.x += self.setting.car_speed
        if self.moving_left and self.rect.x > 160 :
            self.x -= self.setting.car_speed
        self.rect.x = self.x