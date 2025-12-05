# Student 3: board.py
# Board grid, collision, place, clear lines

from config import COLS, ROWS

class Board:
    def __init__(self):
        self.cols = COLS
        self.rows = ROWS
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

    def in_bounds(self, x, y):
        return 0 <= x < self.cols and y < self.rows

    def valid(self, tetromino, dx=0, dy=0):
        for x,y in tetromino.cells():
            nx, ny = x+dx, y+dy
            if ny < 0:
                continue
            if not self.in_bounds(nx, ny):
                return False
            if self.grid[ny][nx] is not None:
                return False
        return True

    def place(self, tetromino):
        for x,y in tetromino.cells():
            if 0 <= y < self.rows:
                self.grid[y][x] = tetromino.color

    def clear_lines(self):
        cleared_rows = []
        new_grid = []
        for row_idx, row in enumerate(self.grid):
            if all(cell is not None for cell in row):
                cleared_rows.append(row_idx)
            else:
                new_grid.append(row)
        # add empty rows on top
        for _ in range(len(cleared_rows)):
            new_grid.insert(0, [None for _ in range(self.cols)])
        self.grid = new_grid
        return cleared_rows  # return list of indices cleared (for particles/score)
