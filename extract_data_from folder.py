import os

def get_all_files(folder_path):
    file_names = []
    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Append file name to the list
            file_names.append(file)
    return file_names

# Example usage
folder_path = r'folder/path'  # Replace this with your folder path
files = get_all_files(folder_path)
print(files)