import os
from pathlib import Path

def delete_malicious_file(file_path):
    try:
        path = Path(file_path)
        if path.is_file():
            os.remove(file_path)
            print(f"Successfully deleted malicious file: {file_path}")
        else:
            print(f"No file found at: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")
