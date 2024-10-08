import pygame
import numpy as np
from cell_evol import new_grid
from cell_evol import draw_grid
import time

def main():

    dim = 300
    twenty_porcent = round(0.20*dim)
    eighty_porcent = round(0.80*dim)

    cell_size = 2  # Size of each cell in pixels
    # Create a 500x500 grid, padding with zeros for the border
    gridarray = np.zeros((dim, dim), dtype=int)
    # Randomly initialize the inner 300x300 area
    gridarray[twenty_porcent:eighty_porcent, twenty_porcent:eighty_porcent] = np.random.randint(2, size=(eighty_porcent-twenty_porcent, eighty_porcent-twenty_porcent))  # Fill the center

    # gridarray[52, 54] = 1  
    # gridarray[53, 54] = 1  
    # gridarray[54, 54] = 1  
    # gridarray[53, 52] = 1  
    # gridarray[54, 53] = 1  

    pygame.init()
    screen = pygame.display.set_mode((dim * cell_size, dim * cell_size))
    pygame.display.set_caption("Grid Array Visualization")
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate the next generation
        gridarray = new_grid(gridarray)
        
        screen.fill((0, 0, 0))  # Clear screen with black
        draw_grid(screen, gridarray, cell_size, dim)
        pygame.display.flip()
        
        clock.tick(20)  # Control the speed of the simulation

if __name__ == "__main__":
    main()

