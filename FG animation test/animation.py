"""
Animation module, including spritesheet 
and animation frame classes
Written Dec 29, 2015 by Benjamin Reed

Credit for original spritesheet implementation 
goes to Paul Vincent Craven at
programarcadegames.com
"""

import pygame as pyg
import constants as con

#class RectWithType(object):
class RectWithType(pyg.Rect):
	"""
	Class representing a collision rect with 
	a type flag defining what kind of collision 
	it is used for. Type flags:
	'Sprite' : Sprite/surface collision
	'Vuln'   : Attack vulnerability region ("hurtbox")
	'Attack' : Attack collision region ("hitbox")
	"""
	type = None
	#def __init__(self, (type, x, y, width, height)):
	def __init__(self, rect):
		super(RectWithType, self).__init__(rect[1], rect[2], rect[3], rect[4])
		#self.rect = pyg.Rect(rect[1], rect[2], rect[3], rect[4])
		self.type = rect[0]
		#self.x = rect[1]
		#self.y = rect[2]
		#self.width = rect[3]
		#self.height = rect[4]

class AnimationFrame(pyg.sprite.Sprite):
	"""
	Class representing a frame of animation
	and its associated collision rects
	"""
	#image = None
	#rects = []

	#def __init__(self, image, name, rects):
	def __init__(self, image, rects):
		super(AnimationFrame, self).__init__()
		self.image = image
		self.rects = []
		#self.name = name
		self.rect = self.image.get_rect()
		print "I'm a frame and these are my rects: "
		print self.rects
		for rect in rects:
			#print str(rect)
			self.rects.append(rect)
		print "After initialization:"
		print self.rects
		
class SpriteSheet(object):
	sprite_sheet = None
	"""
	Class used to grab images out of a sprite sheet.
	"""
	def __init__(self, file_name):
		"""
		Construct a SpriteSheet from image at file 
		path (file_name) and convert
		"""
		self.sprite_sheet = pyg.image.load(file_name).convert()
		
	def get_image(self, x, y, width, height):
		"""
		Grab a single image out of the sprite_sheet image
		Parameters: (x,y) for origin of frame you wish to
		slice, and (width, height) for the dimensions of 
		your desired slice
		"""
		image = pyg.Surface([width, height]).convert()
		image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
		
		# DEBUG: Set transparency color key to black
		image.set_colorkey(con.ALPHA_COLOR)
		
		return image