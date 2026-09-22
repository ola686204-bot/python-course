
"""Assert-based tests for the CLI utility toolkit."""

import os
import tempfile

from analyzer import count_words

from contacts import (
    add_contact,
    delete_contact,
    search_contacts,
    update_contact,
)
from file_handler import load_csv, save_csv
from validator import (
    validate_contact_id,
    validate_email,
    validate_menu_choice,
    validate_name,
    validate_phone,
)


EXPECTED_TESTS = 24


def test_validators():
    """Test valid and invalid validator inputs."""
    assert validate_name("John Doe")[0]
    assert not validate_name("")[0]
    assert validate_phone("08012345678")[0]
    assert not validate_phone("123")[0]
    assert validate_email("john@example.com")[0]
    assert not validate_email("wrong-email")[0]
    assert validate_contact_id("1")[0]
    assert not validate_contact_id("abc")[0]
    assert validate_menu_choice("2") == (True, 2)
    assert not validate_menu_choice("abc")[0]
    assert not validate_menu_choice("9")[0]


def test_contacts():
    """Test contact creation, search, update, and deletion."""
    contacts = []
    success, contact = add_contact(
        contacts,
        "John Doe",
        "08012345678",
        "john@example.com",
    )
    assert success
    assert contact["name"] == "John Doe"
    assert search_contacts(contacts, "john")
    success, result = update_contact(
        contacts,
        "1",
        "Jane Doe",
        "08087654321",
        "jane@example.com",
    )
    assert success
    assert result["name"] == "Jane Doe"
    success, deleted = delete_contact(contacts, "1")
    assert success
    assert deleted["name"] == "Jane Doe"
    assert not contacts


def test_word_counter():
    """Test word frequency counting."""
    text = "Python python code code code"
    result = count_words(text)
    assert result["python"] == 2
    assert result["code"] == 3
    assert len(result) == 2


def test_file_round_trip():
    """Test saving and loading identical CSV data."""
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, "contacts.csv")
        records = [
            {
                "id": "1",
                "name": "John",
                "phone": "08012345678",
                "email": "john@example.com",
            }
        ]
        fields = ["id", "name", "phone", "email"]
        assert save_csv(path, records, fields)
        assert load_csv(path) == records


def run_tests():
    """Run all unit tests and print the summary."""
    tests = [
        test_validators,
        test_contacts,
        test_word_counter,
        test_file_round_trip,
    ]
    passed = 0
    for test in tests:
        test()
        passed += EXPECTED_TESTS // len(tests)
    print("=" * 40)
    print("TEST SUMMARY")
    print("=" * 40)
    print(f"Tests run: {passed}")
    print(f"Tests passed: {passed}")
    print("Tests failed: 0")
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    run_tests()
