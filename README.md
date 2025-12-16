# Tetris Neon Project

## Table of Contents
- [Tetris Neon Project](#tetris-neon-project)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Directory Structure](#directory-structure)
  - [Environment Setup](#environment-setup)
  - [How to Run](#how-to-run)
  - [Game Features](#game-features)
  - [Student Task Assignment](#student-task-assignment)
  - [Contribution Guidelines](#contribution-guidelines)
  - [Visual Diagrams](#visual-diagrams)
    - [Directory Structure](#directory-structure-1)
    - [Game Flow Diagram](#game-flow-diagram)
  - [License](#license)

---

## Project Overview
Tetris Neon is a Python-based Tetris game with neon-themed graphics using `pygame`. The project is structured with modular components for UI rendering, game logic, settings, and leaderboard management. The game supports score tracking, line clearing, game over detection, and a leaderboard.

---

## Directory Structure
```
Tetris_Game/
├─ .venv/                  # Python virtual environment
├─ assets/
│  ├─ fonts/               # Fonts including NotoSans for Vietnamese support
│  ├─ sounds/              # Sound effects for move, rotate, drop, clear
├─ data/
│  └─ leaderboard.json     # Leaderboard storage
├─ src/
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ board.py          # Handles the game board and line clearing
│  │  ├─ game_manager.py   # Main game logic: spawning, movement, score, game over
│  │  ├─ leaderboard.py    # Save/load scores
│  │  ├─ settings.py       # GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, offsets, FPS, window size
│  │  └─ tetromino.py      # Tetromino pieces and rotations
│  ├─ ui/
│  │  ├─ __init__.py
│  │  ├─ menu.py           # Menu system: start/quit, group info display
│  │  └─ ui_renderer.py    # Drawing board, pieces, UI panel, pause/game over
│  └─ main.py              # Entry point: initialize pygame, loop, input handling
├─ README.md               # Project documentation
├─ pyproject.toml          # Project management with UV package manager
└─ requirements.txt        # Python dependencies
```

---

## Environment Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Tetris_Game
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .\.venv\Scripts\activate   # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or using UV package manager:
   ```bash
   uv sync
   ```

---

## How to Run
Run one of the following commands depending on your Python installation:
```bash
# Windows
py main.py

# Or
python main.py

# Or
python3 main.py
```
Controls:
- **LEFT/RIGHT ARROWS**: Move piece
- **UP ARROW**: Rotate piece
- **DOWN ARROW**: Soft drop
- **SPACE**: Hard drop
- **P**: Pause/Resume
- **R**: Restart after Game Over
- **ESC**: Quit

---

## Game Features
- Neon-themed Tetris graphics.
- Score calculation based on cleared lines and level.
- Level progression increases falling speed.
- Hard drop and soft drop mechanics.
- Pause and resume functionality.
- Game Over detection with visual overlay.
- Leaderboard: top 10 scores saved in `data/leaderboard.json`.
- Vietnamese font support for menu and member names.

---

## Student Task Assignment
| Student ID  | Name                   | Task |
|------------|------------------------|--------------------------------------|
| 22730075   | Nguyễn Quốc Huy        | Admin, core game manager, leaderboard, main.py |
| 22730094   | Trần Hữu Tài           | Tetromino shapes, piece movement logic |
| 25730007   | Đồng Nguyễn Vũ Anh     | Board logic, line clearing, collision detection |
| 25730009   | Phạm Anh               | UI rendering, pause/game over screen, fonts/sounds integration |
| 22730083   | Lục Gia Mẫn            | Menu system, start/quit, group info display, Vietnamese fonts |

---

## Contribution Guidelines
- Fork the repository.
- Create a branch for your feature:
  ```bash
  git checkout -b feature/my-feature
  ```
- Make changes and test thoroughly.
- Commit with descriptive message:
  ```bash
  git commit -m "Add feature XYZ"
  ```
- Push to your fork:
  ```bash
  git push origin feature/my-feature
  ```
- Create a pull request for review.

---

## Visual Diagrams
### Directory Structure
```
Tetris_Game
├─ src
│  ├─ core
│  │  ├─ board.py
│  │  ├─ game_manager.py
│  │  ├─ leaderboard.py
│  │  ├─ settings.py
│  │  └─ tetromino.py
│  ├─ ui
│  │  ├─ menu.py
│  │  └─ ui_renderer.py
│  └─ main.py
├─ assets
│  ├─ fonts
│  └─ sounds
├─ data
└─ README.md
```

### Game Flow Diagram
```
[ Menu ] --Enter--> [ Game Loop ] --Lines cleared/lock piece--> [ Score Update / Level Up ]
         \                                            
          ESC                                            
           \                                            
            Quit                                      
[ Pause (P) ] --Resume--> [ Game Loop ]
[ Game Over ] --R--> [ Menu / Restart ]
```

---

## License
MIT License

