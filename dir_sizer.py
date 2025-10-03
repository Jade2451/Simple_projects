import os

def get_human_readable_size(size_in_bytes):
    """Converts a size in bytes to a human-readable format (KB, MB, GB)."""
    if size_in_bytes is None:
        return "0 B"
    power = 1024
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size_in_bytes >= power and n < len(power_labels):
        size_in_bytes /= power
        n += 1
    return f"{size_in_bytes:.2f} {power_labels[n]}B"

def check_directory_size():
    """
    Calculates the total size of a directory by walking through its contents.
    """
    print("💾 Directory Size Checker 💾")
    
    # --- Get User Input ---
    path = input("Enter the full path to the directory: ")

    if not os.path.isdir(path):
        print(f"❌ Error: The path '{path}' is not a valid directory.")
        return

    total_size = 0
    
    print("\nScanning... This may take a moment for large directories.")
    
    try:
        # --- Walk the Directory Tree ---
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                # Get the full path to the file
                fp = os.path.join(dirpath, f)
                # Add the file's size to the total, skipping if it's a broken link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        # --- Display the Result ---
        readable_size = get_human_readable_size(total_size)
        print("\n" + "="*35)
        print(f"  Total Directory Size: {readable_size}")
        print(f"  Path: {path}")
        print("="*35 + "\n")

    except Exception as e:
        print(f"❌ An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    check_directory_size()
