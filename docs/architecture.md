# Architecture

Data Drift is a lightweight, modular Python arcade game built with Pygame. The architecture is intentionally simple, offline-first, and easy to extend for contributors.

---

## Project Structure

```

data-drift/
│
├── main.py                  # Core game loop (entry point)
├── requirements.txt         # Dependencies
├── README.md                # Project overview
├── LICENSE                  # Open-source license
│
├── game/
│   ├── player.py            # Player movement + animation
│   ├── enemy.py             # Data error entities (obstacles)
│   ├── score.py             # Scoring + combo system
│
├── assets/
│   ├── icons/               # UI icons (NULL, DUP, OUTLIER, TYPE)
│   ├── sounds/              # Future audio effects
│   ├── sprites/             # Player/enemy visual assets (optional)
│
├── docs/
│   ├── overview.md
│   ├── gameplay.md
│   ├── mechanics.md
│   ├── enemies.md
│   ├── player.md
│   ├── architecture.md
│   ├── roadmap.md
│
└── tests/
└── test_core.py         # Basic game logic tests (future expansion)

```

---

## Core Systems

### 1. Game Loop (`main.py`)
- Initializes Pygame
- Handles input, rendering, and updates
- Controls spawn timing and difficulty scaling
- Runs at 60 FPS game tick

---

### 2. Player System (`game/player.py`)
- Left/right movement only
- Smooth arcade-style animation
- Trail effect for motion feedback
- Collision boundary enforcement

---

### 3. Enemy System (`game/enemy.py`)
- Generates data quality issues as obstacles
- Uses lane-based spawning for fairness
- Each enemy type has a unique visual language
- Handles movement and collision hitboxes

---

### 4. Score System (`game/score.py`)
- Tracks survival score
- Implements combo multiplier system
- Resets combo on failure events
- Drives progression difficulty indirectly

---

## Design Principles

### Simplicity First
No complex engine dependencies or backend systems.

### Offline-First
Game runs fully without internet access.

### Modular Design
Each system is isolated to encourage easy contribution.

### Visual Clarity
Every enemy represents a real-world data issue using familiar analyst UI metaphors (Excel, tables, charts).

---

## Extensibility

The architecture supports future upgrades such as:

- Sound system integration
- Sprite-based animations
- New enemy types (data drift, null propagation, schema mismatch)
- Game modes (challenge, endless, timed runs)
- UI dashboard overlays (Power BI-style HUD)

---

## Summary

This architecture prioritizes:

- fast gameplay loop
- readability for contributors
- easy expansion
- strong thematic alignment with data analytics concepts