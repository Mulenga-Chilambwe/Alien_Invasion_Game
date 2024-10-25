import pygame

class Settings():
    """A class stores all settings for Alien Invsion."""
    
    # initializing the class
    def __init__(self):
        """intialize the game's static setting"""
        # inittlize pygame 
        pygame.init()
        
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # load the image from the folder
        self.background_image = pygame.image.load('images/sky.jpeg')
        
         
        # Scale the image to fit the screen
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        
        # ship setting 
        self.ship_speed_factor = 2
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 235, 44, 10
        self.bullets_allowed = 6
        
        # alien settings 
        self.alien_speed_factor = 1.2
        self.fleet_drop_speed = 10
        
        # fleet_direction of 1 represents right; -1 representts left.
        self.fleet_direction = 1
        
        # how quickly the game speed up 
        self.speedup_scale = 1.1
        
        # how quickly the alien points increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_setting()
        
    def initialize_dynamic_setting(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction  = 1
        
        # scoring 
        self.alien_points = 50
        
    
    def increase_speed (self):
        """Increase speed settings and alien point vaalue."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)