# Design — Data Drift

## Visual Philosophy

Data Drift is designed around the concept of:
> "Readable chaos under increasing data pressure"

---

## Color System

- Background: deep dark blue (#0A0C14)
- Player: neon cyan glow
- Enemies:
  - Red (NULL)
  - Orange (DUP)
  - Purple (OUTLIER)
  - Yellow (TYPE ERROR)

---

## Visual Hierarchy

1. Player (highest priority clarity)
2. Enemies (adaptive readability)
3. Score UI
4. Background grid
5. Noise particles

---

## Motion Design

- Player uses sinusoidal bounce
- Enemies fall vertically with constant acceleration feel
- Screen shake triggers on collision
- VisualState controls intensity scaling