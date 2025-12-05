# Student 5: ui_effects.py
# rounded rect, glow and simple easing utilities

import pygame

def rounded_rect(surface, color, rect, radius=8):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

def draw_glow(surface, color, rect, spread=6):
    # simple glow: blit translucent rects around
    glow_surf = pygame.Surface((rect[2]+spread*2, rect[3]+spread*2), pygame.SRCALPHA)
    r,g,b = color
    for i in range(spread,0,-1):
        alpha = int(20 * (i/spread))
        pygame.draw.rect(glow_surf, (r,g,b,alpha), (spread-i, spread-i, rect[2]+i*2, rect[3]+i*2), border_radius=12)
    surface.blit(glow_surf, (rect[0]-spread, rect[1]-spread))
