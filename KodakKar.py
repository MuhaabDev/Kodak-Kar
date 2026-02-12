import sys
import pygame

from settings import Setting
from car import Kar
from background import BackGround
from bullets import Bullet
from npc_cars import NPC

class KodakKar:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        # Intialiaizing Objects
        self.settings = Setting()
        
        # Intialiaizing Game Settings
        pygame.display.set_caption(self.settings.name)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width , self.settings.screen_height))
        
        # Intialiaizing Objects
        self.car = Kar(self)
        self.background = BackGround(self)
        self.bullets = pygame.sprite.Group()
        
          
    def run_game(self): 
        """Start the main loop for the game."""
        while True:
            self.check_event()
            self.car.update()
            self._update_bullet()
            self.background.update()
            self.update_screen() 
            self.clock.tick(60)
           
        

    def check_event(self):
        """Watch for keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
      
      
                                
    def _check_keydown_events(self , event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullet_allowed:
                self._fire_bullet()
     
     
             
    def _check_keyup_events(self , event):
       """Respond to key releases."""
       if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
       elif event.key == pygame.K_LEFT:
            self.car.moving_left = False
     
     
                           
    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.background.blitme()
        self.car.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
       
       
        
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
      
      
      
    def _update_bullet(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)
                
                
   