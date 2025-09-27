import os
import shutil

def organize_folder(folder_path):
    """
    Organizes files in a given folder into subdirectories based on file extension.
    
    :param folder_path: The absolute path of the folder to organize.
    """
    
    # --- Mapping of file extensions to folder names ---
    FILE_TYPES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Scripts": [".py", ".js", ".html", ".css", ".sh"]
    }

    # --- Check if the provided path is a valid directory ---
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        return

    print(f"Organizing files in: {folder_path}\n")

    # --- Iterate over all files in the directory ---
    for filename in os.listdir(folder_path):
        # Construct the full path of the file
        file_path = os.path.join(folder_path, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
            
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        
        # --- Find the target folder for this file type ---
        moved = False
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                # Create the target directory if it doesn't exist
                target_folder_path = os.path.join(folder_path, folder_name)
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path)
                    print(f"Created folder: {target_folder_path}")
                
                # Move the file
                shutil.move(file_path, os.path.join(target_folder_path, filename))
                print(f"Moved '{filename}' to '{folder_name}' folder.")
                moved = True
                break
        
        # --- Handle files with unlisted extensions ---
        if not moved:
            other_folder = os.path.join(folder_path, "Other")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
                print(f"Created folder: {other_folder}")
            
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"Moved '{filename}' to 'Other' folder.")

    print("\n✅ Organization complete!")


# --- Main execution block ---
if __name__ == "__main__":
    # Get folder path from user input
    path_to_organize = input("Enter the full path of the folder you want to organize: ")
    organize_folder(path_to_organize)
