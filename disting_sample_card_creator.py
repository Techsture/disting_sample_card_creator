#!/usr/bin/env python3

# You'll need to `pip install soundfile`

import argparse
import math
import os
import random
import shutil
import soundfile


def check_file(dirpath, filenames):
    error_flag = False
    for filename in filenames:
        if filename == '.DS_Store':
            print(f"Deleting {filename}")
            os.remove(f'{dirpath}/.DS_Store')
            continue
        else:
            try:
                print(f"Checking {filename}...")
                wav_file_data = soundfile.SoundFile(f"{dirpath}/{filename}")
                # For troubleshooting purposes:
                #print(f"{filename}\n \
                #        Format: {wav_file_data.format} \n \
                #        Sample Rate: {wav_file_data.samplerate}\n \
                #        Channels: {wav_file_data.channels}\n \
                #        Bit Depth: {wav_file_data.subtype}\n \
                #    ")
                if wav_file_data.format != 'WAV':
                    print(f"\t[1] {filename} is not a WAV file.")
                    error_flag = True
                if wav_file_data.samplerate != 44100:
                    print(f"\t[2] {filename} does not have a samplerate of 44.1kHz.")
                    error_flag = True
                if wav_file_data.channels != 2:
                    print(f"\t[3] {filename} is not Stereo.")
                    error_flag = True
                if wav_file_data.subtype != 'PCM_16':
                    print(f"\t[4] {filename} is not 16-bit.")
                    error_flag = True
                if error_flag == False:
                    print("\tFile OK!")
                    continue
                soundfile.SoundFile.close(wav_file_data)
            except:
                print(f"\t[1] {filename} is not an audio file.")
                error_flag = True
    if error_flag == False:
        print("\nNo errors found. Continuing...\n")
        return
    else:
        print("\nErrors found!  See above output.  Exiting...")
        exit()
    return


def generate_filename():
    counter = 0
    filename_length = 8
    acceptable_characters = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    randomized_filename = ''
    while counter < filename_length:
        randomized_filename = randomized_filename + random.choice(acceptable_characters)
        counter += 1
    return randomized_filename


def make_directories(dirpath, filenames):
    counter = 0
    file_count = len(filenames)
    directory_count = math.ceil(file_count / 16)
    while counter < directory_count:
        print(f"Creating directory {dirpath}/{counter}")
        os.mkdir(f'{dirpath}/{counter}')
        counter += 1
    print("\nAll directories created.\n")
    return


def move_files(dirpath, filenames):
    file_count = len(filenames)
    directory_count = math.ceil(file_count / 16)
    random.shuffle(filenames)
    directory_counter = 0
    while directory_counter < directory_count:
        file_counter = 0
        while file_counter < 16:
            try:
                filename = filenames.pop(0)
            except:
                print("\nNo files left to move!  Exiting...\n")
                exit()
            if filename == '.DS_Store':
                continue
            else:
                print(f"Moving {filename} to directory {directory_counter}.")
                shutil.move(f'{dirpath}/{filename}', f'{dirpath}/{directory_counter}/{filename}')
                file_counter += 1
        directory_counter += 1
    return


def rename_files(dirpath, filenames):
    for filename in filenames:
        if filename == '.DS_Store':
            continue
        else:
            file_extension = os.path.splitext(filename)[1]
            randomized_filename = generate_filename()
            print(f"Renaming {filename} to {randomized_filename}{file_extension}")
            os.rename(f'{dirpath}/{filename}', f'{dirpath}/{randomized_filename}{file_extension}')
    print("\nRenaming complete!\n")
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='System path to directory containing files.')
    parser.add_argument('--skip_renaming', action='store_true', default=False, help='Add to skip renaming files.')
    args = parser.parse_args()
    directory = args.directory
    skip_renaming = args.skip_renaming
    for (dirpath, dirnames, filenames) in os.walk(directory):
        make_directories(dirpath, filenames)
        check_file(dirpath, filenames)
        if skip_renaming is False:
            rename_files(dirpath, filenames)
            # If files have been renamed, you need to get the new list of filenames.
            for (dirpath, dirnames, filenames) in os.walk(directory):
                move_files(dirpath, filenames)
        else:
            print("Skipping file renaming.\n")
            move_files(dirpath, filenames)
    exit()


if __name__ == '__main__':
    main()
