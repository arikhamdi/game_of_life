"""
Conway’s Game of life
The Rules

BIRTH: a new cell is born if it is surrounded by exactly three live cells.
LIFE: a cell lives on as long as it is surrounded by two or three live cells.
DEATH: a cell dies of loneliness if it is surrounded by fewer than two live cells.
A cell dies of overcrowding if it is surrounding by four or more live cells.
"""
import random
import glider_gun, glider


# build the grid whit a 2D list
height = 150
width = 150

def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0,1)


grid_model = [0] * height
next_grid_model = [0] * height

for i in range(height):        
    grid_model[i] = [0] * width
    next_grid_model[i]  = [0] * width


randomize(grid_model, width, height)


# iterate throuh the 2D list to check the stat of every cells
# apply the rules to every cells
def next_gen():
    global grid_model, next_grid_model

    for i in range(0, height):
        for j in range(0, width):
            cell = 0
            count = count_neighbors(grid_model, i, j)
            
            if grid_model[i][j] == 0:
                if count == 3:
                    cell = 1
            elif grid_model[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
            next_grid_model[i][j] = cell
            
    temp = grid_model
    grid_model = next_grid_model
    next_grid_model = temp
                
            
                

# count neighbors to know what rule needs to be applied
def count_neighbors(grid, row, col):
    count = 0
    
    if row-1 >= 0:
        count = count + grid[row-1][col]
    if (row-1 >= 0) and (col-1 >= 0):
        count = count + grid[row-1][col-1]
    if (row-1 >= 0) and (col+1 < width):
        count = count + grid[row-1][col+1]
    if col-1 >= 0:
        count = count + grid[row][col-1]
    if col + 1 < width:
        count = count + grid[row][col+1]
    if row + 1 < height:
        count = count + grid[row+1][col]
    if (row + 1 < height) and (col-1 >= 0):
        count = count + grid[row+1][col-1]
    if (row + 1 < height) and (col+1 < width):
        count = count + grid[row+1][col+1]
        
    return count

glider_gun_pattern = glider_gun.glider_gun_pattern
glider_pattern = glider.glider_pattern

def load_pattern(pattern, x_offset=0, y_offset=0):
    global grid_model
    for i in range(0, height):
        for j in range(0, width):
            grid_model[i][j] = 0

    j = y_offset
    
    for row in pattern:
        i = x_offset
        for value in row:
            grid_model[i][j] = value
            i = i + 1
        j = j + 1

if __name__ == '__main__':
    next_gen()
