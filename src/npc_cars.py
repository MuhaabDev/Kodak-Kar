import pygame 
from pygame.sprite import Sprite
from src.settings import Setting

class NPC(Sprite):
    """A Class to represent the npc cars"""
    
    def __init__(self , kar_game , random_lane  , car_skin , acceleration ):
        """Initialize the npc cars and set its starting position."""
        super().__init__()
        self.setting = Setting()
        self.screen = kar_game.screen
        self.screen_rect = kar_game.screen.get_rect()
        
        #Load the npc cars image , scale it ,set its rect attribute.
        self.npc_cars_images_path = ['assets/npc_cars/car1.bmp', 'assets/npc_cars/car2.bmp', 'assets/npc_cars/car3.bmp']              
        self.lanes_positions_x = { 1 : 162 , 2 : 392 , 3 : 622 , 4 : 842 }
        self.rect_image = pygame.image.load( self.npc_cars_images_path[car_skin])
        self.rect_image = pygame.transform.scale(self.rect_image , (self.setting.car_width,self.setting.car_height))
        self.rect = self.rect_image.get_rect()
        self.rect.x = self.lanes_positions_x[random_lane]
        self.rect.y = -400
        self.y = float(self.rect.y)
        
        # to speed up the car every five seconds
        self.acceleration = acceleration
            
    def update(self):
        """Update the npc car position"""
        # Update the exact position of the npc.
        self.y += self.setting.npc_speed + self.acceleration
        # Update the rect position.
        self.rect.y = self.y
          
    def blitme(self):  
        """Draw the car at its current location."""
        self.screen.blit( self.rect_image ,  self.rect )
         
    def load_cars(self , paths):
         """"Load the npc cars and their rect."""
         for index , path in enumerate(paths):
            try:
                image = pygame.image.load(path)
                image_scaled = pygame.transform.scale(image ,(self.setting.car_width,self.setting.car_height))
                car_rect = image_scaled.get_rect()
                self.images.append(image_scaled)
                self.images_rect.append(car_rect)
                print(f'NPC Car {index+1} Loaded Successfuly')
            except Exception as e:
                print(f'Error at loading Car {index+1}')