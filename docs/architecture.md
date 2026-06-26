# Architecture — Data Drift

## System Overview

Data Drift is a real-time arcade simulation built on a layered game architecture using pygame.

The system is divided into five core layers:

---

## 1. Game Loop Layer (main.py)

Responsible for:
- Event handling
- Game state transitions
- Object updates
- Rendering order control

It acts as the central orchestrator.

---

## 2. Entity Layer

### Player
- Handles movement and boundary logic
- Maintains trail system for motion visualization
- Supports death collapse animation

### DataEnemy
- Procedurally spawned anomalies
- Uses adaptive readability modes
- Collision detection with player

---

## 3. World Layer

### Background
- Grid-based visual structure
- Floating data noise particles
- Dynamic scrolling illusion

---

## 4. Feedback Systems

### JuiceEngine
- Screen shake system
- Collision impact feedback

### VisualState
- Global difficulty visual controller
- Adjusts intensity based on score and speed boost

---

## 5. Scoring System

- Tracks survival time and evasion success
- Drives difficulty scaling