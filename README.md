# CodeAlpha - Task 1: Hangman Game

A Python console-based implementation of the classic **Hangman Game** developed as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
The objective of this task is to create a text-based Hangman game where the player attempts to guess a secret word by inputting one letter at a time, within a maximum allowed limit of incorrect attempts.

### 🎯 Key Requirements Met
- **Predefined Word Pool**: Uses 5 curated words (`PYTHON`, `DEVELOPER`, `INTERNSHIP`, `PROGRAMMING`, `CODEALPHA`).
- **Attempt Limit**: Limits incorrect guesses to 6 (represented via ASCII hangman stages).
- **Console Input / Output**: Pure command-line interface with clean ASCII art visual feedback.
- **Input Validation**: Ensures only single alphabet characters are accepted and prevents duplicate guesses without penalty.
- **Replayability**: Option to replay the game after finishing a round.

---

## 🧠 Key Python Concepts Utilized
- **`random` module**: Random selection of the target word (`random.choice`).
- **Control Flow**: `while` loops for continuous game states and `if-elif-else` conditional branching.
- **Data Structures**:
  - `lists` for word representation and ASCII art stages.
  - `sets` for efficient storage and lookup of guessed letters.
- **String Manipulation**: Case normalization (`.upper()`, `.lower()`), input stripping (`.strip()`), and string joining (`" ".join()`).
- **Functions & Clean Code**: Modularized functions (`display_game_status`, `get_player_guess`, `play_hangman`, `main`).

---

## 🚀 How to Run the Project

### Prerequisites
Make sure Python 3.x is installed on your system.

### Running the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/CodeAlpha_HangmanGame.git
   ```
2. Navigate into the project folder:
   ```bash
   cd CodeAlpha_HangmanGame
   ```
3. Run the Python script:
   ```bash
   python hangman.py
   ```

---

## 🎮 Game Demo / Rules
1. A secret word is randomly selected from the predefined list.
2. The player guesses one letter at a time.
3. If the letter exists in the secret word, it reveals its positions.
4. If the letter is not in the word, an incorrect guess is recorded and the hangman figure advances.
5. **Win Condition**: Guess all letters of the word before reaching 6 incorrect guesses.
6. **Lose Condition**: Reach 6 incorrect guesses before completing the word.

---

## 👤 Author
- **Author**: Vidhi
- **Internship**: Python Programming Internship at **CodeAlpha**
- **Website**: [CodeAlpha](https://www.codealpha.tech)
