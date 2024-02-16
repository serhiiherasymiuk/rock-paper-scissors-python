import random


def get_user_choice():
    """Prompt the user to input their choice and validate it."""
    valid_choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}

    while True:
        user_choice = input("Enter your choice (1 for rock, 2 for paper, 3 for scissors): ")
        if user_choice in valid_choices:
            return valid_choices[user_choice]
        else:
            print("Invalid choice. Please enter 1 for rock, 2 for paper, or 3 for scissors.")


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
