import random
import time

# --- Board Setup ---
# A dictionary where the key is the start square and the value is the end square.
SNAKES = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 79
}

LADDERS = {
    4: 14,
    9: 31,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    63: 81,
    71: 91
}

WINNING_SQUARE = 100

def roll_dice():
    """Simulates rolling a 6-sided die."""
    return random.randint(1, 6)

def play_game():
    """Main function to run the Snake and Ladders game."""
    player_position = 1
    turns = 0
    
    print("🐍 Welcome to Snakes and Ladders! 🪜")
    print(f"Your goal is to reach square {WINNING_SQUARE}.")
    
    while player_position < WINNING_SQUARE:
        print("\n" + "-"*30)
        print(f"You are currently on square {player_position}.")
        
        # --- Wait for user to roll ---
        input("Press ENTER to roll the dice...")
        
        roll = roll_dice()
        turns += 1
        print(f"You rolled a {roll}!")
        
        new_position = player_position + roll
        
        # --- Check game conditions ---
        if new_position == WINNING_SQUARE:
            player_position = new_position
            print(f"You moved to square {player_position}.")
            print(f"\n🎉 Congratulations! You reached square {WINNING_SQUARE} in {turns} turns!")
            break
        elif new_position > WINNING_SQUARE:
            print(f"Oops! You rolled a {roll}, which is too high. You must land exactly on {WINNING_SQUARE}.")
            print("You stay on square {player_position}.")
            continue
        else:
            player_position = new_position
            print(f"You moved to square {player_position}.")
            time.sleep(0.5) # Small pause for effect

        # --- Check for Snakes or Ladders ---
        if player_position in SNAKES:
            new_position = SNAKES[player_position]
            print(f"🐍 Oh no! You landed on a snake. You slide down from {player_position} to {new_position}.")
            player_position = new_position
            time.sleep(0.5)
            
        elif player_position in LADDERS:
            new_position = LADDERS[player_position]
            print(f"🪜 Wow! You landed on a ladder. You climb up from {player_position} to {new_position}!")
            player_position = new_position
            time.sleep(0.5)

    # --- Ask to play again ---
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

# --- Main execution block ---
if __name__ == "__main__":
    play_game()
