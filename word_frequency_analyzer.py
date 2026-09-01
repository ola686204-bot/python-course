"""
    This is program that accepts a block of text from the user,
    processes is using dictionary patterns, and produces a detailed analysis report.
"""

def clean_text(text):
    """
    clean and normalize the input text.

    Args: 
        The word to clean
    Returns:
        The cleaned word with lowercase words and punctuation removed.
    """
    text = text.lower().strip()
    punctuation = ".,!?;:()[]{}\"'"

    for mark in punctuation:
        text = text.replace(mark, "")

    return text

def tokenize(text):
    """
        Split cleaned text into a list of individual words.

    Args:
        The word to be splited.

    Returns:
        A list containing individual words.
    """

    words = text.split()

    return words

def count_frequencies(words):
    """
        Count how often each words appears.

    Args:
        A list of individual words.

    Returns:
        A frequency dictionary using the get() pattern
    """
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0)+ 1

    return frequency

def remove_stop_words(frequency, stop_words=None):
    """
        Removes the stop words from the frequency
    Args:
        frequency: A dictionary containing words to be removed.
        stop_words: The words to be removed.
    Returns:
        returns a frequency dictionary with all stops words removed.
    """

    stop_words = [
        'the',
        'a',
        'an',
        'and',
        'or',
        'but',
        'in',
        'on',
        'at',
        'to',
        'for',
        'of',
        'is',
        'it',
        'was',
        'be',
        'are'
    ]

    return{
    word: count
    for word, count in frequency.items()
    if word not in stop_words
}

def get_top_n(frequency, n):
    """
        returns the n most frequent words.
    Args:
        frequency: a dictionary containing word frequncies.
        n : the number of top words to return.
    Returns:
        a sorted list of word and tuples.
    """
    sorted_words= sorted(
        frequency.items(),
        key = lambda item: item[1],
        reverse = True,
    )

    return sorted_words[:n]

def compute_stats(frequency):
    """
        returns a dictionary containing total_words
    Args:
        frequency: a dictionary containig word frequncies.
    Returns:
        a dictionary containing five different functions.
    """

    total_words = sum(frequency.values())
    unique_words = len(frequency)

    most_common = max(
        frequency,
        key=frequency.get
    )
    least_common = min(
        frequency,
        key=frequency.get
    )
    average_frequency = round(
        total_words / unique_words,
        2,
    )

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "most_common": most_common,
        "least_common": least_common,
        "average_frequency": average_frequency
    }

def display_report(text, frequency, stats, top_n):
    """
        Display the complete word frequency analysis report.
        
        Args:
            text: The original input text.
            frequency: A dictionary containing word frequencies.
            stats: A dictionary containing statistical information.
            top_n: A list of the n most frequent words.
            """
    print(f"\n{'='*50}")
    print(f"{'WORD FREQUENCY ANALYSIS REPORT':^50}")
    print(f"{'='*50}")

    print(f"Original Text:")
    print(f"{text})")


    print(f"\n{'Top words':^30}")
    print(f"{'-'*30}")
    print(f"{'Word':<20}{'count':>10}")
    print(f"{'_' * 30}")

    for word, count in top_n:
        print(f"{word:<20}{count:>10}")

    print(f"\n{'Statistics':^30}")
    print(f"{'_' * 30}")
    print(f"{'Total words':<25}{stats['total_words']:>5}")
    print(f"{'unique words:':<25}{stats['unique_words']:>5}")
    print(
        f"{'Most common:':<25}"
        f"{stats['most_common']:>5}"
    )
    print(
        f"{'Least common:':<25}"
        f"{stats['least_common']:>5}"
    )
    print(
        f"{'Average frequency:':<25}"
        f"{stats['average_frequency']:>5}"
    )
    print(f"{'=' * 50}")

def main():
    """Run the word analyzer."""
    text = input("Enter at least 10 words: ")

    if len(text.split()) < 10:
        print(f"Error: Please enter at least 10 words.")
        return

    cleaned = clean_text(text)
    words = tokenize(cleaned)
    frequency = count_frequencies(words)

    frequency = remove_stop_words(frequency)
    top_n = get_top_n(frequency, 10)
    stats = compute_stats(frequency)

    display_report(
        text,
        frequency,
        stats,
        top_n
    )

if __name__ == "__main__":
    main()
