# display settings
DEFAULT_IMAGE_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

# Images
BG_IMAGE_PATH = 'graphics/0/bg-grid.png'
GRID_IMAGE_PATH = 'graphics/0/gridline.png'
GAME_INDICES= [1, 2, 3] # 0 and 4 are outside of play area
SYM_PATH = 'graphics/0/symbols'

# Text
TEXT_COLOR = 'White'
UI_FONT = 'graphics/font/kidspace.demo.ttf'
UI_FONT_SIZE = 40
WIN_FONT_SIZE = 110

# 5 Symbols for demo
symbols = {
    'diamond': f"{SYM_PATH}/0_diamond.png",
    'floppy': f"{SYM_PATH}/0_floppy.png",
    'hourglass': f"{SYM_PATH}/0_hourglass.png",
    'seven': f"{SYM_PATH}/0_seven.png",
    'telephone': f"{SYM_PATH}/0_telephone.png",
}

# 4 symbols for more wins
#symbols = {
    #'diamond': f"{SYM_PATH}/0_diamond.png",
    #'floppy': f"{SYM_PATH}/0_floppy.png",
    #'hourglass': f"{SYM_PATH}/0_hourglass.png",
    #'hourglass2': f"{SYM_PATH}/0_hourglass.png",
    #'telephone': f"{SYM_PATH}/0_telephone.png",
#}