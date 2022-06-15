#!/usr/bin/env python3

import os
import random


def get_directory(file_path, counter):
    directory_counter = 0
    for item in os.listdir(file_path):
        if os.path.isdir(f'{file_path}{item}'):
            directory_counter += 1
    random_directory = random.randint(0, directory_counter)
    print(f"Disting {counter}:")
    print(f"\tDirectory: {random_directory}")
    return random_directory

def get_file(file_path, random_directory):
    file_counter = 0
    for item in os.listdir(f'{file_path}{random_directory}'):
        file_counter += 1
    random_file = random.randint(0, file_counter)
    print(f"\t\tFile: {random_file}")
    return


def main():
    file_path = '/Volumes/Music/Sound Library (Sync\'d)/Disting Samples/'
    disting_count = 2
    counter = 0
    while counter < disting_count:
        random_directory = get_directory(file_path, counter)
        get_file(file_path, random_directory)
        counter += 1
    exit()


if __name__ == '__main__':
    main()
