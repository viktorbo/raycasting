from math import pi

# WINDOW
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
WINDOW_CENTER_W = WINDOW_WIDTH // 2
WINDOW_CENTER_H = WINDOW_HEIGHT // 2
WINDOW_CENTER = (WINDOW_CENTER_W, WINDOW_CENTER_H)
WINDOW_FPS = 60

# COLORS (RGB)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

# PLAYER
PLAYER_DEFAULT_POSITION = WINDOW_CENTER
PLAYER_VIEW_ANGLE = 0
PLAYER_VIEW_ANGLE_SPEED = 0.04
PLAYER_SPEED = 5
PLAYER_CIRCLE_RADIUS = 0.025 * (WINDOW_CENTER_W + WINDOW_CENTER_H)

# RAYS
RAY_DISTANCE = PLAYER_CIRCLE_RADIUS + 200
FOV_ANGLE = pi / 3
NUM_RAYS = 120
DELTA_ANGLE = FOV_ANGLE / NUM_RAYS

# OBJECTS
TILE_SIZE = 50
