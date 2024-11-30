import os
import sys
import platform

def add_to_path(directory):
    # Get the current user's PATH
    user_path = os.environ.get('PATH', '')

    # Ensure the directory is not already in the PATH
    if directory not in user_path:
        # Add the directory to the current user's PATH
        if platform.system() == 'Windows':
            # On Windows, use the User environment variable for PATH
            import winreg
            try:
                # Open the key for the user's environment variables
                reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE)
                # Append the directory to the PATH
                winreg.SetValueEx(reg_key, "PATH", 0, winreg.REG_EXPAND_SZ, user_path + ";" + directory)
                winreg.CloseKey(reg_key)
                print(f"Added {directory} to PATH successfully.")
            except Exception as e:
                print(f"Failed to add to PATH on Windows: {e}")
        else:
            # For macOS and Linux, update the user's environment
            try:
                user_shell_config = os.path.expanduser("~/.bashrc" if platform.system() != 'Darwin' else "~/.zshrc")
                with open(user_shell_config, 'a') as f:
                    f.write(f'\nexport PATH="{directory}:$PATH"\n')
                print(f"Added {directory} to PATH successfully.")
            except Exception as e:
                print(f"Failed to add to PATH on macOS/Linux: {e}")
    else:
        print(f"{directory} is already in the PATH.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_to_path.py <directory_path>")
    else:
        add_to_path(sys.argv[1])

