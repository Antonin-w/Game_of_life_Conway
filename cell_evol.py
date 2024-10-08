# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import numpy as np
import pygame
import sys

def sum_neighbours(matrix, row, column):
    neighbours = [matrix[row-1, column-1],
                    matrix[row-1, column],
                    matrix[row-1, column+1],
                    matrix[row, column-1], 
                    matrix[row, column+1],
                    matrix[row+1, column-1],
                    matrix[row+1, column],
                    matrix[row+1, column+1]]
                     
    return sum(neighbours)

def cell_evol(matrix, row, column):
    neighbours_lives = sum_neighbours(matrix, row, column)
    if matrix[row, column] == 1:
        return 0 if neighbours_lives < 2 or neighbours_lives > 3 else 1
    else:
        return 1 if neighbours_lives == 3 else 0

def new_grid(matrix):
    new_grid = matrix.copy()
    for row in range(1, matrix.shape[0]-1):
        for column in range(1, matrix.shape[1]-1):
            new_grid[row, column] = cell_evol(matrix, row, column)

    return new_grid


def draw_grid(screen, grid, cell_size):
    for row in range(grid.shape[0]):
        for column in range(grid.shape[1]):
            color = (255, 255, 255) if grid[row, column] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (column * cell_size, row * cell_size, cell_size, cell_size))

def main():
    dim = 100
    cell_size = 6  # Size of each cell in pixels
    gridarray = np.zeros((dim-2, dim-2))
    gridarray = np.pad(gridarray, pad_width=1, mode='constant', constant_values=0)  # Add a border of 0s

    gridarray[2, 4] = 1  
    gridarray[3, 4] = 1  
    gridarray[4, 4] = 1  
    gridarray[3, 2] = 1  
    gridarray[4, 3] = 1  

    pygame.init()
    screen = pygame.display.set_mode((dim * cell_size, dim * cell_size))
    pygame.display.set_caption("Grid Array Visualization")
    
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        next_generation = new_grid(gridarray)
        
        # Update the grid array with the next generation
        gridarray[1:-1, 1:-1] = next_generation[1:-1, 1:-1]
        gridarray[-1, :] = 0  # Last row
        gridarray[:, -1] = 0  # Last column

        screen.fill((0, 0, 0))  # Clear screen with black
        draw_grid(screen, gridarray, cell_size)
        pygame.display.flip()
        
        clock.tick(30)  # Control the speed of the simulation

if __name__ == "__main__":
    main()
