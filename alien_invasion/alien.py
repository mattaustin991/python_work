import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	
	def __init__(self, ai_settings, screen):
		""" Initialize the alien and set start position."""
		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Load the alien imageand set its rect atribute.
		self.image = pygame.image.load('images/domship3.bmp')
		self.rect = self.image.get_rect()
		
		#Start each new alien neer the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Store the alens exact postion.
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)
	
	def check_edges(self):
		"""Return True if alien is at edge of the screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
			
	def update(self):
		""" Move the alien."""
		self.x += (self.ai_settings.alien_speed_factor * 
						self.ai_settings.fleet_direction)
		self.rect.x = self.x
		
