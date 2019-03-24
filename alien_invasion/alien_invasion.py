 
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf

def run_game():
	# Initialize game and create screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width
		,ai_settings.screen_height))		
	pygame.display.set_caption("Dominion Invasion")
	
	# Make a ship and group for bullets and aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	# Make an alien fleet.
	gf.create_fleet(ai_settings, screen,ship,aliens)
	
	# Start the main loop for the game.	
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings,screen,ship,aliens, bullets)
		gf.update_aliens(ai_settings,ship, aliens)
		gf.update_screen(ai_settings, screen, ship,aliens, bullets)
		
		
run_game()

