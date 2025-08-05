import os 
from pathlib import Path

JUNK_PATHS = [
    str(Path.home() / "Downloads"),
    str(Path.home() / ".cache")
]

def find_junk(min_size_bytes=10**6):
    junk = []
    for path in JUNK_PATHS:
        if os.path.exists(path):
            for root, _, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    try:
                        if os.path.getsize(full_path) > min_size_bytes:
                            junk.append(full_path)
                    except Exception:
                        continue
    return junk 
                