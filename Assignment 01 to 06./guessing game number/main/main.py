import random
import time

def get_difficulty_level():
    print("Choose your difficulty level:")
    print("1. Easy (1 to 50)")
    print("2. Medium (1 to 100)")
    print("3. Hard (1 to 200)")
    
    while True:
        try:
            choice = int(input("Enter the difficulty level (1/2/3): "))
            if choice == 1:
                return 50
            elif choice == 2:
                return 100
            elif choice == 3:
                return 200
            else:
                print("Invalid choice. Please select a valid level (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")

def guessing_game():
    print("Welcome to the Guessing Number Game!")
    difficulty_max = get_difficulty_level()
    print(f"\nI am thinking of a number between 1 and {difficulty_max}.")
    
    number_to_guess = random.randint(1, difficulty_max)
    attempts = 0
    guessed_correctly = False
    
    start_time = time.time()  # Start the timer

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                end_time = time.time()  # End the timer
                time_taken = round(end_time - start_time, 2)  # Calculate time taken
                print(f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                print(f"You took {time_taken} seconds to guess the number.")
                
                play_again = input("\nWould you like to play again? (yes/no): ").lower()
                if play_again == 'yes':
                    guessing_game()
                else:
                    print("Thank you for playing! Goodbye.")
                    break
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guessing_game()
