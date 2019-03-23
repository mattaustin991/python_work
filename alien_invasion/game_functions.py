import sys 
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):	
	"""Respond to key presses."""
	if event.key == pygame.K_RIGHT:
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
			
def update_screen(ai_settings, screen, ship, bullets):
	"""Update and refresh image on screen."""
	#Refresh screen with each loop iteration.
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	
	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	#Make most recent screen image visible
	pygame.display.flip()


def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	#Update bullet posotions.
	bullets.update()
	
	#Get rid of offscreen bullets.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
def fire_bullet(ai_settings, screen, ship, bullets):
	""" Fire bullet if limit not reached."""
	#Create new bullet and add to bullets group.
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)