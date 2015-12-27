import pygame as pyg
import character_con as chara
from spritesheet import *

class GlorifiedSprite(pyg.sprite.Sprite):
	# -------- Lists for animation frames --------
	all_frames_R = []
	all_frames_L = []
	image_index = 0
	direction = "R"

	def __init__(self, character):
		super(GlorifiedSprite, self).__init__()
		self.init_frames()
		self.image = self.all_frames_R[self.image_index]
		self.rect = self.image.get_rect()
		self.rect.x = 40
		self.rect.y = 40
		self.drawing_axis = character["AXIS"]
		
	def init_frames(self):
		sprite_sheet = SpriteSheet("img/nov2015_spritesheet_2.png")
		originX = 0
		originY = 0
		image_width = 120
		image_height = 114
		
		for x in range (0, 27):
			image = sprite_sheet.get_image(originX, originY, image_width, image_height)
			self.all_frames_R.append(image)
			originX += image_width
			
		originX = 0
		for x in range (0, 27):
			image = sprite_sheet.get_image(originX, originY, image_width, image_height)
			image = pyg.transform.flip(image, True, False)
			self.all_frames_L.append(image)
			originX += image_width
			
	def draw(self, surface):
		surface.blit(self.image, self.rect)
		
	def flip_image(self):
		if self.direction == "R":
			self.direction = "L"
			self.image = self.all_frames_L[self.image_index]
		else:
			self.direction = "R"
			self.image = self.all_frames_R[self.image_index]
		
	def next_image(self):
		self.image_index += 1
		if self.image_index >= len(self.all_frames_R):
			self.image_index = 0
		if self.direction == "R":
			self.image = self.all_frames_R[self.image_index]
		else: 
			self.image = self.all_frames_L[self.image_index]
			
	def prev_image(self):
		self.image_index -= 1
		if self.image_index < 0:
			self.image_index = len(self.all_frames_R)-1
		if self.direction == "R":
			self.image = self.all_frames_R[self.image_index]
		else: 
			self.image = self.all_frames_L[self.image_index]