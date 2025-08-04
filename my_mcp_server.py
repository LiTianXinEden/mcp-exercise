from mcp.server.fastmcp import FastMCP
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
from pathlib import Path
from datetime import datetime
import requests
import os

server = FastMCP("my-python-server")

@server.tool()
def say_hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}! Welcome to MCP."

@server.tool()
def list_directory(directory_path: str) -> list:
    """List the contents of a directory"""
    try:
        files = os.listdir(directory_path)
        return files
    except FileNotFoundError:
        return "Directory not found"
    except PermissionError:
        return "Permission denied"

@server.tool()
def list_details(directory_path: str) -> list:
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

@server.tool()
def get_weather(location: str) -> str:
    """
    Fetches the current weather for a given city or country using wttr.in.
    Args:
        location (str): The name of the city or country (e.g., 'Paris',
        'Singapore').
    Returns:
        str: A plain-text summary of the current weather, or an error message.
    """
    try:
        url = f"https://wttr.in/{location}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return (
                f"Error: Unable to fetch weather data "
                f"(status code {response.status_code})"
            )
    except Exception as e:
        return f"Error: {e}"

# Example usage:
# if __name__ == "__main__":
#     location = input("Enter a city or country: ")
#     print(get_weather(location))


if __name__ == "__main__":
    print("Starting MCP server...")
    server.run(transport="stdio")