import random

# List of words for the game
word_list = ['python', 'streamlit', 'hangman', 'computer', 'data', 'machine', 'learning', 'artificial', 'intelligence']
word_to_guess = random.choice(word_list)  # Select a random word from the list
guessed_word = ['_'] * len(word_to_guess)  # Initialize a list to store the guessed letters
attempts_left = 6  # Maximum number of wrong attempts

# Hangman art based on the number of attempts left
hangman_art = [
    '''
      ------
      |    |
           |
           |
           |
           |
     =========
    ''',
    '''
      ------
      |    |
      O    |
           |
           |
           |
     =========
    ''',
    '''
      ------
      |    |
      O    |
      |    |
           |
           |
     =========
    ''',
    '''
      ------
      |    |
      O    |
     /|    |
           |
           |
     =========
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
           |
           |
     =========
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
     =========
    ''',
    '''
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
     =========
    '''
]

# Function to update the guessed word and attempts
def update_game(letter):
    global attempts_left
    if letter in word_to_guess:
        for i, char in enumerate(word_to_guess):
            if char == letter:
                guessed_word[i] = letter
    else:
        attempts_left -= 1

# Main Game Loop
print("🖤 Hangman Game 💀")
print("Guess the word, letter by letter! You have 6 attempts before the hangman is fully drawn. 😱")
print("The word to guess is:", ' '.join(guessed_word))
print("You have", attempts_left, "attempts left.")
print("")

# Game Loop
while attempts_left > 0:
    print("\n" + "".join(guessed_word))
    print("\nAttempts left:", attempts_left)
    print("Guessed so far:", ' '.join([letter if letter in guessed_word else '_' for letter in word_to_guess]))
    print(hangman_art[6 - attempts_left])

    letter_guess = input("\nGuess a letter: ").lower()

    if len(letter_guess) == 1 and letter_guess.isalpha():
        if letter_guess in guessed_word:
            print("You already guessed that letter!")
        else:
            update_game(letter_guess)
    else:
        print("Please enter a valid letter.")

    if "_" not in guessed_word:
        print("\n🎉 You guessed the word:", word_to_guess, "🎉")
        break
else:
    print("\n💀 You lost! The word was:", word_to_guess, "💀")
