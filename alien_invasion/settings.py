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
		self.bullet_speed_factor = 4.5
		self.bullet_width = 6
		self.bullet_height = 10
		self.bullet_color = 70,110,255
		self.bullets_allowed = 20
		
		#Alien Settings
		self.alien_speed_factor = 2
		self.fleet_drop_speed = 10
		# fleet direction of 1 means right; -1 means left.
		self.fleet_direction = 1
