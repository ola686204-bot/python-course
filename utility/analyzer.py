
"""Word frequency analysis functions."""

import os
import re

from display import display_frequency, display_message, get_input, print_analyzer_menu
from file_handler import read_text, write_text
from logger import log_operation


WORD_PATTERN = r"[A-Za-z0-9']+"
TOP_WORD_LIMIT = 10
REPORT_SEPARATOR = "\n"
REPORT_TITLE = "WORD FREQUENCY ANALYSIS"


def count_words(text):
    """Count the frequency of words in text.

    Args:
        text (str): Text to analyze.

    Returns:
        dict: Word frequency mapping.
    """
    words = re.findall(WORD_PATTERN, text.lower())
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def get_top_words(frequencies, limit=TOP_WORD_LIMIT):
    """Return the most frequent words.

    Args:
        frequencies (dict): Word frequency mapping.
        limit (int): Maximum number of words.

    Returns:
        list: Sorted word and count tuples.
    """
    return sorted(
        frequencies.items(),
        key=lambda item: (-item[1], item[0])
    )[:limit]


def analyze_text(text):
    """Analyze text and return its top words.

    Args:
        text (str): Text to analyze.

    Returns:
        list: Top word frequency tuples.
    """
    return get_top_words(count_words(text))


def analyze_file(file_path):
    """Read and analyze a text file.

    Args:
        file_path (str): Input text file.

    Returns:
        tuple: Success status and analysis result.
    """
    success, text = read_text(file_path)
    if not success:
        return False, text
    return True, analyze_text(text)


def create_report(words):
    """Create a formatted analysis report.

    Args:
        words (list): Word and count tuples.

    Returns:
        str: Analysis report.
    """
    lines = [REPORT_TITLE]
    for position, item in enumerate(words, start=1):
        lines.append(f"{position}. {item[0]} - {item[1]}")
    return REPORT_SEPARATOR.join(lines) + REPORT_SEPARATOR


def save_analysis(words, file_path):
    """Save an analysis report.

    Args:
        words (list): Word and count tuples.
        file_path (str): Report destination.

    Returns:
        bool: True when saving succeeds.
    """
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    return write_text(file_path, create_report(words))


def handle_text_input(report_path, log_path):
    """Handle analysis of user-entered text."""
    text = get_input("Enter text: ")
    words = analyze_text(text)
    display_frequency(words)
    if save_analysis(words, report_path):
        log_operation("Text analysis completed", log_path)
        display_message("Analysis report saved.")


def handle_file_input(report_path, log_path):
    """Handle analysis of a text file."""
    file_path = get_input("File path: ")
    success, words = analyze_file(file_path)
    if not success:
        display_message(words)
        return
    display_frequency(words)
    if save_analysis(words, report_path):
        log_operation("File analysis completed", log_path)
        display_message("Analysis report saved.")


def run_analyzer(report_path, log_path):
    """Run the interactive word frequency analyzer."""
    while True:
        print_analyzer_menu()
        choice = get_input("Choose an option: ")
        if choice == "1":
            handle_text_input(report_path, log_path)
        elif choice == "2":
            handle_file_input(report_path, log_path)
        elif choice == "3":
            break
        else:
            display_message("Invalid choice. Please try again.")
