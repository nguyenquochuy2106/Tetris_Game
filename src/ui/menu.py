import pygame
from ui.ui_renderer import UIRenderer

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.ui = UIRenderer(screen)

        try:
            # font tiếng Việt đầy đủ
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

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    return "quit"
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                        return "start"
                    if ev.key == pygame.K_ESCAPE:
                        return "quit"

            self.screen.fill((10, 10, 20))  # dark background

            # --- Tên game (centered) ---
            title_surf = self.title_font.render("TETRIS NEON", True, (0, 255, 200))
            title_rect = title_surf.get_rect(center=(width // 2, height // 4))
            self.screen.blit(title_surf, title_rect)

            # --- Tên nhóm ---
            group_surf = self.font.render(self.group_name, True, (255, 255, 0))
            group_rect = group_surf.get_rect(center=(width // 2, title_rect.bottom + 40))
            self.screen.blit(group_surf, group_rect)

            # --- Danh sách thành viên (canh trái) ---
            member_x = width // 2 - 200  # cách giữa một chút sang trái
            for i, member in enumerate(self.members):
                text = f"{member['mssv']} - {member['name']}"
                member_surf = self.font.render(text, True, (200, 200, 255))
                member_rect = member_surf.get_rect(topleft=(member_x, group_rect.bottom + 20 + i * 30))
                self.screen.blit(member_surf, member_rect)


            # --- Hướng dẫn phím (ngay dưới danh sách thành viên) ---
            guide_surf = self.small_font.render("Press ENTER to Start or ESC to Quit", True, (200, 200, 200))
            guide_rect = guide_surf.get_rect(center=(width // 2, member_rect.bottom + 40))
            self.screen.blit(guide_surf, guide_rect)

            pygame.display.flip()
            clock.tick(30)
