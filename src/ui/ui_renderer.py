import pygame
from src.core.settings import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, OFFSET_X, OFFSET_Y, GRID_WIDTH, GRID_HEIGHT

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

    def draw_piece(self, piece):
        for x,y in piece.get_cells():
            if y<0: continue
            r = pygame.Rect(OFFSET_X+x*CELL_SIZE, OFFSET_Y+y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
            pygame.draw.rect(self.screen, piece.color, r, border_radius=6)

    def draw_ui_panel(self, game):
        x = OFFSET_X + GRID_WIDTH*CELL_SIZE + 20
        y = OFFSET_Y
        rect = pygame.Rect(x,y,180,220)
        pygame.draw.rect(self.screen,(18,18,28),rect,border_radius=10)
        pygame.draw.rect(self.screen,(0,180,220),rect,width=2,border_radius=10)
        self.screen.blit(self.font.render(f"SCORE: {game.score}", True,(0,255,255)), (x+12,y+12))
        self.screen.blit(self.font.render(f"LEVEL: {game.level}", True,(0,255,255)), (x+12,y+42))
        self.screen.blit(self.font.render(f"LINES: {game.lines}", True,(0,255,255)), (x+12,y+72))

    def render(self, game, paused=False):
        # nền chính
        self.screen.fill((8, 8, 18))
        self.draw_board(game.board)
        self.draw_piece(game.current)
        self.draw_ui_panel(game)

        if paused:
            t = self.big_font.render("PAUSED", True, (255, 200, 0))
            r = t.get_rect(center=(OFFSET_X + GRID_WIDTH*CELL_SIZE//2,
                                OFFSET_Y + GRID_HEIGHT*CELL_SIZE//2))
            self.screen.blit(t, r)

        if game.game_over:
            # overlay tối làm background game over
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(200)  # mờ
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            # GAME OVER title
            t = self.big_font.render("GAME OVER", True, (255, 60, 60))
            r = t.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
            self.screen.blit(t, r)

            # SCORE hiển thị
            score_text = self.font.render(f"Final Score: {game.score}", True, (255, 255, 255))
            r2 = score_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50))
            self.screen.blit(score_text, r2)

            # Leaderboard top 10
            top_scores = game.leaderboard.load()
            y_offset = WINDOW_HEIGHT//2
            for i, rec in enumerate(top_scores):
                s = self.font.render(f"{i+1}. {rec['name']} - {rec['score']}", True, (0, 255, 255))
                r3 = s.get_rect(center=(WINDOW_WIDTH//2, y_offset + i*30))
                self.screen.blit(s, r3)

            # Restart hint
            s2 = self.font.render("Press R to Restart", True, (255, 255, 255))
            r4 = s2.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT - 50))
            self.screen.blit(s2, r4)

