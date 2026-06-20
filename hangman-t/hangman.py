import random

# List of 5 predefined words
words = ["python", "apple", "computer", "school", "keyboard"]

# Choose a random word
word = random.choice(words)
 
# Create blanks
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

print("=== HANGMAN GAME ===")

while wrong_guesses < max_wrong and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if letter exists
    if guess in word:
        print("Correct!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong!")
        wrong_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)