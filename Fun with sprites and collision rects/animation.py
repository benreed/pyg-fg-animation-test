"""
Module for sprite animation classes and functions
Written Dec 27, 2015 by Benjamin Reed
Version 0.0.1-alpha
"""
import pygame as pyg
import constants as con
from spritesheet import *

class AnimationFrame(object):
	"""
	Class to encompass both an animation 
	frame to display as well as any 
	and all associated collision rects
	"""
	def __init__(self, image, clsn_rect, vuln_rects, atk_rects=None):
		"""
		Makes an animation frame out of the 
		parameter image (pre-sliced by sprite
		sheet methods) and parameter rects 
		(retrieved from character constants)
		"""
		self.clsn_rect = clsn_rect
		self.vuln_rects = []
		self.atk_rects = []
		self.image = image
		# Append collision rects
		for rect in vuln_rects:
			self.vuln_rects.append(rect)