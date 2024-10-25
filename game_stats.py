class GameStats():
    """Track statistics fro alien invasion"""
    
    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #start alien invasion in an active state 
        self.game_active = False
        
        # High score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that cab change during the game"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0