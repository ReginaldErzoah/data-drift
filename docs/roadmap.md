# Roadmap

Data Drift is designed as a long-term open-source arcade project that evolves from a simple offline survival game into a **fully immersive data-professional training experience disguised as a game**.

This roadmap defines the evolution in structured phases, from core gameplay to advanced data-themed systems.

---

# Phase 1 — Core Arcade Foundation (CURRENT)

## Goal
Build a stable, playable, Chrome Dino–style survival game.

---

## Completed / In Progress Features

### Player System
- Left/right movement only
- Smooth animation system (bounce + lean)
- Data stream trail effect
- Collision boundaries enforced

---

### Enemy System (Data Errors)
- NULL (missing values)
- DUP (duplicate rows)
- OUTLIER (data spikes)
- TYPE (schema mismatch)

- Lane-based spawning system (prevents safe zones)
- Consistent hitbox system
- Arcade-style downward movement

---

### Core Loop
- Continuous enemy spawning
- Survival-based scoring
- Collision = game over
- Increasing tension through spawn timing

---

### Score System
- Survival score tracking
- Combo multiplier system
- Reset on failure

---

## Technical Goals
- Maintain 60 FPS performance
- Keep game fully offline
- Keep dependencies minimal (Pygame only)

---

# Phase 2 — Visual Polish & Game Feel Upgrade

## Goal
Make the game feel like a **real polished indie arcade title**

---

## Player Enhancements
- Improved glow effects
- Stronger motion trail system
- Directional animation smoothing
- Optional skin variants (future expansion)

---

## Enemy Enhancements
- Stronger visual differentiation per error type
- Animated error states (pulse, flicker, shake)
- Improved clarity at high speed

---

## Environment Upgrade
- Excel-style grid background
- Subtle scrolling data layer
- Dark UI theme refinement
- Depth layering (foreground vs background)

---

## Feedback Effects
- Screen shake on collision
- Red flash on error hit
- Combo glow scaling effect

---

## Audio Layer (Optional but recommended)
- Soft movement sound
- Error collision sound
- Combo achievement sound

---

# Phase 3 — Data Intelligence Layer

## Goal
Turn gameplay into a **data-awareness experience**

---

## New Mechanics

### Data Events System
Random gameplay modifiers:

- “Data Spike Event” → faster enemies
- “Dirty Dataset Mode” → more NULLs spawn
- “Schema Drift Event” → TYPE errors increase
- “Replication Burst” → DUP enemies increase

---

## New Enemy Variants
- Data Drift anomaly (new category)
- Corrupt record enemy
- Late-arriving data packets
- Aggregation errors

---

## Skill Layer
- Combo-based scoring multipliers
- Perfect dodge bonus system
- Risk-reward lanes

---

# Phase 4 — Game Modes Expansion

## Goal
Expand replayability and engagement

---

## New Modes

### 1. Endless Mode (Default)
- Infinite survival
- Increasing difficulty curve

---

### 2. Challenge Mode
- Predefined datasets (scenarios)
- Fixed difficulty spikes
- Score benchmarking

---

### 3. Analyst Training Mode
- Teaches recognition of data issues
- Slower spawn rate
- Educational tooltips (optional)

---

## Custom Runs
- Seed-based runs
- Replay sharing system (future idea)

---

# Phase 5 — Data Ecosystem Expansion

## Goal
Evolve game into a **data learning ecosystem**

---

## Advanced Features

### Dataset-Themed Levels
- “E-commerce dataset”
- “Financial transactions”
- “Sensor data stream”
- “Healthcare records”

Each dataset changes:
- enemy frequency
- error types
- visual theme

---

### Dashboard Mode
- Full Power BI-style HUD overlay
- Real-time score analytics
- Combo heatmaps
- Error frequency tracking

---

### Player Progression System
- XP system for survival time
- Unlockable visual upgrades
- Titles:
  - Junior Analyst
  - Data Wrangler
  - Insight Engineer
  - Drift Survivor

---

# Phase 6 — Open Source Expansion

## Goal
Turn Data Drift into a community-driven ecosystem

---

## Community Features

- Custom enemy contributions
- New visual skins
- New dataset packs
- Difficulty mods

---

## Plugin System (Advanced)
Allow contributors to define:

- New error types
- Visual templates
- Game modifiers

---

## Packaging & Distribution
- PyInstaller builds (Windows executable)
- Linux build support (future)
- Offline portable mode

---

# Phase 7 — Advanced Vision (LONG TERM)

## Goal
Transform into a **data simulation arcade platform**

---

## Potential Future Expansion

- Multiplayer “data cleanup race”
- AI-generated dataset challenges
- Real-world anonymized dataset integration
- Procedural data error generation engine
- Educational institution integration

---

# Vision Statement

Data Drift evolves from:

> “a simple offline arcade game”

to:

> “a living simulation of data chaos that teaches intuition through play”

---

# Final Goal

To make data concepts:

- intuitive without reading documentation
- fun without losing meaning
- memorable through gameplay
- accessible offline to everyone

---

# Summary

This roadmap ensures Data Drift grows in three key dimensions:

1. Gameplay depth
2. Visual polish
3. Data intelligence realism

While always staying:

> lightweight, offline-first, and arcade-simple