# Tetris Game with Python

A classic Tetris clone built with Python and Pygame. The game uses asyncio to support running smoothly in a web browser, so you can play it online.

---

## Play Online

**[Play Tetris in your Browser Here.](https://revathii-nair.github.io/Tetris/)**

---

## How to Play

- **← Left Arrow**: Move the block left
- **→ Right Arrow**: Move the block right
- **↑ Up Arrow**: Rotate the block clockwise
- **↓ Down Arrow**: Drop the block faster
- **Enter / Return**: Restart the game after _GAME OVER_

---

## Features

- **Classic Gameplay**: All 7 Tetromino blocks (I, J, L, O, S, T, Z) with rotation logic.
- **Next Block Preview**: Plan ahead with a visible upcoming piece.
- **Scoring System**: Line clears award points (100, 200, 500, 1000 depending on number of lines cleared).
- **High Score Tracking**: Keeps your best score during the session.
- **Browser Ready**: Uses `pygbag` with an asynchronous game loop for smooth play online.

---

## Project Structure

- `main.py` → Async game loop, event handling, rendering
- `game.py` → Core logic: spawning, collisions, scoring
- `grid.py` → 20×10 playfield, line clears
- `block.py` & `blocks.py` → Tetromino definitions + rotations
- `build/web/` → Browser build output for GitHub Pages

---

## Prerequisites

1. Install Python 3.x
2. Install Pygame:
   ```bash
   pip install pygame
   ```

## Run Locally

1. Clone this repo:
   ```bash
   git clone https://github.com/Revathii-Nair/Tetris.git
   cd tetris
   ```
2. Run the game
   ```bash
   python main.py
   ```
