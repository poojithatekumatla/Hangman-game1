import random

# Predefined list of words
words = ["python", "hangman", "computer", "science", "program"]

# Randomly choose one word
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman Game!")
print("You have 6 chances to guess the word.")

# Main game loop
while attempts_left > 0:
    # Display the current word with underscores for unguessed letters
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts_left)

    # Check if the player has guessed all letters
    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break

    # Take input from the player
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Add guessed letter
    guessed_letters.append(guess)

    # Check guess
    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1

# Game over condition
if attempts_left == 0:
    print("\n💀 Game Over! The word was:", word_to_guess)
