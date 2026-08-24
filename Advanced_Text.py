"""
    This is an Advanced Text
    Transformation program that 
    uses string methods and formatting to produce Text output.
"""

def word_count(text):
    """count total and unique word in text.
    
    Args:
        text: The text to be analyzed.
        
    Returns:
        A dictionary containing the total and unique word count.
    """
    words = text.lower().split()
    return {
        "total": len(words),
        "unique": len(set(words))
    }

def palindrome_checker(text):
    """Check if the given text is a palindrome.
    
    Args:
        text: The text to be checked.
        
    Returns:
        True if the text is a palindrome and also ignoring case and whitespace, False otherwise.
    """
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]

def text_normalizer(text):
    """Normalize the text by removing strip whitespace,
     and converting to lowercase.
    
    Args:
        text: The text to be normalized.
        
    Returns:
        The normalized text.
    """
    return text.strip().lower()

def sentence_builder(name, score, grade):
    """Build a sentence using string formatting.
    
    Args:
        name: The name of the student.
        score: The score of the student.
        grade: The grade of the student.
        
    Returns:
        A formatted sentence containing the student's information.
    """
    return f"Student {name} scored {score} and received a grade of {grade}."

def word_frequency(text):
    """returns the top 3 most frequent  words as a formatted string.
    
    Args:
        text: The text to be analyzed.
        
    Returns:
        A dictionary containing words as keys and their frequencies as values.
    """
    words = text.lower().split()
    frequencies= {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies  

def format_table(data):
    """cretate an alignment table of names and scores.   
    Args:
        data: A list of dictionaries containing the data to be formatted.
        
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
    text = input("Enter some Text:")

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
        ("Charlie", 75)
    ]
    table = format_table(table_data)

    print("\n=== Advanced Text Tools ===")
    print(f"Original text: {text}")
    print(f"Total words: {count['total']}")
    print(f"Unique words: {count['unique']}")
    print(f"Palindrome: {palindrome}")
    print(f"Normalized text: {normalized_text}")
    print(f"Top 3 words: {frequency}")
    print(f"Report: {report}")
    print(f"\n{table}")
def main():
        """Start the Advanced Text tools program."""
        run_tools()

if __name__ == "__main__":
    main() 