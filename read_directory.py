import os
from pathlib import Path

# Directory to read (current folder by default)
directory = Path(".")

print("Files and folders in:", directory.resolve())
print("-" * 40)

# Method 1: pathlib (recommended)
for item in directory.iterdir():
    kind = "folder" if item.is_dir() else "file"
    print(f"{kind:6}  {item.name}")

print("-" * 40)

# Method 2: os.listdir
for name in os.listdir(directory):
    full_path = directory / name
    if os.path.isdir(full_path):
        print(f"[DIR]  {name}")
    else:
        print(f"[FILE] {name}")
