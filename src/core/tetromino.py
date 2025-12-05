# Student 4: tetromino.py
# Tetromino class + rotations + small utility

import random

SHAPES = {
    'I': [[1,1,1,1]],
    'O': [[1,1],[1,1]],
    'T': [[0,1,0],[1,1,1]],
    'S': [[0,1,1],[1,1,0]],
    'Z': [[1,1,0],[0,1,1]],
    'J': [[1,0,0],[1,1,1]],
    'L': [[0,0,1],[1,1,1]],
}

NEON_COLORS = [
    (0,255,255),   # cyan
    (255,20,147),  # pink
    (0,255,128),   # green
    (255,255,0),   # yellow
    (0,128,255),   # blue
    (255,128,0)    # orange
]

class Tetromino:
    def __init__(self, key=None):
        self.key = key or random.choice(list(SHAPES.keys()))
        self.grid = [row[:] for row in SHAPES[self.key]]
        self.color = random.choice(NEON_COLORS)
        # spawn position: centered near top
        self.x = (10 - len(self.grid[0])) // 2
        self.y = -2
        self.rotation = 0

    def width(self):
        return len(self.grid[0])

    def height(self):
        return len(self.grid)

    def rotate(self):
        # rotate cw
        self.grid = [list(r) for r in zip(*self.grid[::-1])]
        self.rotation = (self.rotation + 1) % 4

    def cells(self):
        """Return list of (x,y) cells relative to board."""
        out = []
        for ry, row in enumerate(self.grid):
            for rx, v in enumerate(row):
                if v:
                    out.append((self.x + rx, self.y + ry))
        return out
