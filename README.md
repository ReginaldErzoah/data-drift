# Data Drift

<p align="left">
  <img src="https://github.com/ReginaldErzoah/data-drift/blob/main/assets/images/datadrift-logo.png" width="400" alt="Data Drift Logo">
</p>

![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

## What is Data Drift?

**Data Drift** is a fast-paced offline arcade game where you survive a stream of corrupted data while working as a glowing **Data Node**.

You move left and right to avoid failing data systems and survive as long as possible.

Now available in two formats:

* Standalone Python Game
* VS Code Extension (one-click launch inside editor)

---

## VS Code Extension Mode (NEW)

Data Drift can now be launched directly inside VS Code.

### Features

* One-click game launch from sidebar
* Built for quick focus breaks during coding
* Runs completely offline
* Launches bundled executable instantly
* No setup required for end users

### How to Use (Extension)

1. Install the VSIX extension
2. Open VS Code sidebar
3. Click **Data Drift**
4. Press **Play Data Drift**
5. Game launches instantly

---

## Game Objective

* Survive as long as possible
* Avoid corrupted data objects
* Score increases over time
* Difficulty scales dynamically

---

## Controls

| Key           | Action     |
| ------------- | ---------- |
| < Left Arrow  | Move Left  |
| > Right Arrow | Move Right |

---

## Game Rules

* Touching corrupted data = Game Over
* Longer survival = Higher score
* Speed increases progressively

---

## Data Identity System

Each falling object represents a real-world data issue:

* **NULL** → missing data anomaly
* **DUP** → duplicate records
* **OUTLIER** → extreme values
* **BAD TYPE** → schema mismatch

---

## Tech Stack

* Python
* Pygame
* Node.js (VS Code extension layer)
* VS Code Extension API
* PyInstaller (for EXE packaging)

---

## File Setup & Distribution

This project now supports **three distribution layers**:

### 1. VS Code Extension (Recommended)

Used to launch the game directly inside VS Code.

```
datadrift-vscode-extension/
│
├── extension.js
├── package.json
├── icons/
├── dist/
│   └── DataDrift.exe
└── README.md
```

Install via:

* `.vsix` file OR GitHub Releases

---

### 2. Standalone Game (Python Source)

Original game version:

```
data-drift/
│
├── main.py
├── game/
├── assets/
├── requirements.txt
└── README.md
```

Run locally:

```bash
python main.py
```

---

### 3. Packaged Executable (Offline Mode)

Used by VS Code extension:

```
dist/DataDrift/
├── DataDrift.exe
└── _internal/
```

This is bundled and launched automatically.

---

## Why this project exists

This project was built to:

* Make coding breaks more engaging
* Help data professionals reset focus
* Visualize data quality issues creatively
* Experiment with game-based productivity tools
* Explore VS Code extension + game hybrid systems

---

## Future Improvements

* Sound effects system
* Leaderboard system
* Web version (browser playable)
* Enhanced VS Code integration (timer + analytics)

---

## Contributing

Pull requests are welcome.

Ideas encouraged:

* gameplay tuning
* UI improvements
* performance optimization
* VS Code UX enhancements

---

## License

MIT License

---

## Author

Built by **Reginald Erzoah**