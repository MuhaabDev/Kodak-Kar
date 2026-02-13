import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the car."""
    
    def __init__(self , kar_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = kar_game.screen
        self.setting = kar_game.settings
        
       # Load the bullet image
        self.image = pygame.image.load('assets/rockets/bullet.bmp')
        self.image = pygame.transform.scale(self.image,
            (self.setting.bullet_width,self.setting.bullet_height))
        self.rect = self.image.get_rect()
        self.rect.midbottom = kar_game.car.rect.midtop
        
        # Store the bullet's position as a float.
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.setting.bullet_speed
        # Update the rect position.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image , self.rect)