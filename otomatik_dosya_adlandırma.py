import os

def rename_and_sort_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()
    
    for index, filename in enumerate(files):
        new_name = f"file_{index + 1}{os.path.splitext(filename)[1]}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"{filename} --> {new_name}")

directory_path = "hedef_klasor"
rename_and_sort_files(directory_path)
