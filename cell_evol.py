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
    if row < 2 or row >= matrix.shape[0] - 2 or column < 2 or column >= matrix.shape[1] - 2:
        return 0  # Cells in the border remain 0
    
    neighbours_lives = sum_neighbours(matrix, row, column)
    if matrix[row, column] == 1:
        return 0 if neighbours_lives < 2 or neighbours_lives > 3 else 1
    else:
        return 1 if neighbours_lives == 3 else 0

def new_grid(matrix):
    new_grid = matrix.copy()
    for row in range(1, matrix.shape[0]):
        for column in range(1, matrix.shape[1]):
            new_grid[row, column] = cell_evol(matrix, row, column)

    return new_grid

def draw_grid(screen, grid, cell_size, dim):
    twenty_porcent = round(0.20*dim)
    eighty_porcent = round(0.80*dim)
    for row in range(twenty_porcent, eighty_porcent):  # Display only rows 100 to 399
        for column in range(twenty_porcent, eighty_porcent):  # Display only columns 100 to 399
            color = (255, 255, 255) if grid[row, column] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (column * cell_size, row * cell_size, cell_size, cell_size))

