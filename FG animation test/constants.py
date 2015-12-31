"""
Constant values of application scope
Written Dec 15, 2015 by Benjamin Reed
Version 0.0.1-alpha
"""

"""
Game constants
"""
# Game version
GAME_VERSION = "0.0.1-alpha"

# Target frame rate
TARGET_FPS = 60

# Primitive colors
BLACK    =    (   0,   0,   0)
BLUE     =    (   0,   0, 255)
CYAN     =    (   0, 255, 255)
GREEN    =    (   0, 255,   0)
PURPLE   =    ( 255,   0, 255)
RED      =    ( 255,   0,   0)
WHITE    =    ( 255, 255, 255)
YELLOW   =    ( 255, 255,   0)

BG_COLOR =    (   0, 155, 200)
ALPHA_COLOR = ( 255,   0, 192)

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Game window caption
WINDOW_CAPTION = "Prototype " + GAME_VERSION

"""
Character constants
"""

# This is a list because standard dicts are 
#   unsorted -- I need to make sure frame data
#   occurs in a fixed order corresponding to 
#   the order in which images are sliced from 
#   the sprite sheet
PHO_ANIM = (
	( "IDLE_1",   ("Sprite", 3,3,10,10), ("Vuln", 10, 10, 10, 20) ),
	( "IDLE_1",   ("Sprite", 30,30,20,10) )
)

PHOEBE = {
	"NAME"          : "Phoebe",
	"SPRITESHEET"   : "img/nov2015_spritesheet_2.png",
	"ANIMS"         : PHO_ANIM,
	"IMAGE_WIDTH"   : 120,
	"IMAGE_HEIGHT"  : 114,
	"NUM_OF_FRAMES" : 2
}