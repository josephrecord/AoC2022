from math import prod
from typing import Tuple

Point = Tuple[int, int] # (x, y) points on a grid

def X_(point) -> int: "X coordinate"; return point[0]
def Y_(point) -> int: "Y coordinate"; return point[1]

directions = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}


g = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]


class Grid(dict):
    def __init__(self, grid: list[list[int]]) -> None:

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                self.update({(x, y): val})

        self.max_x = x
        self.max_y = y
    
    def is_edge(self, point: Point) -> bool:
        """Check if a point is on the edge of the grid"""
        if X_(point) in (0, self.max_x) or Y_(point) in (0, self.max_y):
            return True
        return False

    def vals_left(self, point: Point) -> list[int]:
        """Return all values left of the given point"""
        points = []
        for i in range(1, X_(point) + 1):
            points.append(self[(X_(point) - i, Y_(point))])
        return points
    
    def vals_right(self, point: Point) -> list[int]:
        """Return all values right of the given point"""
        points = []
        for i in range(1, self.max_x - X_(point) + 1):
            points.append(self[(X_(point) + i, Y_(point))])
        return points
    
    def vals_up(self, point: Point) -> list[int]:
        """Return all values above the given point"""
        points = []
        for i in range(1, Y_(point) + 1):
            points.append(self[(X_(point), Y_(point) - i)])
        return points
    
    def vals_down(self, point: Point) -> list[int]:
        """Return all values below the given point"""
        points = []
        for i in range(1, self.max_y - Y_(point) + 1):
            points.append(self[(X_(point), Y_(point) + i)])
        return points
    
    def scenic_score(self, point: Point) -> int:
        # trees at edge have ss of zero
        if self.is_edge(point):
            return 0

        tree_height = self[point]  # height of the tree in question
        
        # get all trees to the left and test height
        trees_left = self.vals_left(point)
        for n, tree in enumerate(trees_left, start=1):
            if tree >= tree_height:
                break
        l_score = n

        # get all trees to the right and test height
        trees_right = self.vals_right(point)
        for n, tree in enumerate(trees_right, start=1):
            if tree >= tree_height:
                break
        r_score = n

        # get all trees to the left and test height
        trees_up = self.vals_up(point)
        for n, tree in enumerate(trees_up, start=1):
            if tree >= tree_height:
                break
        u_score = n

        # get all trees to the left and test height
        trees_down = self.vals_down(point)
        for n, tree in enumerate(trees_down, start=1):
            if tree >= tree_height:
                break
        d_score = n

        return prod([l_score, r_score, u_score, d_score])




grid = []
with open("input8.txt") as f:
    for line in f:
        line = line.strip()
        row = [int(x) for x in line]
        grid.append(row)



forest = Grid(grid)

ssmax = 0
for tree in forest:
    ss = forest.scenic_score(tree)
    if ss > ssmax:
        ssmax = ss
