# Hangman Game 🎮

This is a simple command-line Hangman game written in Python. It was created as part of my web development internship task at **CodeAlpha**.

## 🧠 How It Works

- The game randomly selects a word from a predefined list.
- The player has to guess the word one letter at a time.
- The player has a total of **6 attempts**.
- Already guessed letters cannot be entered again.
- The game ends when the player guesses the word or runs out of attempts.

## 🛠️ Tech Used

- Python 3

## 📁 Files

- `hangman.py`: The main Python file that runs the Hangman game.
- `README.md`: This file.

## ▶️ How to Run

1. Make sure Python is installed on your system.
2. Open a terminal in the project directory.
3. Run the command:

   ```bash
   python hangman.py
   ```

## 💡 Sample Gameplay

```
Welcome to Hangman!
Guess the word: _ _ _ _ _ _ _ _
Enter a letter: a
Wrong guess! You have 5 attempts left.
Enter a letter: o
Good job! 'o' is in the word.
...
```

## 📌 Features

- Random word selection
- Input validation
- Case-insensitive guesses
- Attempt tracking
- Game over and success messages

