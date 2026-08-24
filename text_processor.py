"""Process a sentence using string indexing and slicing."""


def get_first_character(text):
    """Return the first character of the text."""
    return text[0]


def get_last_character(text):
    """Return the last character using negative indexing."""
    return text[-1]


def get_first_word(text):
    """Return the first word from the text."""
    space_index = text.find(" ")
    return text[:space_index]


def get_last_word(text):
    """Return the last word from the text."""
    space_index = text.find(" ")
    return text[space_index + 1:]


def reverse_string(text):
    """Return the text in reverse order."""
    return text[::-1]


def every_other_character(text):
    """Return every second character from the text."""
    return text[::2]


def get_middle(text):
    """Return the middle character or middle two characters."""
    length = len(text)
    middle = length // 2

    if length % 2 == 0:
        return text[middle - 1:middle + 1]

    return text[middle]


def character_count(text):
    """Return the total number of characters."""
    return len(text)


def display_results(text, results):
    """Display the text processing results."""
    print("\n=== Text Processor Results ===")
    print(f"Original text: {text}")
    print(f"First character: {results['first_character']}")
    print(f"Last character: {results['last_character']}")
    print(f"First word: {results['first_word']}")
    print(f"Last word: {results['last_word']}")
    print(f"Reversed: {results['reversed']}")
    print(f"Every other character: {results['every_other']}")
    print(f"Middle: {results['middle']}")
    print(f"Character count: {results['count']}")


def main():
    """Run the text processor."""
    text = input("Enter a sentence: ")

    if len(text) == 0:
        print("Error: Please enter a sentence.")
        return

    results = {
        "first_character": get_first_character(text),
        "last_character": get_last_character(text),
        "first_word": get_first_word(text),
        "last_word": get_last_word(text),
        "reversed": reverse_string(text),
        "every_other": every_other_character(text),
        "middle": get_middle(text),
        "count": character_count(text),
    }

    display_results(text, results)


if __name__ == "__main__":
    main()