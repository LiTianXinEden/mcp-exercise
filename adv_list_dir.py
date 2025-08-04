from pathlib import Path  # Modern file handling
from datetime import datetime  # For formatting timestamps

def list_details(directory_path):
    """List the contents of a directory with details: 
       name, size, type, last modified"""
    path = Path(directory_path)
    if not path.exists():
        return "Directory not found"
    if not path.is_dir():
        return "Not a directory"
    result = []
    for item in path.iterdir():
        stat = item.stat()
        size = stat.st_size
        is_dir = item.is_dir()
        last_modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        result.append({
            'name': item.name,
            'size': size,
            'type': 'directory' if is_dir else 'file',
            'last_modified': last_modified
        })
    return result

# Example usage
if __name__ == "__main__":
    user_input = input("Enter directory path: ")
    result = list_details(user_input)
    for entry in result if isinstance(result, list) else [result]:
        print(entry)
