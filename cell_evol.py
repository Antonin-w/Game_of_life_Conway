# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import numpy as np

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