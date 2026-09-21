"""File loading, saving, and backup operations."""

import os
from datetime import datetime


def load_contacts(filename):
    """Load contacts from a text file.

    Args:
        filename (str): Path to the contacts file.

    Returns:
        list: List of valid contact dictionaries.
    """
    contacts = []

    if not os.path.exists(filename):
        return contacts

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 5:
                    print(f"Warning: Skipping malformed line: {line}")
                    continue

                try:
                    contact_id = int(parts[0])
                except ValueError:
                    print(f"Warning: Invalid contact ID: {line}")
                    continue

                contacts.append(
                    {
                        "id": contact_id,
                        "name": parts[1],
                        "phone": parts[2],
                        "email": parts[3],
                        "city": parts[4],
                    }
                )

    except OSError as error:
        print(f"Error reading file: {error}")

    return contacts


def save_contacts(contacts, filename):
    """Save contacts to a text file.

    Args:
        contacts (list): List of contact dictionaries.
        filename (str): Path to the contacts file.

    Returns:
        bool: True if saving succeeds, otherwise False.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for contact in contacts:
                file.write(
                    f"{contact['id']},"
                    f"{contact['name']},"
                    f"{contact['phone']},"
                    f"{contact['email']},"
                    f"{contact['city']}\n"
                )

        return True

    except OSError as error:
        print(f"Error saving contacts: {error}")
        return False


def backup_contacts(contacts, filename):
    """Create a timestamped backup of the contacts.

    Args:
        contacts (list): List of contact dictionaries.
        filename (str): Original contacts file path.

    Returns:
        str or None: Backup path if successful, otherwise None.
    """
    directory = os.path.dirname(filename)

    if not directory:
        directory = "."

    backup_directory = os.path.join(directory, "backups")
    os.makedirs(backup_directory, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = os.path.join(
        backup_directory,
        f"contacts_backup_{timestamp}.txt",
    )

    if save_contacts(contacts, backup_filename):
        return backup_filename

    return None


if __name__ == "__main__":
    pass
