"""Entry point for the CLI utility toolkit."""

import os

from analyzer import run_analyzer
from contacts import run_contact_manager
from display import display_message, get_input, print_main_menu
from file_handler import ensure_directory
from logger import clear_logs, log_operation, view_logs


DATA_DIRECTORY = "data"
CONTACT_FILE = "contacts.csv"
REPORT_FILE = "analysis_report.txt"
LOG_FILE = "operations.log"
EXPORT_FILE = "contacts_export.csv"


def get_paths():
    """Build all application file paths.

    Returns:
        tuple: Contact, report, log, and export paths.
    """
    ensure_directory(DATA_DIRECTORY)
    base = DATA_DIRECTORY
    return (
        os.path.join(base, CONTACT_FILE),
        os.path.join(base, REPORT_FILE),
        os.path.join(base, LOG_FILE),
        os.path.join(base, EXPORT_FILE),
    )


def run_logger(log_path):
    """Run the operation logger menu."""
    while True:
        print("\n1. View log")
        print("2. Clear log")
        print("3. Return")
        choice = get_input("Choose an option: ")
        if choice == "1":
            display_message(view_logs(log_path))
        elif choice == "2":
            clear_logs(log_path)
            log_operation("Operation log cleared", log_path)
            display_message("Log cleared.")
        elif choice == "3":
            return
        else:
            display_message("Invalid choice.")


def main():
    """Start the CLI utility toolkit."""
    contact_path, report_path, log_path, export_path = get_paths()
    log_operation("Application started", log_path)
    while True:
        print_main_menu()
        choice = get_input("Choose an option: ")
        if choice == "1":
            run_contact_manager(contact_path, export_path, log_path)
        elif choice == "2":
            run_analyzer(report_path, log_path)
        elif choice == "3":
            run_logger(log_path)
        elif choice == "4":
            log_operation("Application exited", log_path)
            display_message("Goodbye!")
            return
        else:
            display_message("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
