"""
Utility for testing character animation and rect members
Written Dec 26, 2015 by Benjamin Reed
	
Credit for this implementation goes to Sean J. McKiernan
(Mekire) at /r/pygame
https://github.com/Mekire
"""
import sys

import pygame as pyg
import constants as con
import character_con as chara
from game_object import *

# -------- Global constants --------
# Game window caption
WINDOW_CAPTION = "Animation test"

# Game window dimensions
SCREEN_SIZE = (200, 200)

# Target frame rate
TARGET_FPS = 60

class App:
	"""
	A class to cleanly encapsulate main game loop phases,
	including initialization, event handling, and state 
	updates
	"""
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
		self.sprite = GlorifiedSprite(chara.PHOEBE)
		
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
				if event.type == pyg.KEYDOWN:
					# Right key: Next image in list
					if event.key == pyg.K_RIGHT:
						self.sprite.next_image()
					# Left key: Previous image in list
					elif event.key == pyg.K_LEFT:
						self.sprite.prev_image()
					# Down key: Flip sprite direction
					elif event.key == pyg.K_DOWN:
						self.sprite.flip_image()
				
	def render(self):
		"""
		Method encompassing drawing to the screen and updating
		the display
		"""
		# Wipe frame 
		self.screen.fill(con.BG_COLOR)
		
		# Draw sprite
		self.sprite.draw(self.screen)
		
		# Draw rects
		if self.debug:
			pyg.draw.rect(self.screen, con.GREEN, self.sprite.rect, 1)
			pyg.draw.line(self.sprite.image, con.WHITE, (self.sprite.drawing_axis, self.sprite.rect.y), (self.sprite.drawing_axis, self.sprite.rect.height), 1)
		
		# Flip display
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