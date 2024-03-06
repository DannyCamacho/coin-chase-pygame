from config import *
import heapq


class Cell:
    def __init__(self):
        self.parent_i = 0  # Parent cell's row index
        self.parent_j = 0  # Parent cell's column index
        self.f = float('inf')  # Total cost of the cell (g + h)
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Heuristic cost from this cell to destination


# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < MAP_HEIGHT) and (col >= 0) and (col < MAP_WIDTH)


# Check if a cell is unblocked (on grid: 0 is blocked, 1 is unblocked)
def is_unblocked(grid, row, col):
    return grid[row][col] == 1


# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]


# Calculate the heuristic h-value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5


# Trace the path from source to destination
def trace_path(cell, dest):
    path = []
    row = dest[0]
    col = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell[row][col].parent_i == row and cell[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell[row][col].parent_i
        temp_col = cell[row][col].parent_j
        row = temp_row
        col = temp_col

    # Reverse the path to get the path from source to destination
    path.reverse()
    return path


# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Initialize the closed list (visited cells), 'False' is not visited
    closed_list = [[False for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    # Initialize the details of each cell for size of map
    cell = [[Cell() for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell[i][j].f = 0
    cell[i][j].g = 0
    cell[i][j].h = 0
    cell[i][j].parent_i = i
    cell[i][j].parent_j = j

    # Initialize the open list (cells to be visited) with the start cell: (f, row, col)
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # For each direction, check the successors
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked, and not visited
            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell
                    cell[new_i][new_j].parent_i = i
                    cell[new_i][new_j].parent_j = j
                    # Trace and return the path from source to destination
                    return trace_path(cell, dest)
                else:
                    # Calculate the new f, g, and h values
                    g_new = cell[i][j].g + 1.0
                    h_new = calculate_h_value(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller
                    if cell[new_i][new_j].f == float('inf') or f_new < cell[new_i][new_j].f:
                        # Add the cell to the open list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details
                        cell[new_i][new_j].f = f_new
                        cell[new_i][new_j].g = g_new
                        cell[new_i][new_j].h = h_new
                        cell[new_i][new_j].parent_i = i
                        cell[new_i][new_j].parent_j = j
