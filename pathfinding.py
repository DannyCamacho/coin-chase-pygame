import heapq
from config import *


class Cell:
    def __init__(self, i=0, j=0, parent_i=0, parent_j=0, f=float('inf'), g=float('inf'), h=0, closed=False):
        self.i = i  # Cell's row index
        self.j = j  # Cell's column index
        self.parent_i = parent_i  # Parent cell's row index
        self.parent_j = parent_j  # Parent cell's column index
        self.f = f  # Total cost of the cell (g + h)
        self.g = g  # Cost from start to this cell
        self.h = h  # Heuristic cost from this cell to destination
        self.closed = closed  # closed list: False is open, True is closed


# Calculate the heuristic h-value of a cell (Euclidean distance to destination)
def calculate_h_value(row, col, dest):
    return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5


# Check if a cell is valid (within the grid)
def is_valid(row, col):
    return (row >= 0) and (row < MAP_HEIGHT) and (col >= 0) and (col < MAP_WIDTH)


# Check if a cell is unblocked (on grid: 0 is blocked, 1 is unblocked)
def is_unblocked(grid, row, col):
    return grid[row][col] == 1


# Check if a cell is the destination
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]


# Trace the path from source to destination
def trace_path(cell, dest):
    path = []
    i = dest[0]
    j = dest[1]
    temp_cell = cell[(i, j)]

    # Trace the path from destination to source using parent cells
    while not (temp_cell.parent_i == i and temp_cell.parent_j == j):
        path.append((i, j))
        i = temp_cell.parent_i
        j = temp_cell.parent_j
        temp_cell = cell[(i, j)]

    # Reverse the path to get the path from source to destination
    path.reverse()
    return path


# Implement the A* search algorithm
def a_star_search(grid, src, dest):
    # Initialize the start cell details
    start = Cell(i=src[0], j=src[1], parent_i=src[0], parent_j=src[1], f=0, g=0)

    # Initialize the open list (cells to be visited) with the start cell: (f, row, col)
    open_list = []
    cell_data = {(start.i, start.j): start}
    heapq.heappush(open_list, (0.0, start.i, start.j))

    # Main loop of A* search algorithm
    while open_list:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        # Mark the cell as visited
        cell_data[(p[1], p[2])].closed = True

        # If the top is the destination
        if is_destination(p[1], p[2], dest):
            # Trace and return the path from source to destination
            return trace_path(cell_data, dest)

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i_new = p[1] + direction[0]
            j_new = p[2] + direction[1]

            temp_cell = cell_data.get((i_new, j_new), None)
            if not temp_cell:
                temp_cell = Cell(i=i_new, j=j_new, parent_i=p[1], parent_j=p[2])
                cell_data[(i_new, j_new)] = temp_cell

            # If the successor is valid, unblocked, and not visited
            if is_valid(i_new, j_new) and is_unblocked(grid, i_new, j_new) and not temp_cell.closed:
                # Calculate the new f, g, and h values
                g_new = cell_data[(p[1], p[2])].g + 1.0
                h_new = calculate_h_value(i_new, j_new, dest)
                f_new = g_new + h_new

                # If the cell is not in the open list or the new f value is smaller
                if f_new < temp_cell.f:
                    # Update the cell details
                    temp_cell.f = f_new
                    temp_cell.g = g_new
                    temp_cell.h = h_new

                    # Add the cell to the open list
                    heapq.heappush(open_list, (f_new, i_new, j_new))
