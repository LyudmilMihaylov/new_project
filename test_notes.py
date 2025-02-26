import unittest
from notes_app import add_note, view_notes

class TestNotesApp(unittest.TestCase):
    def test_add_note(self):
        result = add_note("Test Title", "Test Content")
        self.assertTrue(result)  # Check if note was added successfully

if __name__ == '__main__':
    unittest.main()
