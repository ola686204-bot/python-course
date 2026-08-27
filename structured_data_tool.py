"""Contact management tool using a list of dictionaries."""

def create_contact(contact_id, name, phone, email, city):
    """Create and return a new contact dictionary."""
    return {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }

def add_contact(contacts, name, phone, email, city):
    """Create a contact annd appends it to the contacts list."""
    contact_id = len(contacts) + 1  # Simple ID generation
    new_contact = create_contact(
        contact_id,
        name,
        phone,
        email, 
        city,
)
    contacts.append(new_contact)
    return new_contact

def view_all_contacts(contacts):
    """Display all contacts in a formatted table."""
    if not contacts:
        print(f"Contact list is empty.")
        return

    print(f"\n=== All Contacts ===")
    print(
        f"{'ID':<5}"
        f"{'Name': <20}"
        f"{'Phone':<18}"
        f"{'Email':<30}"
        f"{'City':<15}"
    )
    print(f"{'_' * 88}")

    for contact in contacts:
        print(
            f"{contact['id']:<5}"
            f"{contact['name']:<20}"
            f"{contact['phone']:<18}"
            f"{contact['email']:<30}"
            f"{contact['city']:<15}"
        )

def find_contact_by_name(contacts, name):
    """Find a contact by name without considering letter case."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None

def update_contact(contacts, contact_id, field, new_value):
    """Update an allowed field in a contact."""
    allowed_fields = [
        "name",
        "phone",
        "email",
        "city",
    ]

    if field not in allowed_fields:
        return False

    for contact in contacts:
        if contact["id"] == contact_id:
            contact[field] = new_value
            return True

    return False


def delete_contact(contacts, contact_id):
    """Delete a contact using its ID."""
    for index, contact in enumerate(contacts):
        if contact["id"] == contact_id:
            return contacts.pop(index)

    return None

def search_contacts(contacts, keyword):
    """Search all contact fields for a keyword."""
    keyword = keyword.lower()
    matches = []

    for contact in contacts:
        for value in contact.values():
            if keyword in str(value).lower():
                matches.append(contact)
                break

    return matches


def run_contact_manager(contacts):
    """Run the contact management menu."""
    while True:
        print(f"\n=== Contact Manager ===")
        print(f"1. Add contact")
        print(f"2. View all contacts")
        print(f"3. Find contact by name")
        print(f"4. Update contact")
        print(f"5. Delete contact")
        print(f"6. Search contacts")
        print(f"7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            city = input("Enter city: ")

            add_contact(
                contacts,
                name,
                phone,
                email,
                city,
            )

            print(f"Contact '{name}' added successfully.")

        elif choice == "2":
            view_all_contacts(contacts)

        elif choice == "3":
            name = input("Enter name to find: ")

            contact = find_contact_by_name(
                contacts,
                name,
            )

            if contact is None:
                print(f"No contact found with the name '{name}'.")
            else:
                print(
                    f"ID: {contact['id']} | "
                    f"Name: {contact['name']} | "
                    f"Phone: {contact['phone']} | "
                    f"Email: {contact['email']} | "
                    f"City: {contact['city']}"
                )

        elif choice == "4":
            try:
                contact_id = int(input("Enter contact ID: "))
                field = input(
                    "Enter field "
                    "(name, phone, email, city): "
                ).lower()
                new_value = input("Enter new value: ")

                updated = update_contact(
                    contacts,
                    contact_id,
                    field,
                    new_value,
                )

                if updated:
                    print(
                        f"Contact {contact_id} "
                        f"updated successfully."
                    )
                else:
                    print(
                        f"Error: Invalid contact ID "
                        f"or field."
                    )

            except ValueError:
                print(f"Error: Contact ID must be a number.")

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
                    print(
                        f"Deleted contact: "
                        f"{deleted['name']}"
                    )

            except ValueError:
                print(f"Error: Contact ID must be a number.")

        elif choice == "6":
            keyword = input("Enter search keyword: ")

            matches = search_contacts(
                contacts,
                keyword,
            )

            if not matches:
                print(f"No matching contacts found.")
            else:
                print(f"\n=== Search Results ===")

                for contact in matches:
                    print(
                        f"ID: {contact['id']:<5}"
                        f"Name: {contact['name']:<20}"
                        f"Phone: {contact['phone']:<18}"
                        f"Email: {contact['email']:<30}"
                        f"City: {contact['city']:<15}"
                    )

        elif choice == "7":
            print(f"Goodbye!")
            break

        else:
            print(f"Error: Invalid menu choice.")


def main():
    """Initialize the contacts list and start the program."""
    contacts = []
    run_contact_manager(contacts)


if __name__ == "__main__":
    main()
