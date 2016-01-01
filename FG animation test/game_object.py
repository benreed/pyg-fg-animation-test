import pygame as pyg
import constants as con
from animation import *

class PlayerCharacter(object):
	anim_frames_R = []
	anim_frames_L = []
	direction = "R"
	current_frame = None
	frame_index = 0
	
	def __init__(self, chara):
		self.load_frames(chara)
		self.current_frame = self.anim_frames_R[1]
		print "All rects in current frame:"
		for element in self.current_frame.rects:
			print str(element)
		
	def draw(self, screen):
		screen.blit(self.current_frame.image, self.current_frame.rect)
		
	def load_frames(self, chara):
		sprite_sheet = SpriteSheet(chara["SPRITESHEET"])
		originX = originY = 0
		image_width = chara["IMAGE_WIDTH"]
		image_height = chara["IMAGE_HEIGHT"]
		rects = []
		
		for x in range (0, chara["NUM_OF_FRAMES"]):
			# Slice image
			image = sprite_sheet.get_image(originX, originY, image_width, image_height)
			name = str(chara["ANIMS"][0])
			rects = []
			
			# Make typed rects 
			#print "Length: " + str(len(chara["ANIMS"]))
			#for y in range (0, len(chara["ANIMS"])):
				#print str(chara["ANIMS"][y])
			print "Length of [anims]x: " + str(len(chara["ANIMS"][x]))
			for z in range (1, len(chara["ANIMS"][x])):
				print "All elements in [anims][x][z]:" + str(chara["ANIMS"][x][z])
				rect = RectWithType(chara["ANIMS"][x][z])
				rects.append(rect)
				
			# Combine rects and image to make an AnimationFrame
			#frame = AnimationFrame(image, name, rects)
			frame = AnimationFrame(image, rects)
			#print str(frame.name)
			
			# Finally, append that frame to the appropriate 
			#   member list 
			self.anim_frames_R.append(frame)
			
			originX += image_width
			
	def next_frame(self):
		self.frame_index += 1
		if self.frame_index > len(anim_frames_R):
			self.frame_index = 0