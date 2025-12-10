import pygame

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
        pass

    def draw_piece(self, piece):
        pass

    def draw_ui_panel(self, game):
        pass

    def render(self, game, paused=False):
        pass

