"""
Character constants module for fighting game prototype
Stores constant character-specific attributes for 
initialization -- frame-specific collision rects, sprite
drawing axes, and of course character names
Written Dec 27, 2015 by Benjamin Reed
Version 0.0.1-alpha
"""

"""
	Character constants: Phoebe
"""
# Member format:
#	[0] : Vertical axis (relative to sprite slice surface)
#	[1] : Head rect
#	[2] : Body rect
#	[3] : Legs rect
#	Additional members: Attack or special trigger rects
PHO_ANIMS = {
	"IDLE_1" : (40,
				(),(),(25, 74, 30, 40))
}

PHOEBE = {
	"NAME"         : "Phoebe",
	"AXIS"         : 40,
	"SPRITESHEET"  : "img/nov2015_spritesheet_2.png",
	"ANIMS"		   : PHO_ANIMS,
	"FRAME_WIDTH"  : 120,
	"FRAME_HEIGHT" : 114
}