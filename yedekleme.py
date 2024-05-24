import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    for filename in os.listdir(source_dir):
        full_file_name = os.path.join(source_dir, filename)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, backup_dir)
            print(f"{filename} yedeklendi.")

source_directory = "kaynak_klasoru"
backup_directory = f"yedek_klasoru_{datetime.now().strftime('%Y%m%d%H%M%S')}"

backup_files(source_directory, backup_directory)
