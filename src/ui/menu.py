import pygame
from ui.ui_renderer import UIRenderer
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.ui = UIRenderer(screen)
        try:
            # full Vietnamese font
            self.title_font = pygame.font.Font("assets/fonts/NotoSans-Bold.ttf", 48)
            self.font = pygame.font.Font("assets/fonts/NotoSans-Regular.ttf", 28)
            self.small_font = pygame.font.Font("assets/fonts/NotoSans-Regular.ttf", 22)
        except:
            self.title_font = pygame.font.SysFont("Arial", 48, bold=True)
            self.font = pygame.font.SysFont("Arial", 28)
            self.small_font = pygame.font.SysFont("Arial", 22)


        # Thông tin nhóm
        self.group_name = "Nhóm Tetris Neon"
        self.members = [
            {"mssv": "22730075", "name": "Nguyễn Quốc Huy"},
            {"mssv": "22730094 ", "name": "Trần Hữu Tài"},
            {"mssv": "25730007", "name": "Đồng Nguyễn Vũ Anh"},
            {"mssv": "25730009", "name": "Phạm Anh"},
            {"mssv": "22730083", "name": "Lục Gia Mẫn"},
        ]
     
    def main_menu(self):
        clock = pygame.time.Clock()
        width, height = self.screen.get_size()

