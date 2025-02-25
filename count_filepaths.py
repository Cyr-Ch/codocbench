import json
from collections import Counter
import os

def extract_root_folders():
    """
    Extract and count root folders from docstrings.jsonl file
    """
    # Store root folders
    root_folders = []
    
    # Read the file line by line
    input_file = 'docstrings.jsonl'
    if not os.path.exists(input_file):
        print(f"File {input_file} not found. Please run parse_main.py first.")
        return
    
    with open(input_file, 'r') as f:
        for line in f:
            try:
                # Parse JSON from each line
                data = json.loads(line)
                if 'file_path' in data:
                    # Get the root folder (first part of the path)
                    parts = data['file_path'].split('/')
                    if parts:
                        root = parts[0]
                        root_folders.append(root)
            except json.JSONDecodeError:
                continue

    # Count occurrences using Counter
    folder_counts = Counter(root_folders)
    
    # Write results to output file
    with open('root_folder_counts.txt', 'w') as f:
        f.write(f"Total unique root folders: {len(folder_counts)}\n")
        f.write(f"Total function/class entries: {len(root_folders)}\n\n")
        for folder, count in folder_counts.most_common():
            f.write(f"{folder}: {count}\n")
    
    print(f"Results written to root_folder_counts.txt")
    print(f"Top 5 root folders:")
    for folder, count in list(folder_counts.most_common(5)):
        print(f"  {folder}: {count}")

if __name__ == "__main__":
    extract_root_folders() 
