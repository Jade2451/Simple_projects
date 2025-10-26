import time
import curses
import collections
import sys

def get_ecg_pattern():
    """
    Defines the PQRST complex as a series of vertical offsets
    from the baseline. Increase magnitudes for better vertical resolution.
    """
    # P-wave (small bump, more defined)
    p_wave = [0, 1, 2, 1, 0]
    
    # PR-segment (baseline)
    pr_segment = [0] * 8 # Slightly shorter for tighter curve
    
    # QRS-complex (the big spike: Q dip, R peak, S dip)
    qrs_complex = [-2, -6, 20, -10, 4, 0] 
    
    # ST-segment (baseline)
    st_segment = [0] * 10
    
    # T-wave (medium bump)
    t_wave = [0, 3, 5, 5, 3, 0]
    
    # Baseline
    baseline = [0] * 40 # Increased baseline length
    
    # Combine 
    return p_wave + pr_segment + qrs_complex + st_segment + t_wave + baseline

def run_ecg(stdscr):
    """
    Main animation function called by curses.
    'stdscr' is the main screen window provided by curses.
    """
    
    # --- Curses Setup ---
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(True)  # Don't block for key presses
    stdscr.timeout(30)  # Refresh every 30ms for smoother animation
    
    # --- Pattern and Data Setup ---
    pattern = get_ecg_pattern()
    pattern_len = len(pattern)
    pattern_index = 0
    
    # Get screen dimensions
    h, w = stdscr.getmaxyx()
    
    # Create a deque to hold the "history" of the wave.
    history = collections.deque([0] * (w - 1), maxlen=(w - 1))

    # Store the previous y-coordinate for drawing connecting lines
    prev_y = h // 2 

    while True:
        # --- Check for Quit ---
        key = stdscr.getch()
        if key == ord('q'):
            break
            
        # --- Get Screen Dimensions ---
        new_h, new_w = stdscr.getmaxyx()
        if new_h != h or new_w != w: # If window resized, clear and re-init history
            h, w = new_h, new_w
            # Re-initialize with baseline (0 offset) integers
            history = collections.deque([0] * (w - 1), maxlen=(w - 1))
            prev_y = h // 2 
            stdscr.clear()
            
        stdscr.clear() # Clear screen at each frame

        # --- Update Data ---
        # 1. Get the next value from our repeating pattern
        next_offset = pattern[pattern_index]
        pattern_index = (pattern_index + 1) % pattern_len
        
        # 2. Add it to our history. We'll decide the character during drawing.
        history.append(next_offset)

        # --- Draw the Animation ---
        center_y = h // 2 # Baseline position

        try:
            stdscr.addstr(center_y, 0, "_" * (w - 1))
        except curses.error:
            pass 

        
        for x in range(len(history)):
            current_offset = history[x]
            current_y = center_y - current_offset

            if x > 0:
                prev_offset = history[x-1]
                prev_y_for_connection = center_y - prev_offset

                if prev_y_for_connection != current_y:
                    step = 1 if current_y > prev_y_for_connection else -1
                    for y_fill in range(prev_y_for_connection, current_y, step):
                        if 0 <= y_fill < h and 0 <= x < w:
                            try:
                                stdscr.addch(y_fill, x, '█')
                            except curses.error:
                                pass
            
            if 0 <= current_y < h and 0 <= x < w:
                try:
                    stdscr.addch(current_y, x, '█')
                except curses.error:
                    pass

        # 3. Draw instructions
        stdscr.addstr(0, 0, "ECG Monitor - Press 'q' to quit")
        
        # --- Refresh the Screen ---
        stdscr.refresh()

def main():
    """
    Wrapper function to safely start and stop curses.
    """
    try:
        curses.wrapper(run_ecg)
    except KeyboardInterrupt:
        print("ECG Monitor stopped.")

# --- Main execution block ---
if __name__ == "__main__":
    # --- Platform-specific check for 'curses' ---
    if sys.platform == "win32":
        try:
            import curses
        except ImportError:
            print("="*50)
            print("ERROR: On Windows, this script requires the 'windows-curses' library.")
            print("Please run: pip install windows-curses")
            print("="*50)
            sys.exit(1)
            
    elif sys.platform == "darwin" or sys.platform.startswith("linux"):
        pass
    
    # Run it hehe
    main()


