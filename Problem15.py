"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""


if __name__ == "__main__":
    grid_x = 20
    grid_y = 20
    from maths.misc import combinations
    
    paths = combinations(grid_x + grid_y, grid_y)
    print 'Number of paths in grid of size %dx%d is %d'%(grid_x, grid_y, paths)