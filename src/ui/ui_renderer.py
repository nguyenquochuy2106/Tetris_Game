import pygame
from src.core.settings import CELL_SIZE, OFFSET_X, OFFSET_Y, GRID_WIDTH, GRID_HEIGHT, WINDOW_HEIGHT, WINDOW_WIDTH

class UIRenderer:
    # Font sizes
    FONT_SIZE_NORMAL = 20
    FONT_SIZE_LARGE = 36

    # Board styling
    BOARD_BORDER_OFFSET = 6
    BOARD_BORDER_WIDTH = 3
    BOARD_BORDER_RADIUS = 12
    BOARD_BORDER_COLOR = (30, 120, 255)

    # Cell styling
    CELL_MARGIN = 2
    CELL_BORDER_RADIUS = 6
    CELL_EMPTY_COLOR = (25, 25, 35)

    # Info panel dimensions
    PANEL_OFFSET_X = 20
    PANEL_WIDTH = 150
    PANEL_HEIGHT = 220
    PANEL_BORDER_RADIUS = 10
    PANEL_BORDER_WIDTH = 2
    PANEL_TEXT_PADDING = 12
    PANEL_TEXT_LINE_HEIGHT = 30

    # Colors
    COLOR_BACKGROUND = (8, 8, 18)
    COLOR_PANEL_BG = (18, 18, 28)
    COLOR_PANEL_BORDER = (0, 180, 220)
    COLOR_TEXT_CYAN = (0, 255, 255)
    COLOR_TEXT_WHITE = (255, 255, 255)
    COLOR_PAUSED = (255, 200, 0)
    COLOR_GAME_OVER = (255, 60, 60)
    COLOR_OVERLAY = (0, 0, 0)

    # Overlay settings
    OVERLAY_ALPHA = 200

    # Game over screen layout
    GAME_OVER_TITLE_OFFSET_Y = -100
    GAME_OVER_SCORE_OFFSET_Y = -50
    LEADERBOARD_START_OFFSET_Y = 0
    LEADERBOARD_ENTRY_HEIGHT = 30
    RESTART_HINT_OFFSET_Y = -50
    
    def __init__(self, screen):
        self.screen = screen
        try:
            self.font = pygame.font.Font("assets/fonts/neon.ttf", self.FONT_SIZE_NORMAL)
            self.big_font = pygame.font.Font("assets/fonts/neon.ttf", self.FONT_SIZE_LARGE)
        except:
            self.font = pygame.font.SysFont("Arial", self.FONT_SIZE_NORMAL)
            self.big_font = pygame.font.SysFont("Arial", self.FONT_SIZE_LARGE)

        # Cache static text surfaces (rendered once)
        self.paused_text = self.big_font.render("PAUSED", True, self.COLOR_PAUSED)
        self.game_over_text = self.big_font.render("GAME OVER", True, self.COLOR_GAME_OVER)
        self.restart_hint_text = self.font.render("Press R to Restart", True, self.COLOR_TEXT_WHITE)

    # vẽ bảng grid trong board.grid theo màu của từng ô
    def draw_board(self, board):
        border_rect = pygame.Rect(
            OFFSET_X - self.BOARD_BORDER_OFFSET,
            OFFSET_Y - self.BOARD_BORDER_OFFSET,
            GRID_WIDTH * CELL_SIZE + self.BOARD_BORDER_OFFSET * 2,
            GRID_HEIGHT * CELL_SIZE + self.BOARD_BORDER_OFFSET * 2
        )
        pygame.draw.rect(self.screen, self.BOARD_BORDER_COLOR, border_rect,
                        width=self.BOARD_BORDER_WIDTH, border_radius=self.BOARD_BORDER_RADIUS)
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = board.grid[y][x]
                cell_rect = pygame.Rect(
                    OFFSET_X + x * CELL_SIZE,
                    OFFSET_Y + y * CELL_SIZE,
                    CELL_SIZE - self.CELL_MARGIN,
                    CELL_SIZE - self.CELL_MARGIN
                )
                pygame.draw.rect(self.screen, color if color else self.CELL_EMPTY_COLOR,
                               cell_rect, border_radius=self.CELL_BORDER_RADIUS)

    # vẽ mảnh hiện tại đang rơi
    def draw_piece(self, piece):
        for x, y in piece.get_cells():
            if y < 0:
                continue
            piece_rect = pygame.Rect(
                OFFSET_X + x * CELL_SIZE,
                OFFSET_Y + y * CELL_SIZE,
                CELL_SIZE - self.CELL_MARGIN,
                CELL_SIZE - self.CELL_MARGIN
            )
            pygame.draw.rect(self.screen, piece.color, piece_rect, border_radius=self.CELL_BORDER_RADIUS)

    def draw_info_panel(self, game):
        panel_x = OFFSET_X + GRID_WIDTH * CELL_SIZE + self.PANEL_OFFSET_X
        panel_y = OFFSET_Y
        panel_rect = pygame.Rect(panel_x, panel_y, self.PANEL_WIDTH, self.PANEL_HEIGHT)
        pygame.draw.rect(self.screen, self.COLOR_PANEL_BG, panel_rect, border_radius=self.PANEL_BORDER_RADIUS)
        pygame.draw.rect(self.screen, self.COLOR_PANEL_BORDER, panel_rect,
                        width=self.PANEL_BORDER_WIDTH, border_radius=self.PANEL_BORDER_RADIUS)

        self.screen.blit(
            self.font.render(f"SCORE: {game.score}", True, self.COLOR_TEXT_CYAN),
            (panel_x + self.PANEL_TEXT_PADDING, panel_y + self.PANEL_TEXT_PADDING)
        )
        self.screen.blit(
            self.font.render(f"LEVEL: {game.level}", True, self.COLOR_TEXT_CYAN),
            (panel_x + self.PANEL_TEXT_PADDING, panel_y + self.PANEL_TEXT_PADDING + self.PANEL_TEXT_LINE_HEIGHT)
        )
        self.screen.blit(
            self.font.render(f"LINES: {game.lines}", True, self.COLOR_TEXT_CYAN),
            (panel_x + self.PANEL_TEXT_PADDING, panel_y + self.PANEL_TEXT_PADDING + self.PANEL_TEXT_LINE_HEIGHT * 2)
        )

    def render(self, game, paused=False):
        self.screen.fill(self.COLOR_BACKGROUND)
        self.draw_board(game.board)
        self.draw_piece(game.current)
        self.draw_info_panel(game)

        if paused:
            paused_rect = self.paused_text.get_rect(
                center=(OFFSET_X + GRID_WIDTH * CELL_SIZE // 2,
                       OFFSET_Y + GRID_HEIGHT * CELL_SIZE // 2)
            )
            self.screen.blit(self.paused_text, paused_rect)
        
        if game.game_over:
            # overlay tối làm background game over
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(self.OVERLAY_ALPHA)
            overlay.fill(self.COLOR_OVERLAY)
            self.screen.blit(overlay, (0, 0))

            # GAME OVER title
            game_over_rect = self.game_over_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + self.GAME_OVER_TITLE_OFFSET_Y)
            )
            self.screen.blit(self.game_over_text, game_over_rect)

            # SCORE hiển thị
            score_text = self.font.render(f"Final Score: {game.score}", True, self.COLOR_TEXT_WHITE)
            score_rect = score_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + self.GAME_OVER_SCORE_OFFSET_Y)
            )
            self.screen.blit(score_text, score_rect)

            # Leaderboard top 10
            top_scores = game.leaderboard.load()
            y_offset = WINDOW_HEIGHT // 2 + self.LEADERBOARD_START_OFFSET_Y
            for index, record in enumerate(top_scores):
                leaderboard_entry_text = self.font.render(
                    f"{index + 1}. {record['name']} - {record['score']}",
                    True,
                    self.COLOR_TEXT_CYAN
                )
                leaderboard_entry_rect = leaderboard_entry_text.get_rect(
                    center=(WINDOW_WIDTH // 2, y_offset + index * self.LEADERBOARD_ENTRY_HEIGHT)
                )
                self.screen.blit(leaderboard_entry_text, leaderboard_entry_rect)

            # Restart hint
            restart_rect = self.restart_hint_text.get_rect(
                center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT + self.RESTART_HINT_OFFSET_Y)
            )
            self.screen.blit(self.restart_hint_text, restart_rect)


