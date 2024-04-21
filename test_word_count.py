import unittest
from word_count import count_words, read_file
from collections import Counter

class TestWordCount(unittest.TestCase):

    def test_count_words(self):
        """Test counting words accurately."""
        text = "Hello world! Hello everyone."
        expected_result = Counter({'hello': 2, 'world': 1, 'everyone': 1})
        self.assertEqual(count_words(text), expected_result)

    def test_read_file(self):
        """Test reading file content."""
        # Create a temporary text file for testing
        with open('temp_test_file.txt', 'w') as temp_file:
            temp_file.write("Hello world! Hello everyone.")

        expected_content = "Hello world! Hello everyone."
        self.assertEqual(read_file('temp_test_file.txt'), expected_content)

if __name__ == '__main__':
    unittest.main()
