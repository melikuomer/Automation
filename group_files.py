import os
import shutil
import sys

def group_files_by_extension(directory):
    # Ensure the provided directory exists
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension and create a new folder based on it
        file_extension = filename.split('.')[-1] if '.' in filename else 'no_extension'
        extension_folder = os.path.join(directory, file_extension)

        # Create the folder if it doesn't exist
        if not os.path.exists(extension_folder):
            os.mkdir(extension_folder)

        # Move the file into the corresponding folder
        shutil.move(file_path, os.path.join(extension_folder, filename))

    print(f"Files in '{directory}' have been grouped by their extensions.")

if __name__ == "__main__":
    # Get the directory from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python group_files.py <directory_path>")
    else:
        group_files_by_extension(sys.argv[1])

