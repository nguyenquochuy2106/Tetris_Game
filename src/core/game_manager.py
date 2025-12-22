import pygame
import random
from .tetromino import Tetromino
from .board import Board
from .leaderboard import Leaderboard

class GameManager:
    def __init__(self):
        self.board = Board()
        self.current = Tetromino()
        self.next = Tetromino()
        self.score = 0
        self.lines = 0
        self.level = 1
        self.drop_timer = 0.0
        self.speed_level = 0
        self.drop_interval = 0.8
        self.game_over = False
        self.awaiting_name_input = False
        self.player_name = ""
        self.name_submitted = False
        self.leaderboard = Leaderboard()

        print(f"[DEBUG] Created piece {self.current.key} at x={self.current.x}, y={self.current.y}")
        print(f"[DEBUG] Created piece {self.next.key} at x={self.next.x}, y={self.next.y}")
        print("[DEBUG] GameManager initialized")

        # load sounds
        try:
            self.snd_move = pygame.mixer.Sound("assets/sounds/move.wav")
            self.snd_rotate = pygame.mixer.Sound("assets/sounds/rotate.wav")
            self.snd_drop = pygame.mixer.Sound("assets/sounds/drop.wav")
            self.snd_clear = pygame.mixer.Sound("assets/sounds/clear.wav")
        except Exception:
            self.snd_move = self.snd_rotate = self.snd_drop = self.snd_clear = None

    def reset(self):
        self.__init__()

    def update(self, dt=0.016):
        if self.game_over:
            return
        self.drop_timer += dt
        if self.drop_timer >= self.drop_interval:
            self.drop_timer = 0
            self._soft_drop()

    def _soft_drop(self):
        if self.board.valid_position(self.current, dy=1):
            self.current.y += 1
        else:
            self.lock_current()

    def move_left(self):
        if self.board.valid_position(self.current, dx=-1):
            self.current.x -= 1
            if self.snd_move: self.snd_move.play()

    def move_right(self):
        if self.board.valid_position(self.current, dx=1):
            self.current.x += 1
            if self.snd_move: self.snd_move.play()

    def rotate_piece(self):
        old_shape = [row[:] for row in self.current.shape]
        old_x = self.current.x
        self.current.rotate()
        for dx in (0, -1, 1, -2, 2):
            if self.board.valid_position(self.current, dx=dx):
                self.current.x += dx
                if self.snd_rotate: self.snd_rotate.play()
                return
        self.current.shape = old_shape
        self.current.x = old_x

    def soft_drop(self):
        self._soft_drop()

    def hard_drop(self):
        while self.board.valid_position(self.current, dy=1):
            self.current.y += 1
        if self.snd_drop: self.snd_drop.play()
        self.lock_current()

    def lock_current(self):
        self.board.place_piece(self.current)
        cleared = self.board.clear_lines()

        if cleared:
            self.lines += cleared
            self.score += cleared * 100 * self.level
            if self.snd_clear: self.snd_clear.play()
            self.speed_level += cleared
            self.drop_interval = max(0.05, 0.8 - (self.speed_level * 0.03))

        # spawn next piece
        self.current = self.next
        self.next = Tetromino()
        print(f"[DEBUG] New piece spawned at x={self.current.x}, y={self.current.y}")

        # 🔥 CHECK GAME OVER IMMEDIATELY
        if not self.board.valid_position(self.current):
            print(f"[DEBUG] Piece {self.current.key} cannot spawn. Game Over!")
            self.game_over_event()

    def game_over_event(self):
        self.game_over = True
        self.awaiting_name_input = True
        print(f"[DEBUG] Game Over! Final Score: {self.score}")

    def submit_name(self):
        name = self.player_name.strip() or "Player"
        self.leaderboard.add_score(name, self.score)
        self.awaiting_name_input = False
        self.name_submitted = True
        print(f"[DEBUG] Score saved: {name} - {self.score}")
