# Student 5: renderer.py
# Draw board, pieces, neon border animation, menu, particles, panel, skins.

import pygame, os, math, time
from config import BLOCK, BOARD_W, BOARD_H, WIDTH, HEIGHT, THEMES, DEFAULT_THEME
from ui.ui_effects import rounded_rect, draw_glow

FONT_PATH = os.path.join("assets","fonts","neon.ttf")

class Renderer:
    def __init__(self, screen, theme_name=DEFAULT_THEME):
        self.screen = screen
        self.theme = THEMES.get(theme_name, THEMES[DEFAULT_THEME])
        self.font = pygame.font.Font(FONT_PATH, 20)
        self.big_font = pygame.font.Font(FONT_PATH, 36)
        self._t = 0.0  # time for animations

    def update_time(self, dt):
        self._t += dt

    def draw_background(self):
        # vertical gradient
        top = self.theme["bg_top"]
        bot = self.theme["bg_bottom"]
        for i in range(HEIGHT):
            mix = i / HEIGHT
            color = (
                int(top[0] * (1-mix) + bot[0] * mix),
                int(top[1] * (1-mix) + bot[1] * mix),
                int(top[2] * (1-mix) + bot[2] * mix),
            )
            pygame.draw.line(self.screen, color, (0,i), (WIDTH,i))

    def draw_neon_frame(self, rect):
        # animated neon glow around rect
        glow_color = self.theme["glow"]
        pulse = 0.6 + 0.4 * math.sin(self._t * 3.0)
        c = tuple(min(255, int(pulse * x)) for x in glow_color)
        # outer glow big
        draw_glow(self.screen, c, rect, spread=12)
        rounded_rect(self.screen, (10,10,10), rect, radius=12)
        # inner bright border
        pygame.draw.rect(self.screen, c, rect, width=3, border_radius=12)

    def draw_board_grid(self, board, bx, by):
        # bx,by top-left of board area
        for r in range(len(board.grid)):
            for c in range(len(board.grid[0])):
                cell = board.grid[r][c]
                x = bx + c * BLOCK
                y = by + r * BLOCK
                rect = (x, y, BLOCK-1, BLOCK-1)
                if cell is None:
                    rounded_rect(self.screen, (18,18,24), rect, radius=6)
                else:
                    # block with glow
                    draw_glow(self.screen, cell, rect, spread=6)
                    rounded_rect(self.screen, cell, rect, radius=6)

    def draw_piece(self, piece, bx, by):
        for x,y in piece.cells():
            if y < 0: continue
            rect = (bx + x*BLOCK, by + y*BLOCK, BLOCK-1, BLOCK-1)
            draw_glow(self.screen, piece.color, rect, spread=6)
            rounded_rect(self.screen, piece.color, rect, radius=6)

    def draw_next(self, next_piece, px, py):
        label = self.font.render("NEXT", True, self.theme["accent"])
        self.screen.blit(label, (px, py))
        offset_y = py + 28
        for x,y in next_piece.cells():
            # draw relative to a preview area by normalizing coords
            rx = (x - next_piece.x)
            ry = (y - next_piece.y)
            rect = (px + 20 + rx*BLOCK, offset_y + ry*BLOCK, BLOCK-2, BLOCK-2)
            draw_glow(self.screen, next_piece.color, rect, spread=6)
            rounded_rect(self.screen, next_piece.color, rect, radius=6)

    def draw_panel(self, game, px, py):
        # background panel
        panel_rect = (px, py, 200, 360)
        rounded_rect(self.screen, self.theme["panel"], panel_rect, radius=12)
        # info
        score_surf = self.font.render(f"SCORE: {game.score}", True, self.theme["accent"])
        self.screen.blit(score_surf, (px+12, py+20))
        level_surf = self.font.render(f"LEVEL: {game.level}", True, self.theme["accent"])
        self.screen.blit(level_surf, (px+12, py+50))

    def draw_menu(self, menu_state, px, py):
        # simple centered menu
        title = self.big_font.render("TETRIS NEON", True, self.theme["accent"])
        self.screen.blit(title, (px+20, py+20))
        # draw options
        for idx, opt in enumerate(menu_state["options"]):
            color = self.theme["accent"] if idx == menu_state["sel"] else (120,120,120)
            txt = self.font.render(opt, True, color)
            self.screen.blit(txt, (px+30, py+100 + idx*36))

    def draw_game_over(self, px, py, score):
        t = self.big_font.render("GAME OVER", True, (255,60,60))
        s = self.font.render(f"Score: {score}", True, (255,255,255))
        self.screen.blit(t, (px+40, py+120))
        self.screen.blit(s, (px+90, py+180))

    def draw_particles(self, ps):
        ps.draw(self.screen)
