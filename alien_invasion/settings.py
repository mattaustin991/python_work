class Settings():
	"""A clas to store settings for Alien Invasion. """
	
	def __init__(self):
		"""Initialize the game settings."""
		#Screen Settings
		self.screen_width = 1600
		self.screen_height = 1200
		self.bg_color = (0, 0, 0)
		
		#Ship settings
		self.ship_speed_factor = 10
		
		#Bullet settings 
		self.bullet_speed_factor = 3.75
		self.bullet_width = 5
		self.bullet_height = 8
		self.bullet_color = 90,195,255
		self.bullets_allowed = 3
