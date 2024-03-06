WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 5
ENEMY_LAYER = 4
BLOCK_LAYER = 3
PATH_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3
ENEMY_SPEED = 2.5

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MAP_WIDTH = int(WIN_WIDTH/TILESIZE)
MAP_HEIGHT = int(WIN_HEIGHT/TILESIZE)

tilemap = [
    'BBBBBBBBBBBBBBBBBBBB',
    'B.B..............BBB',
    'BEB....B...B..B....B',
    'B.B.BBBB..B..BBBB..B',
    'B.B....B.......B...B',
    'B.B..B.B...B......BB',
    'B.B.BB.B..BBBBBBB..B',
    'B.B..B.B.......P...B',
    'B.B....BBBBBBBBB..BB',
    'B.B..B..B.....B....B',
    'B.B.BB..BB..B..B...B',
    'B.B..............B.B',
    'B.BBBB..BBBBB..BBB.B',
    'B..................B',
    'BBBBBBBBBBBBBBBBBBBB',
]
