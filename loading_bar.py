import time
import sys

def simulate_loading(duration=20, bar_length=40):
    """
    Simulates a loading process for a given duration
    and displays a progress bar.
    """
    print(f"\nSimulating a task for {duration} seconds...")
    
    # Iterate over the total number of "steps"
    # More steps = smoother animation
    steps = 100 
    for i in range(steps + 1):
        # Calculate percentage
        percent = i
        
        # Calculate how many blocks to fill in the bar
        filled_length = int(bar_length * i // steps)
        
        # Create the bar string
        bar = "█" * filled_length + '-' * (bar_length - filled_length)
        
        # Create the output string
        # \r moves the cursor to the start of the line
        # end="" prevents it from adding a newline
        output_string = f'\rProgress: |{bar}| {percent}% Complete'
        
        sys.stdout.write(output_string)
        sys.stdout.flush()
        
        # Simulate work by sleeping
        time.sleep(duration / steps)
        
    print("\n\n✅ Task complete!")

# --- Main execution block ---
if __name__ == "__main__":
    try:
        simulate_loading()
    except KeyboardInterrupt:
        print("\n\nLoading cancelled by user.")
