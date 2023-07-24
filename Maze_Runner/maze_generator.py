# Importing the pygame library
import pygame
# Importing the choice function from random module
from random import choice

# Defining the resolution of the game window
RES = WIDTH, HEIGHT = 1202, 902
# Defining the size of each tile in the maze
TILE = 100
# Calculating the number of columns and rows in the maze based on the resolution and tile size
cols, rows = WIDTH // TILE, HEIGHT // TILE


# Creating a class called Cell
class Cell:

    # Constructor method for Cell class, takes x and y as parameters
    def __init__(self, x, y):
        # Initializing the x and y coordinates of the cell
        self.x, self.y = x, y
        # Initializing walls dictionary with all walls set to True
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        # Initializing visited flag to False
        self.visited = False
        # Setting the thickness of the walls
        self.thickness = 4

    # Method to draw the cell, takes the screen as parameter
    def draw(self, sc):
        # Calculating the actual coordinates of the cell
        x, y = self.x * TILE, self.y * TILE

        if self.walls['top']:  # Checking if top wall exists
            # Drawing the top wall
            pygame.draw.line(sc, pygame.Color('darkorange'),  # Setting the color of the line
                             (x, y), (x + TILE, y), self.thickness)  # Drawing a line from (x, y) to (x + TILE, y)

        # Similarly checking and drawing other walls if they exist
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkorange'),
                             (x + TILE, y), (x + TILE, y + TILE), self.thickness)  # Drawing a line from (x + TILE, y) to (x + TILE, y + TILE)

        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkorange'),
                             (x + TILE, y + TILE), (x, y + TILE), self.thickness)  # Drawing a line from (x + TILE, y + TILE) to (x, y + TILE)

        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkorange'),
                             (x, y + TILE), (x, y), self.thickness)  # Drawing a line from (x, y + TILE) to (x, y)

    # Method to get the rectangles representing the walls of the cell

    def get_rects(self):
        # Creating an empty list to store the rectangles
        rects = []

        # Calculating the actual coordinates of the cell
        x, y = self.x * TILE, self.y * TILE

        if self.walls['top']:                           # Checking if top wall exists
            # Creating and adding a rectangle to the list for the top wall
            # Creating a rectangle at (x, y) with width TILE and height self.thickness
            rects.append(pygame.Rect((x, y), (TILE, self.thickness)))

         # Similarly checking and creating rectangles for other walls if they exist
        if self.walls['right']:
            rects.append(pygame.Rect(
                (x + TILE - self.thickness, y), (self.thickness, TILE)))  # Creating a rectangle at (x + TILE - self.thickness, y) with width self.thickness and height TILE

        if self.walls['bottom']:
            rects.append(pygame.Rect(
                (x, y + TILE - self.thickness), (TILE, self.thickness)))  # Creating a rectangle at (x, y + TILE - self.thickness) with width TILE and height self.thickness

        if self.walls['left']:
            # Creating a rectangle at (x, y) with width self.thickness and height TILE
            rects.append(pygame.Rect((x, y), (self.thickness, TILE)))

        return rects  # Returning the list of rectangles

    # Method to check if a cell at given coordinates is valid or not
    def check_cell(self, x, y):
        # Lambda function to calculate the index of the cell in the grid_cells array
        def find_index(x, y): return x + y * cols

        # Checking if the given coordinates are within the range of the maze
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
            # Returning False if the coordinates are outside the maze
            return False

        # Returning the cell from the grid_cells array at the calculated index
        return self.grid_cells[find_index(x, y)]

    # Method to check the neighbors of the current cell
    def check_neighbors(self, grid_cells):
        # Assigning the grid_cells array to the instance variable
        self.grid_cells = grid_cells

        # Creating an empty list to store the neighboring cells
        neighbors = []

        # Checking the top neighbor
        top = self.check_cell(self.x, self.y - 1)
        # Checking the right neighbor
        right = self.check_cell(self.x + 1, self.y)
        # Checking the bottom neighbor
        bottom = self.check_cell(self.x, self.y + 1)
        # Checking the left neighbor
        left = self.check_cell(self.x - 1, self.y)

        # Checking if the neighbors exist and are not visited, and adding them to the list if they meet the condition
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        # Returning a random neighbor from the list if it exists, otherwise returning False
        return choice(neighbors) if neighbors else False


# Function to remove walls between two neighboring cells
def remove_walls(current, next):
    # Calculating the difference in x coordinates of the cells
    dx = current.x - next.x
    if dx == 1:  # Checking if the next cell is to the left of the current cell
        # Removing the left wall of the current cell
        current.walls['left'] = False
        # Removing the right wall of the next cell
        next.walls['right'] = False
    elif dx == -1:  # Checking if the next cell is to the right of the current cell
        # Removing the right wall of the current cell
        current.walls['right'] = False
        # Removing the left wall of the next cell
        next.walls['left'] = False

    # Calculating the difference in y coordinates of the cells
    dy = current.y - next.y
    if dy == 1:  # Checking if the next cell is above the current cell
        # Removing the top wall of the current cell
        current.walls['top'] = False
        # Removing the bottom wall of the next cell
        next.walls['bottom'] = False
    elif dy == -1:                                 # Checking if the next cell is below the current cell
        # Removing the bottom wall of the current cell
        current.walls['bottom'] = False
        # Removing the top wall of the next cell
        next.walls['top'] = False


def generate_maze():                                 # Function to generate the maze
    # Creating a list of Cell objects to represent the cells in the maze
    grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]

    # Setting the current cell as the first cell in the grid
    current_cell = grid_cells[0]
    # Creating an empty stack to store the visited cells
    array = []
    # Variable to keep track of the number of visited cells
    break_count = 1

    # Looping until all cells are visited
    while break_count != len(grid_cells):
        # Marking the current cell as visited
        current_cell.visited = True
        # Checking the neighbors of the current cell
        next_cell = current_cell.check_neighbors(grid_cells)

        if next_cell:                                  # If there is a valid neighboring cell
            next_cell.visited = True                     # Marking the next cell as visited
            # Incrementing the count of visited cells
            break_count += 1
            # Adding the current cell to the stack
            array.append(current_cell)
            # Removing the walls between the current and next cell
            remove_walls(current_cell, next_cell)
            current_cell = next_cell                            # Moving to the next cell
        elif array:                                       # If the stack is not empty
            # Pop the previous cell from the stack and make it the current cell
            current_cell = array.pop()

    # Set an exit point in the maze (for example, at a random inner cell)
    # Selecting the last cell in the grid as the exit cell
    exit_cell = grid_cells[-1]

    return grid_cells


def exit_open(exit_cell):
    # Deletes the cell when the key is collected
    exit_cell.walls["right"] = False
