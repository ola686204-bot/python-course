"""Contact management functions for the CLI utility toolkit."""

import os

from display import (
    display_contacts,
    display_message,
    get_input,
    print_contact_menu,
)
from file_handler import load_csv, save_csv
from logger import log_operation
from validator import (
    validate_contact_id,
    validate_email,
    validate_name,
    validate_phone,
)


CONTACT_FIELDS = ["id", "name", "phone", "email"]
EMPTY_CONTACTS = 0
FIRST_ID = 1


def load_contacts(file_path):
    """Load contacts from a CSV file.

    Args:
        file_path (str): Contact CSV path.

    Returns:
        list: Contact records.
    """
    return load_csv(file_path)


def save_contacts(contacts, file_path):
    """Save contacts to a CSV file.

    Args:
        contacts (list): Contact records.
        file_path (str): Destination path.

    Returns:
        bool: True when saving succeeds.
    """
    return save_csv(file_path, contacts, CONTACT_FIELDS)


def get_next_id(contacts):
    """Generate the next contact ID.

    Args:
        contacts (list): Existing contacts.

    Returns:
        str: New contact ID.
    """
    if not contacts:
        return str(FIRST_ID)
    numbers = [int(contact["id"]) for contact in contacts]
    return str(max(numbers) + FIRST_ID)


def add_contact(contacts, name, phone, email):
    """Add a validated contact to a contact list.

    Args:
        contacts (list): Contact collection.
        name (str): Contact name.
        phone (str): Contact phone.
        email (str): Contact email.

    Returns:
        tuple: Success status and contact record.
    """
    checks = [validate_name(name), validate_phone(phone), validate_email(email)]
    if not all(check[0] for check in checks):
        return False, "Invalid contact information."
    contact = {
        "id": get_next_id(contacts),
        "name": checks[0][1],
        "phone": checks[1][1],
        "email": checks[2][1],
    }
    contacts.append(contact)
    return True, contact


def search_contacts(contacts, query):
    """Search contacts by name, phone, or email.

    Args:
        contacts (list): Contact collection.
        query (str): Search text.

    Returns:
        list: Matching contacts.
    """
    query = query.lower().strip()
    return [
        contact for contact in contacts
        if query in contact["name"].lower()
        or query in contact["phone"]
        or query in contact["email"].lower()
    ]


def update_contact(contacts, contact_id, name, phone, email):
    """Update an existing contact.

    Args:
        contacts (list): Contact collection.
        contact_id (str): Contact identifier.
        name (str): New name.
        phone (str): New phone.
        email (str): New email.

    Returns:
        tuple: Success status and result.
    """
    valid, contact_id = validate_contact_id(contact_id)
    if not valid:
        return False, contact_id
    for contact in contacts:
        if contact["id"] == contact_id:
            return update_existing(contact, name, phone, email)
    return False, "Contact not found."


def update_existing(contact, name, phone, email):
    """Validate and update contact fields.

    Args:
        contact (dict): Contact to update.
        name (str): New name.
        phone (str): New phone.
        email (str): New email.

    Returns:
        tuple: Success status and updated contact.
    """
    checks = [validate_name(name), validate_phone(phone), validate_email(email)]
    if not all(check[0] for check in checks):
        return False, "Invalid contact information."
    contact.update({
        "name": checks[0][1],
        "phone": checks[1][1],
        "email": checks[2][1],
    })
    return True, contact


def delete_contact(contacts, contact_id):
    """Delete a contact from the list.

    Args:
        contacts (list): Contact collection.
        contact_id (str): Contact identifier.

    Returns:
        tuple: Success status and deleted contact.
    """
    valid, contact_id = validate_contact_id(contact_id)
    if not valid:
        return False, contact_id
    for index, contact in enumerate(contacts):
        if contact["id"] == contact_id:
            return True, contacts.pop(index)
    return False, "Contact not found."


def export_contacts(contacts, file_path):
    """Export contacts to a CSV file.

    Args:
        contacts (list): Contact records.
        file_path (str): Export destination.

    Returns:
        bool: True when export succeeds.
    """
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    return save_contacts(contacts, file_path)


def handle_add(contacts, file_path, log_path):
    """Handle interactive contact creation."""
    name = get_input("Name: ")
    phone = get_input("Phone: ")
    email = get_input("Email: ")
    success, result = add_contact(contacts, name, phone, email)
    if success and save_contacts(contacts, file_path):
        log_operation("Contact added", log_path)
        display_message("Contact added successfully.")
    else:
        display_message(result if isinstance(result, str) else "Could not add contact.")


def handle_view(contacts):
    """Display all saved contacts."""
    display_contacts(contacts)


def handle_search(contacts, log_path):
    """Handle interactive contact searching."""
    query = get_input("Search: ")
    results = search_contacts(contacts, query)
    display_contacts(results)
    log_operation("Contacts searched", log_path)


def handle_update(contacts, file_path, log_path):
    """Handle interactive contact updates."""
    contact_id = get_input("Contact ID: ")
    name = get_input("New name: ")
    phone = get_input("New phone: ")
    email = get_input("New email: ")
    success, result = update_contact(contacts, contact_id, name, phone, email)
    if success and save_contacts(contacts, file_path):
        log_operation("Contact updated", log_path)
        display_message("Contact updated successfully.")
    else:
        display_message(result)


def handle_delete(contacts, file_path, log_path):
    """Handle interactive contact deletion."""
    contact_id = get_input("Contact ID: ")
    success, result = delete_contact(contacts, contact_id)
    if success and save_contacts(contacts, file_path):
        log_operation("Contact deleted", log_path)
        display_message("Contact deleted successfully.")
    else:
        display_message(result)


def handle_export(contacts, export_path, log_path):
    """Handle contact export."""
    if export_contacts(contacts, export_path):
        log_operation("Contacts exported", log_path)
        display_message("Contacts exported successfully.")
    else:
        display_message("Could not export contacts.")


def run_contact_manager(file_path, export_path, log_path):
    """Run the interactive contact manager."""
    contacts = load_contacts(file_path)
    while True:
        print_contact_menu()
        choice = get_input("Choose an option: ")
        if choice == "1":
            handle_add(contacts, file_path, log_path)
        elif choice == "2":
            handle_view(contacts)
        elif choice == "3":
            handle_search(contacts, log_path)
        elif choice == "4":
            handle_update(contacts, file_path, log_path)
        elif choice == "5":
            handle_delete(contacts, file_path, log_path)
        elif choice == "6":
            handle_export(contacts, export_path, log_path)
        elif choice == "7":
            break
        else:
            display_message("Invalid choice. Please try again.")
