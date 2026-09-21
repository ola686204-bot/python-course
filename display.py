
"""Output formatting and contact display functions."""


def display_all_contacts(contacts):
    """Display all contacts in a formatted table.

    Args:
        contacts (list): List of contact dictionaries.

    Returns:
        None: This function only displays information.
    """
    if not contacts:
        print("Contact list is empty.")
        return

    print("\n=== All Contacts ===")
    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Phone':<18}"
        f"{'Email':<30}"
        f"{'City':<15}"
    )
    print("-" * 88)

    for contact in contacts:
        print(
            f"{contact['id']:<5}"
            f"{contact['name']:<20}"
            f"{contact['phone']:<18}"
            f"{contact['email']:<30}"
            f"{contact['city']:<15}"
        )


def display_contact(contact):
    """Display one contact's information.

    Args:
        contact (dict): Contact dictionary to display.

    Returns:
        None: This function only displays information.
    """
    if contact is None:
        print("Contact not found.")
        return

    print(
        f"Name: {contact['name']} | "
        f"Phone: {contact['phone']} | "
        f"Email: {contact['email']} | "
        f"City: {contact['city']}"
    )


def display_summary(contacts):
    """Display a summary of the contact collection.

    Args:
        contacts (list): List of contact dictionaries.

    Returns:
        None: This function only displays information.
    """
    total = len(contacts)

    cities = set()
    for contact in contacts:
        cities.add(contact["city"].lower())

    print("\n=== Contact Summary ===")
    print(f"Total contacts: {total}")
    print(f"Different cities: {len(cities)}")


if __name__ == "__main__":
    pass
