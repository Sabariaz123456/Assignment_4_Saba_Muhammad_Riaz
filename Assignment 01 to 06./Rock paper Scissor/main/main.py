import random

# Define emoji representations for Rock, Paper, Scissors
emoji_choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Emojis for different stages of the game
emoji_results = {
    "win": "🎉🥳🎊",
    "lose": "💻😞💔",
    "tie": "🤝😌"
}

emoji_feedback = {
    "easy": "😌",
    "medium": "😏",
    "hard": "😈"
}

def get_user_choice():
    """Prompts the user to select Rock, Paper, or Scissors using emojis."""
    while True:
        user_choice = input("Enter your choice (rock 🪨, paper 📄, or scissors ✂️): ").lower()
        if user_choice in emoji_choices:
            return user_choice
        else:
            print("Invalid choice. Please choose either 'rock 🪨', 'paper 📄', or 'scissors ✂️'.")

def get_computer_choice(difficulty):
    """Randomly selects Rock, Paper, or Scissors for the computer with difficulty adjustment."""
    if difficulty == 'easy':
        return random.choice(["rock", "paper", "scissors"])  # Random choice
    elif difficulty == 'medium':
        # The computer is slightly biased (more likely to pick 'rock')
        return random.choice(["rock", "rock", "paper", "scissors"])
    else:
        # Hard mode: The computer picks the next choice based on your last move
        return last_player_choice()

def last_player_choice():
    """Returns the computer's counter move based on the user's last choice."""
    if last_choice == "rock":
        return "paper"  # Paper beats rock
    elif last_choice == "paper":
        return "scissors"  # Scissors beats paper
    elif last_choice == "scissors":
        return "rock"  # Rock beats scissors

def decide_winner(user_choice, computer_choice):
    """Decides the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return f"It's a tie! {emoji_results['tie']}"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return f"You win! {emoji_results['win']}"
    else:
        return f"Computer wins! {emoji_results['lose']}"

def play_game():
    """Main function to play Rock, Paper, Scissors."""
    global last_choice
    print("Welcome to Rock, Paper, Scissors! ✂️📄🪨")
    
    # Choose difficulty
    difficulty = input("Select difficulty (easy 😌, medium 😏, hard 😈): ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid difficulty. Please choose 'easy 😌', 'medium 😏', or 'hard 😈'.")
        difficulty = input("Select difficulty (easy 😌, medium 😏, hard 😈): ").lower()

    # Best of series
    rounds = int(input("How many rounds would you like to play? (e.g., 3, 5): "))
    rounds_to_win = rounds // 2 + 1  # To win the series

    user_score = 0
    computer_score = 0
    print(f"Best of {rounds} rounds. First to {rounds_to_win} wins! 🏆")
    
    # Hint system and previous choice tracking
    round_num = 0
    last_choice = None
    
    while user_score < rounds_to_win and computer_score < rounds_to_win:
        round_num += 1
        print(f"\nRound {round_num}: ⚡")
        
        # User's choice with emojis
        user_choice = get_user_choice()
        print(f"You chose: {emoji_choices[user_choice]} 🤔")
        last_choice = user_choice  # Track last choice for computer's hard mode
        
        # Computer's choice based on difficulty
        computer_choice = get_computer_choice(difficulty)
        print(f"Computer chose: {emoji_choices[computer_choice]} 🤖")
        
        # Determine winner and update score
        result = decide_winner(user_choice, computer_choice)
        print(result)
        
        if result == f"You win! {emoji_results['win']}":
            user_score += 1
        elif result == f"Computer wins! {emoji_results['lose']}":
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score} 🥅")
        
        # Hint for next round (only if difficulty is medium or hard)
        if difficulty != 'easy':
            print(f"Hint: The computer might pick {emoji_choices[computer_choice]} next time! 🧐")

    print("\nGame Over! 🎮👑")
    if user_score > computer_score:
        print(f"You won the series with {user_score} points! 🎉🥳🎊")
    elif user_score < computer_score:
        print(f"Computer won the series with {computer_score} points! 💻😞💔")
    else:
        print(f"It's a tie overall! 🤝🎉")

    play_again = input("\nDo you want to play again? (yes 🙋‍♂️/no 👋): ").lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing! Goodbye. 👋💫")

# Start the game
play_game()
