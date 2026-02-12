import pygame

class BackGround:
    
    def __init__(self , kar_game):
        # Load the game screen
        self.screen = kar_game.screen
        self.screen_rect = kar_game.screen.get_rect()
        
        # load the background image 
        self.background_image = pygame.image.load('assets/background/full_background.png')
        self.background_image = pygame.transform.scale(self.background_image,(1200,3000))
        self.background_rect = self.background_image.get_rect()
        self.background_rect.midbottom = self.screen_rect.midbottom
        self.y_intial = self.background_rect.y
        
        self.y = float(self.background_rect.y)
        self.speed = kar_game.settings.bg_speed
        self.reset = False
        self.counter = 0
        
    def update(self):
        """Move the background down the screen""" 
        # Update the exact position of the background.
        self.y += self.speed
        # Update the rect position
        self.background_rect.y = self.y
        self.counter += 1
        
        if self.counter > 172 : 
            self.y = self.y_intial
            self.background_rect.y = self.y
            self.counter = 0
            
    def blitme(self):
        """Draw the car at its current location."""
        self.screen.blit(self.background_image , self.background_rect)
        
        
        
        