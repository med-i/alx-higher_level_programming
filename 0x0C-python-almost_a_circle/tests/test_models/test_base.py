"""
This module provides tests for the Base class.
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Define test cases for the Base class from models.base."""

    def test_id_no_argument(self):
        """Test Base's id assignment when no id argument is passed."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_with_argument(self):
        """Test Base's id assignment with a specific id."""
        base = Base(12)
        self.assertEqual(base.id, 12)

    def test_to_json_string_basic(self):
        """Test basic case."""
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(json_dictionary, expected)

    def test_to_json_string_list_of_dictionaries(self):
        """Test with a list of dictionaries."""
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(3, 4, 4, 4, 2)
        rect3 = Rectangle(22, 33, 5, 18, 3)
        list_dictionaries = []
        list_dictionaries.append(rect1.to_dictionary())
        list_dictionaries.append(rect2.to_dictionary())
        list_dictionaries.append(rect3.to_dictionary())
        json_dictionary = Base.to_json_string(list_dictionaries)
        expected = (
            '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, '
            '{"x": 4, "y": 4, "id": 2, "height": 4, "width": 3}, '
            '{"x": 5, "y": 18, "id": 3, "height": 33, "width": 22}]'
        )
        self.assertEqual(json_dictionary, expected)

    def test_to_json_string_empty_list(self):
        """Test with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")


if __name__ == "__main__":
    unittest.main()
