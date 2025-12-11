from .settings import GRID_WIDTH, GRID_HEIGHT

class Board:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        print("[DEBUG] Initialized Board")
