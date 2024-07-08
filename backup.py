import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    for root, _, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source_dir)
            dest_file = os.path.join(dest_dir, relative_path)

            dest_file_dir = os.path.dirname(dest_file)
            if not os.path.exists(dest_file_dir):
                os.makedirs(dest_file_dir)

            if os.path.exists(dest_file):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                dest_file = f"{dest_file}_{timestamp}"

            try:
                shutil.copy2(source_file, dest_file)
                print(f"Copied '{source_file}' to '{dest_file}'")
            except Exception as e:
                print(f"Error copying '{source_file}' to '{dest_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:- python backup.py /Full Path_of_Source_Dir /Full Path_of_Destination Dir \n(Tip pwd command to check path (backup.py is Python script name ))")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
