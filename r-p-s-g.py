import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    choices = ['rock','paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def print_result(user_choice, computer_choice, winner):
    """Display the result of the round."""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0

    print("........Welcome to Rock-Paper-Scissors Game!..........")

    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print_result(user_choice, computer_choice, winner)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\nScore - You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\nThanks for playing!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
