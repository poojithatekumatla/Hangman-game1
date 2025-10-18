import random


words = ["python", "hangman", "computer", "science", "program"]

word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman Game!")
print("You have 6 chances to guess the word.")


while attempts_left > 0:
    
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts_left)


    if all(letter in guessed_letters for letter in word_to_guess):
        print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
        break

   
    guess = input("Enter a letter: ").lower()

 
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

  
    guessed_letters.append(guess)

   
    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1


if attempts_left == 0:
    print("\n💀 Game Over! The word was:", word_to_guess)

