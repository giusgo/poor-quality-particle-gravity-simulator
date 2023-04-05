# PyGame library
import pygame
# Canvas creation
from canvas import particle_generator, screen_drawings
# Physics
from newton import physics



# WINDOW TITLE
WINDOW_TITLE = "Poor-quality particle simulator"

# DIMENSIONS OF THE WINDOW
WIDTH, HEIGHT = 1280, 720

# DISPLAY OBJECT
DISPLAY = pygame.display

# Set colors
COLORS = {
    # For the grid
    # WHITE
    'WHITE': (20, 20, 20),
    # BLACK
    'BLACK': (0, 0, 0),

    # For the particles
    'PARTICLE_COLORS': [
        # Green
        (144, 238, 144),
        # Yellow
        (255, 219, 88),
        # Blue
        (70, 130, 180),
        # Red
        (199, 21, 133),
        # Purple
        (66, 28, 82)
    ]
}

# SET CUSTOM FONT
FONT_SIZE = 16
FONT_SOURCE = 'misc/fonts/DotGothic16/DotGothic16-Regular.ttf'

# SCALE OF THE GRID AND PARTICLES
SCALE = 1

# CLOCK
CLOCK = pygame.time.Clock()

# Set simulation FPS
FPS = 60

# GRAVITATIONAL CONSTANT
scale_factor = (1e9 ** 2) / (WIDTH * HEIGHT)
G = 6.67430e-11 * scale_factor + (SCALE * 0.07)
# dt (time)
dt = 0.7

# --- FOR RANDOM GENERATION, SET THESE PROPERTIES:

# PARTICLES TO SPAWN
PARTICLES_NUM = 2

# MASS FOR THE PARTICLES
MIN_MASS, MAX_MASS = 1, 20

# PARTICLE TRAILS
TRAILS = False