import pygame.font

class Button():
    
    def __init__(self, ai_settings, screen, msg):
        """initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect
        
        # set the dimension and properties of the button 
        self.width, self.height = 200, 50
        self.button_color = (230, 230, 230)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the buttons rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center =  self.rect.center
        
        # the button message needs to be prepped only once.
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,  self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    
    def draw_button(self):
        # draw blank button and then draaw message 
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)                