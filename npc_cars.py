import pygame 
from settings import Setting
from pygame.sprite import Sprite

class NPC(Sprite):
    """A Class to represent the npc cars"""
    
    def __init__(self , kar_game):
        """Initialize the npc cars and set its starting position."""
        super().__init__()
        self.setting = Setting()
        self.screen = kar_game.screen
        self.screen_rect = kar_game.screen.get_rect()
        
        # Load the npc cars image , scale it ,set its rect attribute.
        #self.npc_cars_images_path = ['assets/npc_cars/car1.bmp', 'assets/npc_cars/car2.bmp', 'assets/npc_cars/car3.bmp']
        #self.images = list()
        #self.images_rect = list()
        #self.load_cars(self.npc_cars_images_path)
        # Intializing Lanes Capacity and Positions
        #self.lanes_capacity = {'lane 1' : 0 ,'lane 2' : 0 ,
                            #    'lane 3' : 0 , 'lane 4' : 0 
                            # }
        # self.lanes_positions_x = {'lane 1' : (162) ,'lane 2' : (392) ,
                                #   'lane 3' : (622) , 'lane 4' : (842) 
                            # }
        
        self.npc_rect_image = pygame.image.load('assets/npc_cars/car1.bmp')
        self.npc_rect_image = pygame.transform.scale(self.npc_rect_image , (self.setting.car_width,self.setting.car_height))
        self.npc_rect = self.npc_rect_image.get_rect()
        self.npc_rect.x = 392
        self.npc_rect.y = -100
        self.y = float(self.npc_rect.y)
        
      
    def update(self):
        """Update the npc car position"""
        # Update the exact position of the npc.
        self.y += self.setting.npc_speed
        # Update the rect position.
        self.npc_rect.y = self.y
      
       
    def blitme(self):  
        """Draw the car at its current location."""
        self.screen.blit( self.npc_rect_image ,  self.npc_rect )
       
       
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