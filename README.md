# Python_Project
# 🎯 Lucky Draw Game (Python)

A simple console-based Lucky Draw / Number Guessing Game written in Python.
The player has three chances to guess a randomly generated number and earn points.

==================================================

📌 GAME RULES

1. The user enters:
   - Lower Bound
   - Upper Bound
2. The program randomly selects a number between the given range.
3. The player has 3 chances to guess the number:
   - First Chance  → 30 Points
   - Second Chance → 20 Points
   - Third Chance  → 10 Points
4. Hints are provided after each wrong guess:
   - TOO LOW
   - TOO HIGH
5. If all attempts fail, the game displays:
   BETTER LUCK NEXT TIME

==================================================

🛠 REQUIREMENTS

- Python 3.x
- No external libraries required
- Uses Python's built-in random module

==================================================

▶ HOW TO RUN

1. Save the program as:
   lucky_draw.py

2. Open terminal / command prompt

3. Run the file:
   python lucky_draw.py

==================================================

🎮 SAMPLE OUTPUT

ENTER LOWER BOUND: 1
ENTER UPPER BOUND: 10

FIRST CHANCE: 5
TOO LOW
HAVE ONE MORE TRY

SECOND CHANCE: 8
SCORE = 20 POINTS!!!
CONGRATULATIONS

==================================================

📂 PROJECT STRUCTURE

lucky-draw-game/
│
├── lucky_draw.py
└── README.md

==================================================

✨ FEATURES

- Random number generation
- User-defined range
- Score-based system
- Hint messages
- Simple and clean console interface

==================================================

🚀 FUTURE IMPROVEMENTS

- Input validation
- Replay option
- Show correct number after losing
- High score tracking
- GUI version using Tkinter

==================================================

📄 LICENSE

Free to use for learning and educational purposes.
