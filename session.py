"""Interactive menu loop for the contact manager."""

import os

from contacts import (
    add_contact,
    delete_contact,
    find_contact_by_name,
    search_contacts,
    update_contact,
)
from display import (
    display_all_contacts,
    display_contact,
    display_summary,
)
from file_handler import (
    backup_contacts,
    load_contacts,
    save_contacts,
)


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "contacts.txt",
)


def run_session():
    """Run the persistent contact manager menu.

    Loads contacts, displays the menu, performs operations,
    and saves changes when the user exits.

    Returns:
        None: The function runs the interactive session.
    """
    contacts = load_contacts(DATA_FILE)

    while True:
        print("\n=== Persistent Contact Manager ===")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Find contact by name")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Search contacts")
        print("7. Display summary")
        print("8. Backup contacts")
        print("9. Save and exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            city = input("Enter city: ")

            if add_contact(
                contacts,
                name,
                phone,
                email,
                city,
            ):
                save_contacts(contacts, DATA_FILE)
                print(f"Contact '{name}' added successfully.")
            else:
                print("Error: Invalid contact information.")

        elif choice == "2":
            display_all_contacts(contacts)

        elif choice == "3":
            name = input("Enter name to find: ")
            contact = find_contact_by_name(contacts, name)
            display_contact(contact)

        elif choice == "4":
            try:
                contact_id = int(input("Enter contact ID: "))
                field = input(
                    "Enter field (name, phone, email, city): "
                ).lower()
                new_value = input("Enter new value: ")

                updated = update_contact(
                    contacts,
                    contact_id,
                    field,
                    new_value,
                )

                if updated:
                    save_contacts(contacts, DATA_FILE)
                    print(
                        f"Contact {contact_id} "
                        f"updated successfully."
                    )
                else:
                    print(
                        "Error: Invalid contact ID, field, "
                        "or value."
                    )

            except ValueError:
                print("Error: Contact ID must be a number.")

        elif choice == "5":
            try:
                contact_id = int(
                    input("Enter contact ID to delete: ")
                )
                deleted = delete_contact(
                    contacts,
                    contact_id,
                )

                if deleted is None:
                    print(
                        f"Error: Contact {contact_id} "
                        f"was not found."
                    )
                else:
                    save_contacts(contacts, DATA_FILE)
                    print(
                        f"Deleted contact: {deleted['name']}"
                    )

            except ValueError:
                print("Error: Contact ID must be a number.")

        elif choice == "6":
            keyword = input("Enter search keyword: ")
            matches = search_contacts(contacts, keyword)

            if not matches:
                print("No matching contacts found.")
            else:
                print("\n=== Search Results ===")
                for contact in matches:
                    display_contact(contact)

        elif choice == "7":
            display_summary(contacts)

        elif choice == "8":
            backup_path = backup_contacts(
                contacts,
                DATA_FILE,
            )

            if backup_path:
                print(f"Backup created: {backup_path}")
            else:
                print("Backup failed.")

        elif choice == "9":
            if save_contacts(contacts, DATA_FILE):
                print("Contacts saved successfully.")
            print("Goodbye!")
            break

        else:
            print("Error: Invalid menu choice.")


if __name__ == "__main__":
    pass
