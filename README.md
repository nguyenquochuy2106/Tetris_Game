# Tetris Neon - Student Project

![Tetris Neon Screenshot](assets/images/game_screenshot.png)

## Table of Contents
- [Tetris Neon - Student Project](#tetris-neon---student-project)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Directory Structure](#directory-structure)
  - [Environment Setup](#environment-setup)
  - [Game Features](#game-features)
  - [Function Overview](#function-overview)
    - [GameManager](#gamemanager)
    - [Board](#board)
    - [Tetromino](#tetromino)
    - [UI Renderer](#ui-renderer)
    - [Menu](#menu)
  - [How to Run](#how-to-run)
  - [Contributing](#contributing)
  - [Tasks Division for Students](#tasks-division-for-students)
  - [Notes](#notes)
  - [Images](#images)
  - [License](#license)

---

## Project Overview
**Tetris Neon** is a modern, neon-themed Tetris game implemented in Python using Pygame.  
The game supports:  
- Classic Tetris gameplay  
- Soft and hard drops  
- Rotation & movement  
- Line clearing & scoring  
- Leveling speed up  
- Leaderboard for top scores  
- Pause & Game Over screen with overlay  
- Student project info & team credits in the menu

---

## Directory Structure

```
Tetris_Game/
├── .venv/                 # Virtual environment
├── assets/
│   ├── fonts/
│   │   ├── NotoSans-Bold.ttf
│   │   ├── NotoSans-Regular.ttf
│   ├── images/
│   │   └── game_screenshot.png
│   └── sounds/
│       ├── clear.wav
│       ├── drop.wav
│       ├── move.wav
│       └── rotate.wav
├── data/
│   └── leaderboard.json
├── src/
│   ├── core/
│   │   ├── board.py
│   │   ├── game_manager.py
│   │   ├── leaderboard.py
│   │   ├── settings.py
│   │   └── tetromino.py
│   ├── ui/
│   │   ├── menu.py
│   │   └── ui_renderer.py
├── main.py
├── README.md
└── pyproject.toml          # uv package manager config
```

---

## Environment Setup

1. **Python**: `>=3.10`  
2. **Virtual environment**:  

```bash
python -m venv .venv
```

3. **Activate virtual environment**:

- Windows:
```bash
.venv\Scripts\activate
```
- macOS / Linux:
```bash
source .venv/bin/activate
```

4. **Install dependencies using `uv`**:
```bash
uv install
```

`pyproject.toml` example:
```toml
[project]
name = "tetris_project"
version = "1.0.0"
requires-python = ">=3.10"

[tool.uv]
venv = ".venv"
```

---

## Game Features

- Neon-themed Tetris board  
- Dynamic speed level based on cleared lines  
- Hard & soft drop  
- Pause / resume  
- Game Over screen with overlay background  
- Score, Level, Lines display  
- Leaderboard saved to `data/leaderboard.json`  
- Student menu with group name and members  

---

## Function Overview

### GameManager
- `update(dt)` – update the game every frame  
- `move_left()`, `move_right()` – move piece horizontally  
- `rotate_piece()` – rotate the current piece  
- `soft_drop()` – move piece down one step  
- `hard_drop()` – drop piece to the bottom  
- `lock_current()` – lock piece, clear lines, spawn next piece  
- `game_over_event()` – triggers game over, saves score to leaderboard  

### Board
- `valid_position(piece, dx, dy)` – check if piece can move/rotate  
- `place_piece(piece)` – place piece on the grid  
- `clear_lines()` – remove full lines, return cleared count  

### Tetromino
- Represents each Tetris piece  
- Holds shape, color, position, rotation  
- `rotate()` – rotate shape  
- `get_cells()` – returns occupied grid cells  

### UI Renderer
- `draw_board(board)` – draws the grid & blocks  
- `draw_piece(piece)` – draw current piece  
- `draw_ui_panel(game)` – score, level, lines panel  
- `render(game, paused)` – render game frame with optional pause overlay  
- Game Over overlay with score display  

### Menu
- Shows:
  - Game title  
  - Group name & student members (MSSV + Name)  
  - Instructions: `Press ENTER to Start or ESC to Quit`  

---

## How to Run

1. Activate virtual environment  
2. Run the game:
```bash
py main.py
```
3. In menu:
- `ENTER` – start game  
- `ESC` – quit game  
- During game:
  - Arrow keys – move / rotate  
  - `DOWN` – soft drop  
  - `SPACE` – hard drop  
  - `P` – pause / resume  
  - `R` – restart after Game Over  

---

## Contributing

1. Fork the repository  
2. Create your feature branch:  
```bash
git checkout -b feature/your-feature
```
3. Commit your changes:  
```bash
git commit -m "Add new feature"
```
4. Push to the branch:  
```bash
git push origin feature/your-feature
```
5. Open a pull request  

---

## Tasks Division for Students

| Student | Task |
|---------|------|
| Nguyễn Quốc Huy (22730075) | GameManager & Board logic |
| Trần Hữu Tài (22730094) | Tetromino shapes & rotation |
| Đồng Nguyễn Vũ Anh (25730007) | UI Renderer & score panel |
| Phạm Anh (25730009) | Menu & team info display |
| Lục Gia Mẫn (22730083) | Leaderboard & Game Over handling |

---

## Notes

- Make sure fonts (`NotoSans-Bold.ttf`, `NotoSans-Regular.ttf`) are available to correctly render Vietnamese characters  
- Sounds are optional; the game works without them  
- The game automatically saves top 10 scores to `data/leaderboard.json`  
- Recommended screen resolution: 1280x720 for proper layout

---

## Images

![Gameplay](assets/images/game_screenshot.png)

---

## License

This project is for educational purposes only.