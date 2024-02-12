import os
import shutil
import sys

def clean_folder(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                shutil.rmtree(dir_path)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: clean-folder <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    clean_folder(folder_path)

if __name__ == "__main__":
    main()