class Setting:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings.""" 
        # Background settings
        self.bg_speed = 10
        
        # Screen Settings
        self.name = "Kodak Kars"
        self.screen_width = 1100
        self.screen_height = 800
        self.bg_color = (20, 20, 230)
        
        # Car Settings
        self.scale = 1.6
        self.car_speed = 10
        self.car_width = 60 * self.scale
        self.car_height = 113 * self.scale
        # NPC Car Settings
        self.npc_speed = 15
        self.shoot = False
       
        # Bullet settings
        self.bullet_speed = 20
        self.bullet_width = 33
        self.bullet_height = 59
        self.bullet_allowed = 1
        
        
    