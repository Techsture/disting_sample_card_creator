# Disting Sample Card Creator

This script:
- Checks the format of each file
    - WAV  
    - 44,100 kHz
    - 16-bit
    - Stereo
- Renames the files with random characters (if not bypassed with --no_renaming switch)
    - [0-9], [a-z], [A-Z]
    - Preserve the `.wav` file extension
- Figures out how many folders to create
    - No folder should have more than 8 files in it
- Creates the required number of folders
- Randomly moves the files into the folders
    - Again, no more than 8 files per folder
