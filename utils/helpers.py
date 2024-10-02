import os

def ensure_directory_exists(directory):
    """
    Ensures that a given directory exists, creating it if it does not.

    :param directory: The directory path to check or create.
    :return: None
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def format_size(bytes, suffix="B"):
    """
    Converts a file size in bytes into a more human-readable format.

    :param bytes: The size in bytes.
    :param suffix: The unit suffix (e.g., "B" for bytes).
    :return: The formatted string of the size.
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(bytes) < 1024.0:
            return f"{bytes:3.1f}{unit}{suffix}"
        bytes /= 1024.0
    return f"{bytes:.1f}Y{suffix}"
