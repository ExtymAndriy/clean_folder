import os
import argparse

def clean_folder(directory):
    # Реалізація функції очищення папки тут
    pass

def main():
    parser = argparse.ArgumentParser(description='Clean a folder.')
    parser.add_argument('directory', help='Path to the folder to clean')
    args = parser.parse_args()
    
    clean_folder(args.directory)

if __name__ == '__main__':
    main()
      