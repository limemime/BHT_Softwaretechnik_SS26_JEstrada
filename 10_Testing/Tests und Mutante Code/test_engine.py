import unittest
from unittest.mock import patch, mock_open
from engine import EntropyEngine

class TestEntropyEngineInit(unittest.TestCase):
    def test_init_sets_correct_attributes(self):
        """Test that __init__ correctly stores the passed parameters and initializes the state variables."""
        # We mock '_load_dictionary' to isolate the rest of the init assignments
        # and prevent it from reading actual files on disk during this test.
        with patch.object(EntropyEngine, '_load_dictionary', return_value=['test', 'words']) as mock_load:
            engine = EntropyEngine('dummy_path.txt', 5, 15)
            
            # Verify arguments are assigned correctly
            self.assertEqual(engine.filepath, 'dummy_path.txt')
            self.assertEqual(engine.min_sleep, 5)
            self.assertEqual(engine.max_sleep, 15)
            
            # Verify initial state variables
            self.assertFalse(engine.running)
            self.assertIsNone(engine.thread)
            self.assertEqual(engine.search_count, 0)
            self.assertIsNone(engine.driver)
            
            # Verify the words list was set from the return value of _load_dictionary
            self.assertEqual(engine.words, ['test', 'words'])
            mock_load.assert_called_once()

    def test_load_dictionary_success(self):
        """Test that _load_dictionary correctly loads and cleans words from a file."""
        # Prepare a mock file content with whitespace and empty lines
        file_content = "  word1  \n\nword2\n   \nword3"
        with patch('builtins.open', mock_open(read_data=file_content)):
            engine = EntropyEngine('dummy_path.txt', 5, 15)
            
            # Check that whitespace is stripped and empty lines are discarded
            self.assertEqual(engine.words, ['word1', 'word2', 'word3'])

    def test_load_dictionary_file_not_found(self):
        """Test that _load_dictionary gracefully handles missing files by logging and returning an empty list."""
        with patch('builtins.open', side_effect=FileNotFoundError):
            with patch('logging.error') as mock_log_error:
                engine = EntropyEngine('missing_file.txt', 5, 15)
                
                # Check that words list is empty
                self.assertEqual(engine.words, [])
                # Verify standard error log was generated
                mock_log_error.assert_any_call("Dictionary file 'missing_file.txt' not found.")

    def test_load_dictionary_other_exception(self):
        """Test that _load_dictionary catches unexpected exceptions, logs them, and returns an empty list."""
        test_exception = Exception("Unexpected Disk Error")
        with patch('builtins.open', side_effect=test_exception):
            with patch('logging.error') as mock_log_error:
                engine = EntropyEngine('corrupted_file.txt', 5, 15)
                
                # Check that words list is empty
                self.assertEqual(engine.words, [])
                # Verify that logging.error recorded the exception message
                mock_log_error.assert_any_call(f"Error reading dictionary: {test_exception}")

    def test_init_extreme_sleep_ranges(self):
        """Test that __init__ accepts and stores extreme sleep values (negative, zero, out-of-order) without crashing."""
        with patch.object(EntropyEngine, '_load_dictionary', return_value=[]):
            # Case 1: Zero sleep
            engine_zero = EntropyEngine('dummy.txt', 0, 0)
            self.assertEqual(engine_zero.min_sleep, 0)
            self.assertEqual(engine_zero.max_sleep, 0)

            # Case 2: Negative sleep values
            engine_neg = EntropyEngine('dummy.txt', -5, -1)
            self.assertEqual(engine_neg.min_sleep, -5)
            self.assertEqual(engine_neg.max_sleep, -1)

            # Case 3: Out-of-order bounds (min > max)
            engine_inverted = EntropyEngine('dummy.txt', 30, 10)
            self.assertEqual(engine_inverted.min_sleep, 30)
            self.assertEqual(engine_inverted.max_sleep, 10)

    def test_init_invalid_sleep_types(self):
        """Test that __init__ accepts and stores non-numeric types for sleep limits without immediately crashing."""
        with patch.object(EntropyEngine, '_load_dictionary', return_value=[]):
            # Case 1: Passing strings instead of numbers
            engine_str = EntropyEngine('dummy.txt', "minimum", "maximum")
            self.assertEqual(engine_str.min_sleep, "minimum")
            self.assertEqual(engine_str.max_sleep, "maximum")

            # Case 2: Passing None values
            engine_none = EntropyEngine('dummy.txt', None, None)
            self.assertIsNone(engine_none.min_sleep)
            self.assertIsNone(engine_none.max_sleep)

    def test_load_dictionary_invalid_filepath_types(self):
        """Test how _load_dictionary behaves when filepath is a senseless type (None, integer)."""
        with patch('logging.error') as mock_log_error:
            # Case 1: None filepath (should cause TypeError in open, which is caught by Exception handler)
            engine_none_path = EntropyEngine(None, 5, 15)
            self.assertEqual(engine_none_path.words, [])
            
            # Assert that logging.error was called with a message starting with the standard prefix
            none_call_args = [call[0][0] for call in mock_log_error.call_args_list]
            self.assertTrue(any(arg.startswith("Error reading dictionary:") for arg in none_call_args))

        with patch('logging.error') as mock_log_error:
            # Case 2: Integer filepath (causes OSError or TypeError depending on OS, which is caught by Exception handler)
            engine_int_path = EntropyEngine(12345, 5, 15)
            self.assertEqual(engine_int_path.words, [])
            
            # Assert that logging.error was called with a message starting with the standard prefix
            int_call_args = [call[0][0] for call in mock_log_error.call_args_list]
            self.assertTrue(any(arg.startswith("Error reading dictionary:") for arg in int_call_args))

    def test_load_dictionary_empty_filepath(self):
        """Test how _load_dictionary behaves with an empty string filepath."""
        with patch('logging.error') as mock_log_error:
            engine_empty_path = EntropyEngine('', 5, 15)
            self.assertEqual(engine_empty_path.words, [])
            # Under standard systems, opening '' raises FileNotFoundError or OSError, both of which are caught.
            # We verify that logging recorded a load attempt failure.
            self.assertTrue(mock_log_error.called)

if __name__ == '__main__':
    unittest.main()

