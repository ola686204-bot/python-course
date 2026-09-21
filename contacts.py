"""Contact creation and CRUD operations."""

from validator import (
    validate_city,
    validate_email,
    validate_name,
    validate_phone,
)


def create_contact(contact_id, name, phone, email, city):
    """Create and return a new contact dictionary.

    Args:
        contact_id (int): Unique ID for the contact.
        name (str): Contact name.
        phone (str): Contact phone number.
        email (str): Contact email address.
        city (str): Contact city.

    Returns:
        dict: A dictionary containing the contact information.
    """
    return {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city,
    }


def add_contact(contacts, name, phone, email, city):
    """Validate and add a new contact.

    Args:
        contacts (list): List of existing contacts.
        name (str): Contact name.
        phone (str): Contact phone number.
        email (str): Contact email address.
        city (str): Contact city.

    Returns:
        bool: True if the contact was added, otherwise False.
    """
    if not validate_name(name):
        return False

    if not validate_phone(phone):
        return False

    if not validate_email(email):
        return False

    if not validate_city(city):
        return False

    contact_id = max(
        (contact["id"] for contact in contacts),
        default=0,
    ) + 1

    contact = create_contact(
        contact_id,
        name,
        phone,
        email,
        city,
    )

    contacts.append(contact)
    return True


def find_contact_by_name(contacts, name):
    """Find a contact by name without considering letter case.

    Args:
        contacts (list): List of contacts.
        name (str): Name to search for.

    Returns:
        dict or None: Matching contact or None if not found.
    """
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact

    return None


def update_contact(contacts, contact_id, field, new_value):
    """Validate and update an existing contact field.

    Args:
        contacts (list): List of contacts.
        contact_id (int): ID of the contact to update.
        field (str): Field to update.
        new_value (str): New value for the field.

    Returns:
        bool: True if updated successfully, otherwise False.
    """
    validators = {
        "name": validate_name,
        "phone": validate_phone,
        "email": validate_email,
        "city": validate_city,
    }

    if field not in validators:
        return False

    if not validators[field](new_value):
        return False

    for contact in contacts:
        if contact["id"] == contact_id:
            contact[field] = new_value
            return True

    return False


def delete_contact(contacts, contact_id):
    """Delete a contact using its ID.

    Args:
        contacts (list): List of contacts.
        contact_id (int): ID of the contact to delete.

    Returns:
        dict or None: Deleted contact or None if not found.
    """
    for index, contact in enumerate(contacts):
        if contact["id"] == contact_id:
            return contacts.pop(index)

    return None


def search_contacts(contacts, keyword):
    """Search all contact fields for a keyword.

    Args:
        contacts (list): List of contacts.
        keyword (str): Search keyword.

    Returns:
        list: Contacts matching the keyword.
    """
    keyword = keyword.lower()
    matches = []

    for contact in contacts:
        for value in contact.values():
            if keyword in str(value).lower():
                matches.append(contact)
                break

    return matches


if __name__ == "__main__":
    pass
