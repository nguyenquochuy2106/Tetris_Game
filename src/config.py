# Student 1: config.py
# Settings, themes, UI constants.

import os

# Paths
ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS = os.path.join(ROOT, "assets")
SOUNDS_DIR = os.path.join(ASSETS, "sounds")
FONTS_DIR = os.path.join(ASSETS, "fonts")
DATA_DIR = os.path.join(ROOT, "data")
LEADERBOARD_FILE = os.path.join(DATA_DIR, "leaderboard.json")

# Grid
COLS = 10
ROWS = 20
BLOCK = 28       # size of each block in px
BOARD_W = COLS * BLOCK
BOARD_H = ROWS * BLOCK
PANEL_W = 220
WIDTH = BOARD_W + PANEL_W + 40
HEIGHT = max(BOARD_H + 40, 680)

FPS = 60

# Themes (skin)
THEMES = {
    "cyberpunk": {
        "bg_top": (8, 0, 20),
        "bg_bottom": (20, 0, 40),
        "accent": (255, 20, 147),
        "panel": (10, 10, 15),
        "glow": (0, 255, 255)
    },
    "retro": {
        "bg_top": (10, 10, 30),
        "bg_bottom": (30, 10, 0),
        "accent": (255, 200, 0),
        "panel": (25, 25, 35),
        "glow": (255, 255, 0)
    },
    "minimal": {
        "bg_top": (15, 15, 20),
        "bg_bottom": (45, 45, 50),
        "accent": (200, 200, 200),
        "panel": (35, 35, 40),
        "glow": (180, 180, 180)
    }
}

DEFAULT_THEME = "cyberpunk"
