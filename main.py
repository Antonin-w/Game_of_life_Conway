import pygame
import numpy as np
from cell_evol import new_grid
from cell_evol import draw_grid
import time
from PIL import Image

def main():

    num_iterations = 1000
    dim = 200
    twenty_percent = round(0.20*dim)
    eighty_percent = round(0.80*dim)

    cell_size = 2  # Size of each cell in pixels
    gridarray = np.zeros((dim, dim), dtype=int)

    # Randomly initialize cells values
    gridarray[twenty_percent:eighty_percent, twenty_percent:eighty_percent] = np.random.randint(2, size=(eighty_percent-twenty_percent, eighty_percent-twenty_percent))  # Fill the center

    # gridarray[52, 54] = 1  
    # gridarray[53, 54] = 1  
    # gridarray[54, 54] = 1  
    # gridarray[53, 52] = 1  
    # gridarray[54, 53] = 1  

    pygame.init()
    screen = pygame.display.set_mode((dim * cell_size, dim * cell_size))
    pygame.display.set_caption("Grid Array Visualization")
    
    clock = pygame.time.Clock()
    frames = []

    for _ in range(num_iterations):
        # Calculate the next generation
        gridarray = new_grid(gridarray)

        # Convert grid to an RGB frame
        frame = np.zeros((dim, dim, 3), dtype=np.uint8)
        frame[gridarray == 1] = [255, 255, 255]  # Set white for live cells
        frame[gridarray == 0] = [0, 0, 0]  # Set black for dead cells

        # Crop the frame
        cropped_frame = frame[twenty_percent:eighty_percent, twenty_percent:eighty_percent]
        frames.append(cropped_frame)

    # Save frames as a GIF using Pillow
    pillow_frames = []
    for frame in frames:
        img = Image.fromarray(frame)
        pillow_frames.append(img)

    pillow_frames[0].save('simulation_high_quality.gif',
                           save_all=True,
                           append_images=pillow_frames[1:],
                           duration=100, 
                           loop=0,
                           dpi=(300, 300))

if __name__ == "__main__":
    main()
