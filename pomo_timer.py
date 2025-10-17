import time
import sys

# --- Settings ---
WORK_MINUTES = 25
BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15

def run_countdown(minutes, session_type):
    """Runs a countdown for a given number of minutes."""
    total_seconds = minutes * 60
    
    print(f"\n--- {session_type} started! ---")
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"\rTime remaining: {time_format} ")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
        
    print(f"\n--- {session_type} over! ---\n")
    # Simple alert sound (works on most terminals)
    print("\a") 

def pomodoro_timer():
    """Main function to run the Pomodoro timer cycles."""
    print("🍅 Pomodoro Productivity Timer 🍅")
    print("Press Ctrl+C to exit at any time.")
    
    cycles = 0
    try:
        while True:
            run_countdown(WORK_MINUTES, "Work Session")
            cycles += 1
            
            # After 4 cycles, take a long break
            if cycles % 4 == 0:
                run_countdown(LONG_BREAK_MINUTES, "Long Break")
            else:
                run_countdown(BREAK_MINUTES, "Short Break")

    except KeyboardInterrupt:
        print("\n\nTimer stopped. Great work!")

# --- Main execution block ---
if __name__ == "__main__":
    pomodoro_timer()
