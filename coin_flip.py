import random
import time

def flip_coins():
    """
    Simulates flipping a coin a specified number of times.
    """
    print("🪙 Coin Flip Simulator 🪙")
    
    while True:
        try:
            # --- Get User Input ---
            num_flips = int(input("\nHow many times do you want to flip the coin? "))
            if num_flips <= 0:
                print("Please enter a positive number of flips.")
                continue

            # --- Initialize counters ---
            heads_count = 0
            tails_count = 0

            print("\nFlipping...")
            
            # --- Run the simulation ---
            for i in range(num_flips):
                # Animate the process slightly
                print(f"Flip {i+1}...", end='\r')
                time.sleep(0.01)
                
                if random.choice(['Heads', 'Tails']) == 'Heads':
                    heads_count += 1
                else:
                    tails_count += 1
            
            # --- Display Results ---
            print("\n\n" + "="*25)
            print("      Flip Results")
            print("="*25)
            print(f"  Heads: {heads_count} ({heads_count / num_flips:.2%})")
            print(f"  Tails: {tails_count} ({tails_count / num_flips:.2%})")
            print("="*25)

        except ValueError:
            print("Invalid input. Please enter a whole number.")
        
        # --- Ask to flip again ---
        flip_again = input("\nFlip again? (y/n): ").lower()
        if flip_again != 'y':
            print("Thanks for flipping!")
            break

# --- Main execution block ---
if __name__ == "__main__":
    flip_coins()
