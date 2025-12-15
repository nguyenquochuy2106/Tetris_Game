import pygame
from src.core.settings import CELL_SIZE, OFFSET_X, OFFSET_Y, GRID_WIDTH, GRID_HEIGHT, WINDOW_HEIGHT, WINDOW_WIDTH

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
        border_rect = pygame.Rect(OFFSET_X-6, OFFSET_Y-6, GRID_WIDTH*CELL_SIZE+12, GRID_HEIGHT*CELL_SIZE+12)
        pygame.draw.rect(self.screen, (30,120,255), border_rect, width=3, border_radius=12)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = board.grid[y][x]
                cell_rect = pygame.Rect(OFFSET_X+x*CELL_SIZE, OFFSET_Y+y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
                pygame.draw.rect(self.screen, color if color else (25,25,35), cell_rect, border_radius=6)

    # vẽ mảnh hiện tại đang rơi
    def draw_piece(self, piece):
        for x,y in piece.get_cells():
            if y<0: continue
            piece_rect = pygame.Rect(OFFSET_X+x*CELL_SIZE, OFFSET_Y+y*CELL_SIZE, CELL_SIZE-2, CELL_SIZE-2)
            pygame.draw.rect(self.screen, piece.color, piece_rect, border_radius=6)

    def draw_info_panel(self, game):
        panel_x = OFFSET_X + GRID_WIDTH*CELL_SIZE + 20
        panel_y = OFFSET_Y
        panel_rect = pygame.Rect(panel_x, panel_y, 150, 220)
        pygame.draw.rect(self.screen, (18,18,28), panel_rect, border_radius=10)
        pygame.draw.rect(self.screen, (0,180,220), panel_rect, width=2, border_radius=10)
        self.screen.blit(self.font.render(f"SCORE: {game.score}", True,(0,255,255)), (panel_x+12, panel_y+12))
        self.screen.blit(self.font.render(f"LEVEL: {game.level}", True,(0,255,255)), (panel_x+12, panel_y+42))
        self.screen.blit(self.font.render(f"LINES: {game.lines}", True,(0,255,255)), (panel_x+12, panel_y+72))

    def render(self, game, paused=False):
        self.screen.fill((8, 8, 18)) # set background
        self.draw_board(game.board)
        self.draw_piece(game.current)
        self.draw_info_panel(game)

        if paused:
            paused_text = self.big_font.render("PAUSED", True, (255, 200, 0))
            paused_rect = paused_text.get_rect(center=(OFFSET_X + GRID_WIDTH*CELL_SIZE//2,
                                OFFSET_Y + GRID_HEIGHT*CELL_SIZE//2))
            self.screen.blit(paused_text, paused_rect)
        
        if game.game_over:
            # overlay tối làm background game over
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(200)  # mờ
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            # GAME OVER title
            game_over_text = self.big_font.render("GAME OVER", True, (255, 60, 60))
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100))
            self.screen.blit(game_over_text, game_over_rect)

            # SCORE hiển thị
            score_text = self.font.render(f"Final Score: {game.score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50))
            self.screen.blit(score_text, score_rect)

            # Leaderboard top 10
            top_scores = game.leaderboard.load()
            y_offset = WINDOW_HEIGHT//2
            for index, record in enumerate(top_scores):
                leaderboard_entry_text = self.font.render(f"{index+1}. {record['name']} - {record['score']}", True, (0, 255, 255))
                leaderboard_entry_rect = leaderboard_entry_text.get_rect(center=(WINDOW_WIDTH//2, y_offset + index*30))
                self.screen.blit(leaderboard_entry_text, leaderboard_entry_rect)

            # Restart hint
            restart_text = self.font.render("Press R to Restart", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT - 50))
            self.screen.blit(restart_text, restart_rect)


