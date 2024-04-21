import sys
from collections import Counter
import re

def read_file(file_path):
    """Reads content from a file and returns it as a string.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}", file=sys.stderr)
        sys.exit(1)

def count_words(text):
    """Counts the occurrences of each word in a given text.

    Args:
        text (str): The text to process.

    Returns:
        collections.Counter: A Counter object with words as keys and their counts as values.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def print_word_counts(word_counts):
    """Prints word counts in descending order of occurrence.

    Args:
        word_counts (collections.Counter): A Counter object with words as keys and their counts as values.
    """
    for word, count in word_counts.most_common():
        print(f"{word}: {count}")

def main(file_path):
    """Main function to count and print word occurrences in a file.

    Args:
        file_path (str): The path to the file.
    """
    text = read_file(file_path)
    word_counts = count_words(text)
    print_word_counts(word_counts)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <path_to_file>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
