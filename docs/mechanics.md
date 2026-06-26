# Mechanics — Data Drift

## Movement

- Player moves horizontally
- Boundaries enforced by screen width

---

## Enemy System

Each enemy:
- Spawns randomly across full screen width
- Falls vertically
- Has type-based visual representation

---

## Collision System

Axis-aligned bounding box (AABB):

- Player rectangle
- Enemy rectangle

Collision triggers:
- Game over
- Screen shake
- Visual impact effect

---

## Difficulty Scaling

Every few seconds:
- speed_boost increases
- enemy speed increases
- readability mode escalates