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

    def draw_board(self, board):
        rect = pygame.Rect(OFFSET_X-6, OFFSET_Y-6, GRID_WIDTH*CELL_SIZE+12, GRID_HEIGHT*CELL_SIZE+12)
        pygame.draw.rect(self.screen, (15,15,25), rect, border_radius=12)
        pygame.draw.rect(self.screen, (30,120,255), rect, width=2, border_radius=12)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = board.grid[y][x]
                r = pygame.Rect(OFFSET_X+x*CELL_SIZE, OFFSET_Y+y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
                pygame.draw.rect(self.screen, color if color else (25,25,35), r, border_radius=6)

    def render(self, game, paused=False):
        # nền chính
        self.screen.fill((8, 8, 18))
        self.draw_board(game.board)