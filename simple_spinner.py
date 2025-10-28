import curses
import time
import sys

def main(stdscr):
    """
    Main function called by curses.wrapper to run the spinner.
    'stdscr' is the main screen window.
    """
    
    # --- Curses Setup ---
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True) # Make getch() non-blocking
    stdscr.timeout(100) # Refresh every 100ms
    
    # --- Spinner Animation ---
    spinner_chars = ['|', '/', '—', '\\']
    spinner_index = 0
    
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
            
        stdscr.clear()
        
        # Get screen dimensions
        h, w = stdscr.getmaxyx()
        
        # Get the current character for the spinner
        char = spinner_chars[spinner_index]
        
        # Calculate center position
        center_y = h // 2
        center_x = w // 2
        
        # Draw the spinner character
        try:
            stdscr.addstr(center_y, center_x, char)
            stdscr.addstr(0, 0, "Press 'q' to quit")
        except curses.error:
            pass # Ignore error if window is too small
            
        stdscr.refresh()
        
        # Move to the next character
        spinner_index = (spinner_index + 1) % len(spinner_chars)

# --- Main execution block ---
if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            import curses
        except ImportError:
            print("ERROR: On Windows, 'curses' is not built-in.")
            print("Please run: pip install windows-curses")
            sys.exit(1)
            
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        print("Spinner stopped.")
