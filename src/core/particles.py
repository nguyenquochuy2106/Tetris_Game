# Student 4: particles.py
# Simple particle system for line clear effect

import random
import pygame
from config import BLOCK

class Particle:
    def __init__(self, pos, color):
        self.pos = list(pos)
        self.vel = [random.uniform(-2,2), random.uniform(-6,-2)]
        self.life = random.uniform(0.6, 1.2)
        self.color = color
        self.size = random.randint(2,5)

    def update(self, dt):
        self.vel[1] += 9.8 * dt * 3  # gravity
        self.pos[0] += self.vel[0] * dt * 60
        self.pos[1] += self.vel[1] * dt * 60
        self.life -= dt

    def draw(self, surf):
        if self.life > 0:
            alpha = max(0, int(255 * (self.life / 1.2)))
            s = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            s.fill((*self.color, alpha))
            surf.blit(s, (self.pos[0], self.pos[1]))

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit_from_row(self, row_index, board_x, board_y, block_size, row_colors):
        # emit from across the width of the board
        for col in range(len(row_colors)):
            color = row_colors[col] or (255,255,255)
            # spawn a few particles per cell
            cell_x = board_x + col * block_size + block_size/2
            cell_y = board_y + row_index * block_size + block_size/2
            for _ in range(6):
                p = Particle((cell_x, cell_y), color)
                self.particles.append(p)

    def update(self, dt):
        for p in self.particles[:]:
            p.update(dt)
            if p.life <= 0:
                self.particles.remove(p)

    def draw(self, surf):
        for p in self.particles:
            p.draw(surf)
