import os 
import hashlib
from pathlib import Path

def hash_file(path):
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception:
        return None
    
def find_duplicates(directories=None):
    if directories is None:
        directories = [
            str(Path.home() / "Downloads"),
            str(Path.home() / "Documents"),
            str(Path.home() / "Desktop"),
        ]

    seen = {}
    duplicates = []

    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                file_hash = hash_file(full_path)
                if not file_hash:
                    continue
                if file_hash in seen:
                    duplicates.append(full_path)
                else:
                    seen[file_hash] = full_path
    return duplicates
                
    
    