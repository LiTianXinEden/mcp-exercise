import os  # Built-in module for operating system interface

def list_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        return files
    except FileNotFoundError:
        return "Directory not found"
    except PermissionError:
        return "Permission denied"

# Example usage
if __name__ == "__main__":
    user_input = input("Enter directory path: ")
    result = list_directory(user_input)
    print(result)