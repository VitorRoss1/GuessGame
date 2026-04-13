# Python Mini Games Collection

A collection of terminal-based mini games developed in Python.  
This repository focuses on fundamental programming concepts, clean structure, and logical problem-solving.

---

## Overview

This project contains small standalone games implemented in Python 3. Each game is designed to reinforce core programming concepts such as:

- Control flow
- Functions & Classes (OOP)
- Input validation
- Loops and conditionals
- Basic game logic

---

## Project Structure
Python-Lil-games/

├── A-blackJack.py

├── B-warGame.py

├── C-tictactoe.py

├── D-guessing.py

└── README.md


---

## Implemented Games

###  B) War Card Game

**File:** `B-warGame.py`

A simulation of the classic card game **War**, played automatically between two players (P1 vs P2). A full 52-card deck is shuffled and split evenly. Each round, both players flip their top card — highest value wins both cards. In case of a tie, **WAR** is triggered and each player puts down 5 extra cards, with the last one deciding the outcome.

#### Key Features

- Object-oriented design with `Card`, `Deck`, and `Playaa` classes
- Full 52-card deck with suit and rank mapping to integer values
- Automatic round-by-round simulation with console output
- War mechanic: tie triggers a 5-card war sequence
- Edge case handling: player eliminated if they have fewer than 5 cards during war
- Win condition detection for both players

#### Concepts Used

- OOP (classes, `__init__`, `__str__`, encapsulation)
- Dictionaries for rank-to-value mapping
- List manipulation (`.pop()`, `.append()`, `.extend()`)
- Nested `while` loops for game and war logic

---

###  C) Tic Tac Toe

**File:** `A-tictactoe.py`

A two-player command-line implementation of the classic Tic Tac Toe game.

#### Key Features

- Two-player turn-based system
- Board state management
- Win condition detection
- Draw detection
- Input validation

---

### D) Guessing Game

**File:** `B-guessing.py`

A number guessing game where the player attempts to guess a randomly generated number within a defined range.

#### Key Features

- Random number generation
- Attempt counter
- Feedback system (higher/lower hints)
- Input validation

---

## How to Run

Ensure Python 3 is installed on your system.

Navigate to the project directory and run a game:

```bash
python B-warGame.py
python C-tictactoe.py
python D-guessing.py
```

---

## Requirements

- Python 3.x
- No external dependencies

---

## Author

**Vítor Rossi**

Developed as part of an ongoing Python learning journey focused on strengthening programming fundamentals and practical implementation skills.

