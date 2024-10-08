import pygame as pg
import numpy as np
from cell_evol import new_grid
import time

# Generate grid
dim = 100
gridarray = np.zeros((dim, dim)).astype(int)
gridarray[50, 50] = 1
gridarray[50, 51] = 1
gridarray[50, 52] = 1

## 

pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

# Specify the dimensions of the grid
grid_width = 100  # Number of blocks in width
grid_height = 100  # Number of blocks in height

# Calculate block size based on screen dimensions
screen_width, screen_height = screen.get_size()
block_size = min(screen_width // grid_width, screen_height // grid_height)

# Create the colors array
colors = np.array([white, black])

# Create a surface for the grid
surface = pg.surfarray.make_surface(colors[gridarray])

# Scale the surface to the calculated block size
scaled_surface = pg.transform.scale(surface, (grid_width * block_size, grid_height * block_size))

clock = pg.time.Clock()
frame_count = 0
update_interval = 3  # Update every 3 seconds
last_update_time = time.time()  # Store the current time

evolution_count = 0
evolution_limit = 10
update_frequency = 10  # Update every 10 frames




pg.quit()
