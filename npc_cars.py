import pygame 
from pygame.sprite import Sprite

class NPC :
    """A Class to represent the npc cars"""
    
    def __init__(self , kar_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = kar_game.screen
        # Load the npc car image and set its rect attribute.
        self.image = pygame.image.load('assets/npc_cars/car1.bmp') 
        self.rect = self.image.get_rect()
        # Start each new car near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the npc car's exact horizontal position.
        self.x = float(self.rect.x)
        