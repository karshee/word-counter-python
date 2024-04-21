import unittest
from unittest.mock import patch, mock_open
from word_count import read_file, count_words, print_word_counts, main
from collections import Counter
from io import StringIO
import sys

class TestWordCount(unittest.TestCase):

    def test_read_file_success(self):
        """Test reading file successfully."""
        mock_content = "Hello world! Hello everyone."
        with patch("builtins.open", mock_open(read_data=mock_content)):
            content = read_file("dummy_path.txt")
            self.assertEqual(content, mock_content)

    def test_read_file_not_found(self):
        """Test file not found error."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            with patch("sys.stderr"):
                with self.assertRaises(SystemExit) as cm:
                    read_file("nonexistent_path.txt")
                self.assertEqual(cm.exception.code, 1)

    def test_count_words(self):
        """Test word counting accurately."""
        text = "Hello world! Hello everyone."
        expected_result = Counter({'hello': 2, 'world': 1, 'everyone': 1})
        self.assertEqual(count_words(text), expected_result)


    def test_print_word_counts(self):
        """Test printing of word counts."""
        word_counts = Counter({'hello': 2, 'world': 1, 'everyone': 1})
        expected_output = "hello: 2\nworld: 1\neveryone: 1\n"
        with patch('sys.stdout', new=StringIO()) as captured_output:
            print_word_counts(word_counts)
            self.assertEqual(captured_output.getvalue(), expected_output)

    def test_main_integration(self):
        """Integration test for the main function behavior."""
        mock_content = "Hello world! Hello everyone."
        expected_output = "hello: 2\nworld: 1\neveryone: 1\n"
        with patch("builtins.open", mock_open(read_data=mock_content)), \
                patch("sys.argv", ["word_count.py", "dummy_path.txt"]), \
                patch('sys.stdout', new=StringIO()) as captured_output:
            main("dummy_path.txt")
            self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
