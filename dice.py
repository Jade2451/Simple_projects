import random

def roll_dice():
    """
    Main function to simulate rolling dice.
    """
    print("🎲 Dice Roll Simulator 🎲")
    
    while True:
        try:
            # --- Get User Input ---
            num_dice = int(input("\nHow many dice do you want to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number.")
                continue

            # --- Roll the Dice ---
            rolls = []
            for _ in range(num_dice):
                roll = random.randint(1, 6)
                rolls.append(roll)
            
            # --- Display Results ---
            print("\n--- You rolled: ---")
            for i, roll in enumerate(rolls, 1):
                print(f"  Die {i}: {roll}")
            print("-------------------")
            print(f"  Total: {sum(rolls)}")

        except ValueError:
            print("Invalid input. Please enter a whole number.")
        
        # --- Ask to roll again ---
        roll_again = input("\nRoll again? (y/n): ").lower()
        if roll_again != 'y':
            print("Thanks for rolling!")
            break

# --- Main execution block ---
if __name__ == "__main__":
    roll_dice()
