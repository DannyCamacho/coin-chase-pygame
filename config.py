WIN_WIDTH = 1280
WIN_HEIGHT = 960
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 6
ENEMY_LAYER = 5
TARGET_LAYER = 4
BLOCK_LAYER = 3
PATH_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 2.5
ENEMY_SPEED = 2

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MAP_WIDTH = 40
MAP_HEIGHT = 30

tilemap = [
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
    'BT..BB...B.......BB..T..BB...B.......BBB',
    'BEB....B...B..B...TB..B....B...B..B...TB',
    'B.B.BB.B.BB..BBBB..BB.B.BB.B.BB..BBBB..B',
    'B.B....B.B....BB...BB.B....B.B....BB...B',
    'B....B.B...B......BBB....B.B...B......BB',
    'B.B.BB....BB.BBBB.....B.BB....BB.BBBB..B',
    'B.B..B.BB.........PBB.B..B.BB..........B',
    'B.BB...BB.BBB.BB..BBB.BB...BB.BBB.BB..BB',
    'B....B........BBB..BB....B........BBB..B',
    'B.B.BBB.BB.BB..B......B.BBB.BB.BB..B...B',
    'B.B..............B.BB.B..............B.B',
    'B.B.BBB.BBB.BB.BBB.BB.B.BBB.BB..BB.BBB.B',
    'B.T..........T.....BB.T..........T.....B',
    'BT..BB...B.......BB..T..BB...B.......BBB',
    'BEB....B...B..B...TB..B....B...B..B...TB',
    'B.B.BB.B.BB..BBBB..BB.B.BB.B.BB..BBBB..B',
    'B.B....B.B....BB...BB.B....B.B....BB...B',
    'B....B.B...B......BBB....B.B...B......BB',
    'B.B.BB....BB.BBBB.....B.BB....BB.BBBB..B',
    'B.B..B.BB..........BB.B..B.BB..........B',
    'B.BB...BB.BBB.BB..BBB.BB...BB.BBB.BB..BB',
    'B....B........BBB..BB....B........BBB..B',
    'B.B.BBB.BB.BB..B......B.BBB.BB.BB..B...B',
    'B.B..............B....B..............B.B',
    'B.B.BBB.BBB.BB.BBB....B.BBB.B.BB.B.BBB.B',
    'B.T..........T........T..........T.....B',
    'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB',
]
