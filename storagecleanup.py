import os
import sys
import shutil
from datetime import datetime, timedelta

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def get_files_sorted_by_age(folder_path):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append((file_path, os.path.getmtime(file_path)))
    return sorted(files, key=lambda x: x[1])

def cleanup_folder(mount_path):
    if not os.path.exists(mount_path):
        print(f"Error: The specified path '{mount_path}' does not exist.")
        return

    total, used, free = shutil.disk_usage(mount_path)
    free_percentage = (free / total) * 100

    print(f"Total space: {total / (1024**3):.2f} GB")
    print(f"Used space: {used / (1024**3):.2f} GB")
    print(f"Free space: {free / (1024**3):.2f} GB")
    print(f"Free space percentage: {free_percentage:.2f}%")

    # Check if free space is less than 20%
    if free_percentage < 20:
        space_to_free = total * 0.1  # 10% of total space
        files_to_remove = get_files_sorted_by_age(mount_path)
        space_freed = 0

        print("Freeing up space by removing oldest files...")
        for file_path, _ in files_to_remove:
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                os.remove(file_path)
                space_freed += file_size
                print(f"Removed: {file_path}")

                if space_freed >= space_to_free:
                    break

        print(f"Freed up {space_freed / (1024**3):.2f} GB of space")

    # Remove files older than 7 days
    seven_days_ago = datetime.now() - timedelta(days=7)
    print("Removing files older than 7 days...")
    for dirpath, dirnames, filenames in os.walk(mount_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.getmtime(file_path) < seven_days_ago.timestamp():
                os.remove(file_path)
                print(f"Removed: {file_path}")

    print("Cleanup completed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <mount_folder_path>")
        sys.exit(1)

    mount_folder = sys.argv[1]
    cleanup_folder(mount_folder)
