"""Validation functions for contact information."""

def validate_name(name):
    """Validate a contact name.

    Args:
        name (str): Name to validate.

    Returns:
        bool: True if the name is valid, otherwise False.
    """
    return bool(name.strip()) and all(
        character.isalpha() or character.isspace()
        for character in name
    )


def validate_phone(phone):
    """Validate a contact phone number.

    Args:
        phone (str): Phone number to validate.

    Returns:
        bool: True if the phone number is valid, otherwise False.
    """
    digits = phone.replace("+", "").replace(" ", "").replace("-", "")
    return digits.isdigit() and 7 <= len(digits) <= 15


def validate_email(email):
    """Validate a contact email address.

    Args:
        email (str): Email address to validate.

    Returns:
        bool: True if the email is valid, otherwise False.
    """
    return (
        "@" in email
        and "." in email.split("@")[-1]
        and " " not in email
    )


def validate_city(city):
    """Validate a contact city.

    Args:
        city (str): City name to validate.

    Returns:
        bool: True if the city is valid, otherwise False.
    """
    return bool(city.strip()) and all(
        character.isalpha() or character.isspace()
        for character in city
    )


if __name__ == "__main__":
    pass
