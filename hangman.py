import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'algorithm']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word: " + " ".join(guessed_word))

    while attempts > 0 and '_' in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        print("Word: " + " ".join(guessed_word))

    if '_' not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)

# Run the game
hangman()

