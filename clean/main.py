import os
import argparse

def clean_folder(folder_path):
    # Реалізуйте функціональність очищення папки тут
    print(f'Cleaning folder at: {folder_path}')
    pass

def main():
    parser = argparse.ArgumentParser(description='Clean a folder.')
    parser.add_argument('folder', metavar='FOLDER', type=str, help='Path to the folder to clean')
    args = parser.parse_args()
    clean_folder(args.folder)

if __name__ == "__main__":
    main()
