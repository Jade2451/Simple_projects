import time
import sys

def countdown_timer(total_seconds):
    """
    Runs a countdown timer for a specified number of seconds.
    """
    print("Timer started! Press Ctrl+C to exit early.")
    try:
        while total_seconds > 0:
            # divmod returns a tuple of (quotient, remainder)
            mins, secs = divmod(total_seconds, 60)
            
            # Format the time string to always have two digits (e.g., 01:05)
            time_format = f"{mins:02d}:{secs:02d}"
            
            # Print on the same line and flush the output
            sys.stdout.write(f"\rTime remaining: {time_format}")
            sys.stdout.flush()
            
            time.sleep(1)
            total_seconds -= 1
            
        print("\n\n" + "="*20)
        print("    🔔 Time's up!    ")
        print("="*20 + "\n")

    except KeyboardInterrupt:
        print("\n\nTimer cancelled by user.")

# --- Main execution block ---
if __name__ == "__main__":
    print("⏱️ Command-Line Countdown Timer ⏱️")
    while True:
        try:
            seconds_input = int(input("Enter the countdown duration in seconds: "))
            if seconds_input > 0:
                countdown_timer(seconds_input)
                break
            else:
                print("Please enter a positive number of seconds.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
