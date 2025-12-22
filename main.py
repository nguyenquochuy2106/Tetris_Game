import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

MAX_NAME_LENGTH = 15

import pygame
from core.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from core.game_manager import GameManager
from ui.ui_renderer import UIRenderer
from ui.menu import Menu

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris Neon - Nhóm 04")
    clock = pygame.time.Clock()
    ui = UIRenderer(screen)
    menu = Menu(screen)

    while True:
        action = menu.main_menu()
        if action == "start":
            game = GameManager()
            run_game_loop(game, ui, clock)
        elif action == "quit":
            break
    pygame.quit()

def run_game_loop(game, ui, clock):
    running = True
    paused = False
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle name input when game is over
            if game.game_over and game.awaiting_name_input:
                if event.type == pygame.TEXTINPUT:
                    if len(game.player_name) < MAX_NAME_LENGTH:
                        game.player_name += event.text
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        game.player_name = game.player_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        if not game.player_name.strip():
                            game.player_name = "Player"
                        game.submit_name()

            # Normal game input
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and not game.game_over:
                    paused = not paused
                if not paused and not game.game_over:
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    elif event.key == pygame.K_RIGHT:
                        game.move_right()
                    elif event.key == pygame.K_UP:
                        game.rotate_piece()
                    elif event.key == pygame.K_DOWN:
                        game.soft_drop()
                    elif event.key == pygame.K_SPACE:
                        game.hard_drop()

                # Only allow restart after name submitted
                if game.game_over and game.name_submitted:
                    if event.key == pygame.K_r:
                        print("[DEBUG] Restarting game")
                        return  # back to menu

        if not paused and not game.game_over:
            game.update(dt)

        ui.render(game, paused)
        pygame.display.flip()

if __name__ == "__main__":
    main()
