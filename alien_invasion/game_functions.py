import sys 
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):	
	"""Respond to key presses."""
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):				
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
			
def update_screen(ai_settings, screen, ship,aliens, bullets):
	"""Update and refresh image on screen."""
	#Refresh screen with each loop iteration.
	screen.fill(ai_settings.bg_color)
	
	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()	
	aliens.draw(screen)
	#Make most recent screen image visible
	pygame.display.flip()


def update_bullets(ai_settings,screen,ship,aliens,bullets):
	"""Update position of bullets and get rid of old bullets."""
	#Update bullet posotions.
	bullets.update()
	
	#Get rid of offscreen bullets.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_alien_bullet_collosions(ai_settings,screen,ship,aliens,bullets)
	
def check_alien_bullet_collosions(ai_settings,screen,ship,aliens,bullets):
	"""check for bullets that have hit aliens."""
	#If so get rid of alien.
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if len(aliens) == 0:
		# Destroy existing bullets and create new fleet.
		bullets()
		create_fleet(ai_settings,screen,ship,aliens)
def fire_bullet(ai_settings, screen, ship, bullets):
	""" Fire bullet if limit not reached."""
	#Create new bullet and add to bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
		
def get_number_aliens_x(ai_settings,alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	"""Determin the number of rows for alien fleet."""
	available_space_y = (ai_settings.screen_height -
	(3 * alien_height) - ship_height + 12)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
	
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""Create an alien and place it in row.""" 
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number		
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
	
def create_fleet(ai_settings,screen,ship,aliens):
	""" Create an alien fleet to fit screen."""
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(
	ai_settings
	,alien.rect.width)
	
	number_rows = get_number_rows(
	ai_settings
	,ship.rect.height
	,alien.rect.height)
		
	# Create the fleet of aliens 
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#Create an alien and place it in row.
			create_alien(
			ai_settings
			,screen
			,aliens
			,alien_number
			,row_number)

def check_fleet_edges(ai_settings, aliens):
	""" Respond appropiatly if any aliens have reached the edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	""" Drop the whole fleet and change direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,ship, aliens):
	""" Update the postions of all aliens in the fleet."""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	#Look for ship alien collisions.
	if pygame.sprite.spritecollideany(ship,aliens):
		print('Ship Hit!')
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
