import pygame

from settings import Settings

from pygame.sprite import Group

import game_functions as gf
 
from ship import Ship  

from game_stats  import GameStats

from button import Button

from Scoreboard import Scoreboard

  
def run_game(): 
    
    # intialize pygame, settings, screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make the play button
    play_button = Button(ai_settings, screen, "play")
    
    # create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb =    Scoreboard(ai_settings, screen, stats)
    
    
    # make a ship   
    ship = Ship(ai_settings,screen)  
    
    # make a group to store bullets in.
    bullets = Group() 
    aliens = Group() 
       
    # create a fleet of aliens.       
    gf.create_fleet(ai_settings, screen, ship, aliens) 
    
     # # make an alien 
    # alien = Alien(ai_settings, screen)
    
    # set the main loop for  the game
    while True:  
        
        # watch for keyboard and mouse events.
        gf.check_events( ai_settings, screen, stats, play_button, ship, aliens, bullets)
          
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
        if stats.game_active:  
        
            ship.update()
        
            gf.update_bullets(ai_settings, screen,stats, sb, ship ,aliens, bullets)
        
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
                
           
        # gf.update_screen(ai_settings,screen, stats, ship, aliens,  bullets, play_button)
        
# call the function 
run_game()

# ended on page 308