# Data Drift

> An offline, Chrome Dino-inspired arcade game built in Python for data professionals.

---

## What is Data Drift?

**Data Drift** is a simple, fast, and addictive offline game where you survive a stream of corrupted data.

You play as a glowing **Data Node**, moving left and right to avoid broken or corrupted data packets.

No internet. No setup complexity. Just pure arcade survival.

---

## Game Objective

- Survive as long as possible
- Avoid corrupted data objects
- Score increases the longer you survive
- Difficulty increases over time

---

## Controls

| Key | Action |
|-----|--------|
| '<' Left Arrow | Move Left |
| '>' Right Arrow | Move Right |

---

## Game Rules

- Touching corrupted data = Game Over
- Surviving longer = Higher Score
- Speed increases over time

---

## Game Identity

Each falling object represents a **data quality issue**:

- NULL > missing data anomaly  
- DUP > duplicate records  
- OUTLIER > extreme values  
- BAD TYPE > invalid schema  

---

## Tech Stack

- Python
- Pygame
- NumPy (optional future expansion)
- Pandas (future analytics mode)

---

## How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/data-drift.git
cd data-drift
````

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the game

```bash
python main.py
```

---

## Project Structure

```
data-drift/
│
├── main.py
├── requirements.txt
├── README.md
│
├── game/
│   ├── player.py
│   ├── enemy.py
│   ├── score.py
│
├── assets/
│   ├── fonts/
│   ├── sounds/
│   ├── images
│
├── docs/
└── tests/
```

---

## Why this project exists

This project was built to:

* Make offline coding more fun
* Give data professionals a quick arcade break
* Explore creative ways of visualizing data quality issues
* Build a minimalist but iconic Python game

---

## Future Ideas

* Sound effects
* Power-ups
* Combo system
* Boss “Data Crisis” mode 
* High score leaderboard
* Web version (Pygame > Web export) and chrome plugin

---

## Contributing

Pull requests are welcome.
Ideas, improvements, and game feel upgrades are encouraged.

---

## License

MIT License

---

## Credits

Built by Reginald Erzoah in Python
Inspired by Chrome Dino
Designed for data professionals & creators