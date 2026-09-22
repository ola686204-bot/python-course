"""Formatted display functions for the CLI utility toolkit."""

SEPARATOR_LENGTH = 50
TABLE_WIDTH = 72
TITLE_SYMBOL = "="
COLUMN_GAP = " | "


def print_separator():
    """Print a visual separator."""
    print(TITLE_SYMBOL * SEPARATOR_LENGTH)


def print_title(title):
    """Display a formatted section title.

    Args:
        title (str): Title to display.
    """
    print_separator()
    print(title.center(SEPARATOR_LENGTH))
    print_separator()


def print_main_menu():
    """Display the main application menu."""
    print_title("CLI UTILITY TOOLKIT")
    print("1. Contact Manager")
    print("2. Word Frequency Analyzer")
    print("3. Operation Logger")
    print("4. Exit")
    print_separator()


def print_contact_menu():
    """Display the contact manager menu."""
    print_title("CONTACT MANAGER")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Export contacts")
    print("7. Return to main menu")


def print_analyzer_menu():
    """Display the word analyzer menu."""
    print_title("WORD FREQUENCY ANALYZER")
    print("1. Enter text")
    print("2. Analyze a file")
    print("3. Return to main menu")


def print_logger_menu():
    """Display the operation logger menu."""
    print_title("OPERATION LOGGER")
    print("1. View log")
    print("2. Clear log")
    print("3. Return to main menu")


def display_contacts(contacts):
    """Display contacts in a formatted table.

    Args:
        contacts (list): Contact records to display.
    """
    if not contacts:
        print("No contacts found.")
        return
    print("-" * TABLE_WIDTH)
    print("ID" + COLUMN_GAP + "NAME" + COLUMN_GAP + "PHONE" + COLUMN_GAP + "EMAIL")
    print("-" * TABLE_WIDTH)
    for contact in contacts:
        print(
            contact["id"],
            COLUMN_GAP,
            contact["name"],
            COLUMN_GAP,
            contact["phone"],
            COLUMN_GAP,
            contact["email"],
        )
    print("-" * TABLE_WIDTH)


def display_frequency(words):
    """Display word frequencies.

    Args:
        words (list): Word and count pairs.
    """
    if not words:
        print("No words found.")
        return
    print_title("TOP WORDS")
    for position, item in enumerate(words, start=1):
        print(f"{position}. {item[0]} - {item[1]}")


def display_message(message):
    """Display a normal application message.

    Args:
        message (str): Message to display.
    """
    print(message)


def get_input(prompt):
    """Safely collect user input.

    Args:
        prompt (str): Input prompt.

    Returns:
        str: User input or an empty string.
    """
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return ""
