""" Contact manager with CSV file persistence."""

from datetime import datetime

CONTACTS_FILE = "contacts.txt"

def parse_contact_line(line):
    """Parse one CSV line into a contact dictinary.
    Args:
        line: A raw CSV line containing five comma-separated fields.
    Returns: 
        A contact dictionary if the line is valid, otherwise None.
    """
    fields = line.strip().split(",")

    if len(fields) != 5:
        print(f"Warning: Skipping malformed line: {line.strip()}")
        return None

    contact_id, name, phone, email, city = fields

    if not contact_id or not name or not phone or not email or not city:
        print(f"Warning: Skipping malformed line: {line.strip()}")
        return None

    return{
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }

def save_contacts(contacts, filename):
    """Save all contacts to a CSV file.

    Args:
        contacts: A list of contact dictionaries.
        filename: The file where contacts will be saved.

    Returns:
        True if saving succeeds, otherwise False.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for contact in contacts:
                line = (
                    f"{contact['id']},"
                    f"{contact['name']},"
                    f"{contact['phone']},"
                    f"{contact['email']},"
                    f"{contact['city']}\n"
                )
                file.write(line)

        return True

    except OSError as error:
        print(f"Error: Could not save contacts to {filename}: {error}")
        return False


def load_contacts(filename):
    """Load contacts from a CSV file.

    Args:
        filename: The file containing saved contacts.

    Returns:
        A list of contact dictionaries.
    """
    contacts = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                contact = parse_contact_line(line)

                if contact is not None:
                    contacts.append(contact)

    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty list.")

    except OSError as error:
        print(f"Error: Could not read contacts file: {error}")

    except ValueError as error:
        print(f"Warning: Invalid contact data: {error}")

    return contacts


def backup_contacts(contacts, filename):
    """Create a timestamped backup of all contacts.

    Args:
        contacts: A list of contact dictionaries.
        filename: The original contacts filename.

    Returns:
        True if the backup succeeds, otherwise False.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_filename = f"contacts_backup_{timestamp}.txt"

    print(f"Creating backup: {backup_filename}")

    return save_contacts(contacts, backup_filename)


def display_contacts(contacts):
    """Display all contacts.

    Args:
        contacts: A list of contact dictionaries.

    Returns:
        None.
    """
    if not contacts:
        print("No contacts available.")
        return

    for contact in contacts:
        print(
            f"{contact['id']} | "
            f"{contact['name']} | "
            f"{contact['phone']} | "
            f"{contact['email']} | "
            f"{contact['city']}"
        )


def add_contact(contacts):
    """Add a new contact and save the updated list.

    Args:
        contacts: The list of contact dictionaries.

    Returns:
        None.
    """
    contact_id = input("Enter contact ID: ")
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    city = input("Enter city: ")

    contact = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }

    contacts.append(contact)

    if save_contacts(contacts, CONTACTS_FILE):
        print("Contact added and saved successfully.")


def update_contact(contacts):
    """Update an existing contact and save the updated list.

    Args:
        contacts: The list of contact dictionaries.

    Returns:
        None.
    """
    contact_id = input("Enter the ID of the contact to update: ")

    for contact in contacts:
        if contact["id"] == contact_id:
            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")
            contact["city"] = input("Enter new city: ")

            if save_contacts(contacts, CONTACTS_FILE):
                print("Contact updated and saved successfully.")

            return

    print("Contact not found.")


def delete_contact(contacts):
    """Delete a contact and save the updated list.

    Args:
        contacts: The list of contact dictionaries.

    Returns:
        None.
    """
    contact_id = input("Enter the ID of the contact to delete: ")

    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)

            if save_contacts(contacts, CONTACTS_FILE):
                print("Contact deleted and saved successfully.")

            return

    print("Contact not found.")


def run_contact_manager():
    """Run the contact management program."""
    contacts = load_contacts(CONTACTS_FILE)

    print(f"{len(contacts)} contact(s) loaded.")

    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Display contacts")
        print("2. Add contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Backup contacts")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_contacts(contacts)

        elif choice == "2":
            add_contact(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            backup_contacts(contacts, CONTACTS_FILE)

        elif choice == "6":
            if save_contacts(contacts, CONTACTS_FILE):
                print("All contacts saved. Goodbye!")
            else:
                print("Warning: Contacts could not be saved.")

            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    run_contact_manager()
