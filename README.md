# Storage Cleanup Script

## Overview

This Python script is designed to manage storage space in a specified mount folder. It performs two main functions:

1. If the free space in the mount folder is less than 20%, it removes the oldest files until 10% of the total space is freed.
2. It removes all files that are older than 7 days.

## Features

- Checks available space in the specified mount folder
- Frees up space by removing oldest files if necessary
- Removes files older than 7 days
- Provides detailed output of actions taken

## Requirements

- Python 3.x
- No additional libraries required (uses only built-in Python modules)

## Usage

1. Save the script as `storage_cleanup.py`.
2. Run the script from the command line, providing the path to the mount folder as an argument:

## How It Works

1. The script first checks if the specified path exists.
2. It calculates the total, used, and free space of the mount.
3. If free space is less than 20% of total space:
- It starts removing the oldest files.
- It continues until 10% of the total space is freed or there are no more files to remove.
4. Regardless of the space check, it then removes all files older than 7 days.

## Output

The script provides detailed output, including:
- Total, used, and free space in the mount folder
- Files removed during the space-freeing process
- Files removed due to being older than 7 days

## Important Considerations

- This script permanently deletes files. Use with caution.
- It's recommended to test the script on a non-critical directory first.
- Consider backing up important data before running this script.
- The script requires appropriate permissions to read and delete files in the specified directory.

## Customization

You can modify the script to adjust:
- The free space threshold (currently set to 20%)
- The amount of space to free up (currently set to 10% of total space)
- The age threshold for file removal (currently set to 7 days)

## License



## Author

mr.vladis

## Contribution

Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

