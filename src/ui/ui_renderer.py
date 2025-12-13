import pygame
from src.core.settings import CELL_SIZE, OFFSET_X, OFFSET_Y, GRID_WIDTH, GRID_HEIGHT

class UIRenderer:
    def __init__(self, screen):
        self.screen = screen
        try:
            self.font = pygame.font.Font("assets/fonts/neon.ttf", 20)
            self.big_font = pygame.font.Font("assets/fonts/neon.ttf", 36)
        except:
            self.font = pygame.font.SysFont("Arial", 20)
            self.big_font = pygame.font.SysFont("Arial", 36)

    # vẽ bảng grid trong board.grid theo màu của từng ô
    def draw_board(self, board):
        rect = pygame.Rect(OFFSET_X-6, OFFSET_Y-6, GRID_WIDTH*CELL_SIZE+12, GRID_HEIGHT*CELL_SIZE+12)
        pygame.draw.rect(self.screen, (30,120,255), rect, width=3, border_radius=12)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = board.grid[y][x]
                r = pygame.Rect(OFFSET_X+x*CELL_SIZE, OFFSET_Y+y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
                pygame.draw.rect(self.screen, color if color else (25,25,35), r, border_radius=6)

    # vẽ mảnh hiện tại đang rơi
    def draw_piece(self, piece):
        for x,y in piece.get_cells():
            if y<0: continue
            r = pygame.Rect(OFFSET_X+x*CELL_SIZE, OFFSET_Y+y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
            pygame.draw.rect(self.screen, piece.color, r, border_radius=6)

    def draw_info_panel(self, game):
        x = OFFSET_X + GRID_WIDTH*CELL_SIZE + 20
        y = OFFSET_Y
        rect = pygame.Rect(x,y,150,220)
        pygame.draw.rect(self.screen,(18,18,28),rect,border_radius=10)
        pygame.draw.rect(self.screen,(0,180,220),rect,width=2,border_radius=10)
        self.screen.blit(self.font.render(f"SCORE: {game.score}", True,(0,255,255)), (x+12,y+12))
        self.screen.blit(self.font.render(f"LEVEL: {game.level}", True,(0,255,255)), (x+12,y+42))
        self.screen.blit(self.font.render(f"LINES: {game.lines}", True,(0,255,255)), (x+12,y+72))

    def render(self, game, paused=False):
        self.screen.fill((8, 8, 18)) # set background
        self.draw_board(game.board)
        self.draw_piece(game.current)
        self.draw_info_panel(game)


