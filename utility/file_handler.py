"""File handling functions for the CLI utility toolkit."""

import csv
import os


ENCODING = "utf-8"
CSV_NEWLINE = ""
DEFAULT_ENCODING = "utf-8"


def ensure_directory(directory):
    """Create a directory if it does not exist.

    Args:
        directory (str): Directory path.

    Returns:
        bool: True when the directory is ready.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError:
        return False
    return True


def load_csv(file_path):
    """Load records from a CSV file.

    Args:
        file_path (str): CSV file path.

    Returns:
        list: Loaded CSV records.
    """
    try:
        with open(file_path, "r", encoding=ENCODING, newline=CSV_NEWLINE) as file:
            return list(csv.DictReader(file))
    except (OSError, csv.Error):
        return []


def save_csv(file_path, records, fieldnames):
    """Save records to a CSV file.

    Args:
        file_path (str): Destination CSV path.
        records (list): Records to save.
        fieldnames (list): CSV column names.

    Returns:
        bool: True when saving succeeds.
    """
    try:
        with open(file_path, "w", encoding=ENCODING, newline=CSV_NEWLINE) as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
    except (OSError, csv.Error):
        return False
    return True


def read_text(file_path):
    """Read text from a file.

    Args:
        file_path (str): Text file path.

    Returns:
        tuple: Success status and text.
    """
    try:
        with open(file_path, "r", encoding=DEFAULT_ENCODING) as file:
            return True, file.read()
    except OSError as error:
        return False, str(error)


def write_text(file_path, content):
    """Write text to a file.

    Args:
        file_path (str): Destination path.
        content (str): Content to write.

    Returns:
        bool: True when writing succeeds.
    """
    try:
        with open(file_path, "w", encoding=DEFAULT_ENCODING) as file:
            file.write(content)
    except OSError:
        return False
    return True


def append_text(file_path, content):
    """Append text to a file.

    Args:
        file_path (str): Destination path.
        content (str): Content to append.

    Returns:
        bool: True when appending succeeds.
    """
    try:
        with open(file_path, "a", encoding=DEFAULT_ENCODING) as file:
            file.write(content)
    except OSError:
        return False
    return True


def clear_file(file_path):
    """Clear all contents from a file.

    Args:
        file_path (str): File to clear.

    Returns:
        bool: True when clearing succeeds.
    """
    return write_text(file_path, "")

