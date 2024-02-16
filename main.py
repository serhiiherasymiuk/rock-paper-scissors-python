import random


def get_user_choice():
    """Prompt the user to input their choice and validate it."""
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice


def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def display_choices(user_choice, computer_choice):
    """Display the choices made by the user and the computer."""
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)


def play_game():
    """Main function to play the Rock, Paper, Scissors game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    display_choices(user_choice, computer_choice)
    print(determine_winner(user_choice, computer_choice))


# Run the game
if __name__ == "__main__":
    play_game()


