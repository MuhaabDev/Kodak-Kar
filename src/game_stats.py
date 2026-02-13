class GameStats:
    """Track statistics for KODAK KAR."""
    
    def __init__(self, kar_game):
        """Initialize statistics."""
        self.settings = kar_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.car_lives = self.settings.car_lives
        self.score = 0
        
        
    