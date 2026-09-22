"""Input validation functions for the CLI utility toolkit."""

import os
import re


MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 50
PHONE_LENGTH = 11
EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
MIN_MENU_OPTION = 1
MAX_MENU_OPTION = 4


def validate_name(name):
    """Validate a contact name.

    Args:
        name (str): Name to validate.

    Returns:
        tuple: Validation status and message.
    """
    name = name.strip()
    if not name:
        return False, "Name cannot be empty."
    if not name.replace(" ", "").isalpha():
        return False, "Name must contain only letters and spaces."
    if not MIN_NAME_LENGTH <= len(name) <= MAX_NAME_LENGTH:
        return False, "Name length is invalid."
    return True, name


def validate_phone(phone):
    """Validate a Nigerian phone number.

    Args:
        phone (str): Phone number to validate.

    Returns:
        tuple: Validation status and message.
    """
    phone = phone.strip()
    if not phone.isdigit():
        return False, "Phone must contain only numbers."
    if len(phone) != PHONE_LENGTH:
        return False, "Phone must contain 11 digits."
    return True, phone


def validate_email(email):
    """Validate an email address.

    Args:
        email (str): Email address to validate.

    Returns:
        tuple: Validation status and message.
    """
    email = email.strip()
    if not re.match(EMAIL_PATTERN, email):
        return False, "Please enter a valid email address."
    return True, email


def validate_menu_choice(choice):
    """Validate a main menu choice.

    Args:
        choice (str): Menu choice entered by the user.

    Returns:
        tuple: Validation status and converted choice.
    """
    try:
        number = int(choice)
    except ValueError:
        return False, "Choice must be a number."
    if not MIN_MENU_OPTION <= number <= MAX_MENU_OPTION:
        return False, "Choice is outside the menu range."
    return True, number


def validate_contact_id(contact_id):
    """Validate a contact ID.

    Args:
        contact_id (str): Contact ID to validate.

    Returns:
        tuple: Validation status and cleaned ID.
    """
    contact_id = contact_id.strip()
    if not contact_id:
        return False, "Contact ID cannot be empty."
    if not contact_id.isdigit():
        return False, "Contact ID must contain only numbers."
    return True, contact_id


def validate_file_path(file_path):
    """Validate an existing file path.

    Args:
        file_path (str): Path to validate.

    Returns:
        tuple: Validation status and cleaned path.
    """
    file_path = file_path.strip()
    if not file_path:
        return False, "File path cannot be empty."
    if not os.path.exists(file_path):
        return False, "File does not exist."
    if not os.path.isfile(file_path):
        return False, "Path must point to a file."
    return True, file_path

