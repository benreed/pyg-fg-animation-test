"""
Pseudo-utility to test animation implementation for 
fighting game prototype
Written Dec 18, 2015 by Benjamin Reed
	
Credit for this implementation goes to Sean J. McKiernan
(Mekire) at /r/pygame
https://github.com/Mekire
"""
import sys

import pygame as pyg
import constants as con
from game_object import *

# -------- Global constants --------
# Game window caption
WINDOW_CAPTION = "Animation Test"

# Game window dimensions
SCREEN_SIZE = (800, 600)

# Target frame rate
TARGET_FPS = 60

class App:
	"""
	A class to cleanly encapsulate main game loop phases,
	including initialization, event handling, and state 
	updates
	"""
	# Debug flag
	debug = True
	
	def __init__(self):
		"""
		Get a reference to the display surface; set up required attributes;
		and instantiate player objects
		"""
		self.screen = pyg.display.get_surface()
		self.screen_rect = self.screen.get_rect()
		self.clock = pyg.time.Clock()
		self.fps = TARGET_FPS
		self.done = False
		self.keys = pyg.key.get_pressed()
		# Instantiate game object members here
		self.player = PlayerCharacter(con.PHOEBE)
		
	def event_loop(self):
		"""
		Method encompassing one trip through the event queue
		Called within main_loop()
		"""
		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				self.done = True
			elif event.type in (pyg.KEYUP, pyg.KEYDOWN):
				self.keys = pyg.key.get_pressed()
				
	def render(self):
		"""
		Method encompassing drawing to the screen and updating
		the display
		"""
		# Wipe frame 
		self.screen.fill(con.BG_COLOR) 
		
		# Draw level
		
		# Draw game objects
		self.player.draw(self.screen)
		pyg.draw.rect(self.player.current_frame.image, con.WHITE, self.player.current_frame.rect, 1)
		if self.debug:
			for rect in self.player.current_frame.rects:
				if rect.type == "Sprite":
					pyg.draw.rect(self.player.current_frame.image, con.GREEN, (rect.x, rect.y, rect.width, rect.height), 1)
				elif rect.type == "Vuln":
					pyg.draw.rect(self.player.current_frame.image, con.BLUE, (rect.x, rect.y, rect.width, rect.height), 1)
		
		# Update display
		pyg.display.flip()
		
	def main_loop(self):
		"""
		Encompasses one rep of the main game loop
		"""
		while not self.done:
			self.event_loop()
			# (update game objects here)
			self.render()
			self.clock.tick(self.fps)
		
def main():
	"""
	Main program function. Performs Pygame initialization,
	starts, and exits the program.
	"""
	pyg.init()
	pyg.display.set_caption(WINDOW_CAPTION)
	pyg.display.set_mode(SCREEN_SIZE)
	App().main_loop()
	pyg.quit()
	sys.exit()
	
if __name__ == "__main__":
	main()