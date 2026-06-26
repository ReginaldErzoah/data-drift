# Data Drift - Roadmap
> A lightweight, offline, addictive arcade survival game with data-themed visuals.

---

# Phase 1 - Core Arcade Foundation (Completed)

## Goal

Build a working Chrome Dino-style survival game.

### Features

* Player left/right movement
* Enemy spawning system
* Collision detection
* Score tracking
* Game over + restart
* Basic background + grid

---

# Phase 2 - Visual Polish Upgrade (Completed)

## Goal

Make the game feel like a real indie arcade title.

### Features

* Glow-based player design
* Enemy type visuals (NULL, DUP, OUTLIER, TYPE)
* Grid-based background system
* Particle noise layer
* Improved motion feel

---

# Phase 3 - Game Feel & Juice (Current Focus)

## Goal

Make gameplay feel responsive and satisfying (Chrome Dino-level polish)

---

### 1. Juice System 

* Screen shake on collision
* Flash feedback on hit
* Particle burst effects
* Micro impact feel

---

### 2. Difficulty Curve 

* Controlled speed increase
* Structured escalation
* No randomness spikes

---

### 3. Animation Polish 

* Smooth trail fading
* Better motion consistency
* Frame stability improvements

---

# Phase 4 - Packaging & Distribution (NEW FOCUS)

## Goal

Make the game easily installable and playable anywhere.

---

## 1. Windows EXE Build

* PyInstaller packaging
* Single-file executable option
* Offline-first design

---

## 2. VSCode Extension Version

### Purpose:

A “break tool” for developers

### Features:

* Launch game from VSCode sidebar
* Lightweight embedded runtime
* Pause-work -> play 2–5 min session
* Resume coding instantly

---

## 3. Web Version (Offline-capable plugin)

* Pygame -> Web (via pygbag or similar)
* Runs in browser
* No backend required
* Embeddable as “break game widget”

---

# Phase 5 - UX & Retention Polish

## Goal

Make it addictive but simple

---

### Features

* Instant restart loop (R key)
* Clean game-over screen
* High score emphasis
* Smooth transition into replay

---

# Phase 6 - Open Source & Community (Lightweight)

## Goal

Allow minimal contributions without complexity

---

### Allowed contributions:

* Skins (visual only)
* New enemy types (simple sprites)
* UI tweaks
* Sound packs

---

### NOT allowed:

* gameplay system changes
* intelligence layers
* data simulation systems

# OPTIONAL UPDATES
## Minimal Audio Layer

* hit.wav
* game_over.wav
* ui_click.wav
* ambient.wav (low volume background loop)
