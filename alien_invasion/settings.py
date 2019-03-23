class Settings():
	"""A clas to store settings for Alien Invasion. """
	
	def __init__(self):
		"""Initialize the game settings."""
		#Screen Settings
		self.screen_width = 1920
		self.screen_height = 1200
		self.bg_color = (0, 0, 0)
		
		#Ship settings
		self.ship_speed_factor = 10
		
		#Bullet settings 
		self.bullet_speed_factor = 3.25
		self.bullet_width = 6
		self.bullet_height = 12
		self.bullet_color = 95,180,255
		self.bullets_allowed = 3
