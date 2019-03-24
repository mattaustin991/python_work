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
		self.image = pygame.image.load('images/dominion_attackship.bmp')
		self.rect = self.image.get_rect()
		
		#Start each new alien neer the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Store the alens exact postion.
		self.x = float(self.rect.x)
		
	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)
