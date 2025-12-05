# Student 2: game_manager.py
# main game logic: spawn, move, lock, scoring, menu-state

import pygame, time
from core.board import Board
from core.tetromino import Tetromino
from core.particles import ParticleSystem
from core.leaderboard import load_leaderboard, save_leaderboard
from config import BLOCK, ROWS, COLS
import os

class GameManager:
    def __init__(self, theme):
        self.board = Board()
        self.piece = Tetromino()
        self.next_piece = Tetromino()
        self.drop_interval = 0.8  # seconds
        self.drop_timer = 0.0
        self.level = 1
        self.score = 0
        self.lines = 0
        self.paused = False
        self.over = False
        self.theme = theme

        self.particles = ParticleSystem()

        # load sounds (Student 2: ensure files exist in assets)
        self.snd_move = self._load_sound("move.wav")
        self.snd_rotate = self._load_sound("rotate.wav")
        self.snd_drop = self._load_sound("drop.wav")
        self.snd_clear = self._load_sound("clear.wav")

        self.leaderboard = load_leaderboard()

    def _load_sound(self, fname):
        path = os.path.join("assets","sounds", fname)
        try:
            return pygame.mixer.Sound(path)
        except Exception:
            return None

    def update(self, dt):
        if self.paused or self.over:
            return
        self.drop_timer += dt
        self.particles.update(dt)
        if self.drop_timer >= self.drop_interval:
            self.drop_timer = 0
            self._soft_drop()

    def _soft_drop(self):
        if self.board.valid(self.piece, dy=1):
            self.piece.y += 1
        else:
            # lock
            self.board.place(self.piece)
            if self.snd_drop: self.snd_drop.play()
            cleared_rows = self.board.clear_lines()
            if cleared_rows:
                # compute score
                self.lines += len(cleared_rows)
                self.score += (100 * (2**(len(cleared_rows)-1))) * self.level
                self.level = 1 + self.lines // 10
                # spawn particles from cleared rows
                # We need colors from board snapshot; but board.clear_lines already shifted board.
                # For effect we'll spawn from approximate y positions (use cleared rows)
                for r in cleared_rows:
                    # spawn using board x/y offsets in UI rendering
                    self.particles.emit_from_row(r, 20, 20, BLOCK, [None]*COLS)
                if self.snd_clear: self.snd_clear.play()
            # spawn next
            self.piece = self.next_piece
            self.next_piece = Tetromino()
            # if collision immediately -> game over
            if not self.board.valid(self.piece):
                self.over = True

    # input controls:
    def move_left(self):
        if self.board.valid(self.piece, dx=-1):
            self.piece.x -= 1
            if self.snd_move: self.snd_move.play()

    def move_right(self):
        if self.board.valid(self.piece, dx=1):
            self.piece.x += 1
            if self.snd_move: self.snd_move.play()

    def rotate(self):
        # try rotate with simple wall kicks
        old_grid = [row[:] for row in self.piece.grid]
        old_x = self.piece.x
        self.piece.rotate()
        kicks = [0, -1, 1, -2, 2]
        for k in kicks:
            if self.board.valid(self.piece, dx=k):
                self.piece.x += k
                if self.snd_rotate: self.snd_rotate.play()
                return
        # revert
        self.piece.grid = old_grid
        self.piece.x = old_x

    def hard_drop(self):
        while self.board.valid(self.piece, dy=1):
            self.piece.y += 1
        # lock immediately
        self._soft_drop()
        if self.snd_drop: self.snd_drop.play()

    def toggle_pause(self):
        self.paused = not self.paused

    def reset(self):
        self.__init__(self.theme)

    def save_score(self, name="Player"):
        # append and save top 10
        self.leaderboard.append({"name": name, "score": self.score, "time": time.time()})
        self.leaderboard = sorted(self.leaderboard, key=lambda r: -r["score"])[:10]
        save_leaderboard(self.leaderboard)
