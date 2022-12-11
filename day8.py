from dataclasses import dataclass


direction_offsets = {"left": (-1, 0), "right": (1, 0), "up": (0, -1), "down": (0, 1)}


@dataclass(frozen=True)
class Tree:
    x: int
    y: int
    height: int


class Forest:
    trees = set()

    def __init__(self, grid: list[list[int]]) -> None:

        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                tree = Tree(x, y, col)
                Forest.trees.add(tree)
                # print(tree)

        self.max_x = x
        self.max_y = y

        # print(f"x: {x}   y: {y}")

    def vis_left(self, tree: Tree) -> bool:
        trees = [t for t in Forest.trees if t.y == tree.y and t.x < tree.x]
        max_height = max([t.height for t in trees])
        if tree.height > max_height:
            return True
        return False

    def vis_right(self, tree: Tree) -> bool:
        trees = [t for t in Forest.trees if t.y == tree.y and t.x > tree.x]
        max_height = max([t.height for t in trees])
        if tree.height > max_height:
            return True
        return False

    def vis_down(self, tree: Tree) -> bool:
        trees = [t for t in Forest.trees if t.y > tree.y and t.x == tree.x]
        max_height = max([t.height for t in trees])
        if tree.height > max_height:
            return True
        return False

    def vis_up(self, tree: Tree) -> bool:
        trees = [t for t in Forest.trees if t.y < tree.y and t.x == tree.x]
        max_height = max([t.height for t in trees])
        if tree.height > max_height:
            return True
        return False

    def is_visible(self, tree: Tree) -> bool:
        if tree.x in (0, self.max_x) or tree.y in (0, self.max_y):
            return True
        else:
            if (
                self.vis_left(tree)
                or self.vis_right(tree)
                or self.vis_up(tree)
                or self.vis_down(tree)
            ):
                return True
            return False


grid = []
with open("input8.txt") as f:
    for line in f:
        line = line.strip()
        row = [int(x) for x in line]
        grid.append(row)


vis = 0

forest = Forest(grid)
for tree in forest.trees:
    if forest.is_visible(tree):
        print(tree)
        vis += 1

print(vis)
