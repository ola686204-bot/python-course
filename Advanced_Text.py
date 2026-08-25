"""Provide advanced text analysis and transformation tools."""


def word_count(text):
    """Count the total and unique words in text.

    Args:
        text: The text to be analyzed.

    Returns:
        A dictionary containing total and unique word counts.
    """
    words = text.lower().split()

    return {
        "total": len(words),
        "unique": len(set(words)),
    }


def palindrome_checker(text):
    """Check whether text is a palindrome.

    The check ignores case and whitespace.

    Args:
        text: The text to be checked.

    Returns:
        True if the text is a palindrome, otherwise False.
    """
    cleaned_text = text.lower().replace(" ", "")

    return cleaned_text == cleaned_text[::-1]


def text_normalizer(text):
    """Normalize text by removing extra whitespace and lowercasing.

    Args:
        text: The text to be normalized.

    Returns:
        The normalized text.
    """
    return " ".join(text.strip().lower().split())


def sentence_builder(name, score, grade):
    """Build a formatted student report.

    Args:
        name: The student's name.
        score: The student's score.
        grade: The student's grade.

    Returns:
        A formatted sentence containing the student's information.
    """
    return f"Student {name} scored {score} and received a grade of {grade}."


def word_frequency(text):
    """Count the frequency of each word in the text.

    Args:
        text: The text to be analyzed.

    Returns:
        A dictionary containing each word and its frequency.
    """
    words = text.lower().split()
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def format_table(data):
    """Create an aligned table of names and scores.

    Args:
        data: A list of name and score tuples.

    Returns:
        A formatted string representing the table.
    """
    lines = [
        f"{'Name':<15}{'Score':>10}",
        f"{'-' * 25}",
    ]

    for name, score in data:
        lines.append(f"{name:<15}{score:>10}")

    return "\n".join(lines)


def run_tools():
    """Run the text transformation tools."""
    text = input("Enter some text: ")

    if not text.strip():
        print("Error: Please enter some text.")
        return

    count = word_count(text)
    palindrome = palindrome_checker(text)
    normalized_text = text_normalizer(text)
    frequency = word_frequency(text)

    report = sentence_builder("Student", 85, "B")

    table_data = [
        ("Alice", 90),
        ("Bob", 85),
        ("Charlie", 75),
    ]

    table = format_table(table_data)

    print("\n=== Advanced Text Tools ===")
    print(f"Original text: {text}")
    print(f"Total words: {count['total']}")
    print(f"Unique words: {count['unique']}")
    print(f"Palindrome: {palindrome}")
    print(f"Normalized text: {normalized_text}")
    print(f"Word frequencies: {frequency}")
    print(f"Report: {report}")
    print(f"\n{table}")


def main():
    """Start the Advanced Text Tools program."""
    run_tools()


if __name__ == "__main__":
    main()
