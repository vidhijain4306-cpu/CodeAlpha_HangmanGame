# CodeAlpha Internship - Task 1: Hangman Game
# Created by: Vidhi

import random

# ASCII Art for Hangman stages (0 to 6 incorrect guesses)
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

# List of 5 predefined words as per CodeAlpha requirements
WORDS = ["PYTHON", "DEVELOPER", "INTERNSHIP", "PROGRAMMING", "CODEALPHA"]
MAX_INCORRECT_GUESSES = 6


def display_game_status(secret_word, guessed_letters, incorrect_guesses):
    """
    Displays the hangman art, current word progress with blanks,
    and already guessed letters.
    """
    # Print the Hangman stage corresponding to incorrect guesses count
    print(HANGMAN_PICS[incorrect_guesses])
    
    # Display the word with guessed letters and underscores for unguessed
    word_display = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("Word: " + " ".join(word_display))
    
    # Display guessed letters and remaining attempts
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
    print("-" * 40)


def get_player_guess(guessed_letters):
    """
    Prompts the player for a guess and validates the input.
    Ensures input is a single alphabetic character not already guessed.
    """
    while True:
        guess = input("Enter a letter: ").strip().upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single alphabetical letter (A-Z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


def play_hangman():
    """
    Main game loop for Hangman.
    """
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    incorrect_guesses = 0
    
    print("=" * 40)
    print("      WELCOME TO CODEALPHA HANGMAN      ")
    print("=" * 40)
    print("Guess the secret word one letter at a time!")
    print(f"You are allowed a maximum of {MAX_INCORRECT_GUESSES} incorrect guesses.\n")
    
    # Main game loop
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        display_game_status(secret_word, guessed_letters, incorrect_guesses)
        
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in secret_word:
            print(f"\nGood job! '{guess}' is in the secret word!")
        else:
            incorrect_guesses += 1
            print(f"\nOops! '{guess}' is not in the word.")
        
        # Check if the player has guessed all letters in secret_word
        is_word_guessed = all(letter in guessed_letters for letter in secret_word)
        if is_word_guessed:
            display_game_status(secret_word, guessed_letters, incorrect_guesses)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"You correctly guessed the word: {secret_word}")
            break
    else:
        # Loop finished without break (incorrect_guesses reached MAX_INCORRECT_GUESSES)
        display_game_status(secret_word, guessed_letters, incorrect_guesses)
        print("💀 GAME OVER! YOU RAN OUT OF GUESSES! 💀")
        print(f"The secret word was: {secret_word}")


def main():
    while True:
        play_hangman()
        print("\n" + "=" * 40)
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("\nThank you for playing CodeAlpha Hangman! Goodbye!")
            break
        print("\n")


if __name__ == "__main__":
    main()
