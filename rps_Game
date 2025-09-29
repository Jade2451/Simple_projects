import random

def play_game():
    """
    Main function to run the Rock, Paper, Scissors game.
    """
    user_score = 0
    computer_score = 0
    
    print("🪨📄✂️ Welcome to Rock, Paper, Scissors! 🪨📄✂️")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    while True:
        # --- Get User and Computer Choices ---
        user_choice = input("\nYour choice: ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice}")

        # --- Determine the Winner ---
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("🤖 The computer wins this round!")
            computer_score += 1
            
        # --- Display Score ---
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # --- End of Game ---
    print("\n" + "="*25)
    print("    Final Score:")
    print(f"    You: {user_score} | Computer: {computer_score}")
    print("    Thanks for playing!")
    print("="*25 + "\n")


# --- Main execution block ---
if __name__ == "__main__":
    play_game()
