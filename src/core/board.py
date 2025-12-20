from .settings import GRID_WIDTH, GRID_HEIGHT

class Board:
    def __init__(self):
        self.width = GRID_WIDTH
        self.height = GRID_HEIGHT
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]
        print("[DEBUG] Initialized Board")

    def valid_position(self, piece, dx=0, dy=0):
        """Check if piece is in a valid position."""
        for x, y in piece.get_cells():
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= self.width or ny >= self.height:
                return False
            if ny >= 0 and self.grid[ny][nx] is not None:
                return False
            # Nếu y < 0, vẫn coi là invalid nếu top row bị chặn
            if ny < 0 and self.grid[0][nx] is not None:
                return False
        return True

def place_piece(self, piece):
        print(f"[DEBUG] Locking piece {piece.key} at y={piece.y}")
        for x, y in piece.get_cells():
            if 0 <= y < self.height:
                self.grid[y][x] = piece.color
        print(f"[DEBUG] Placed piece {piece.key} on board")

def clear_lines(self):
        new_grid = []
        cleared = 0
        for row in self.grid:
