"""
This module provides tests for the Base class.
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_save_to_file_rectangles(self):
        """Test save multiple rectangles."""
        rect1 = Rectangle(10, 7, 2, 8, 12)
        rect2 = Rectangle(2, 4, id=89)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            expected = (
                '[{"x": 2, "y": 8, "id": 12, "height": 7, "width": 10}, '
                '{"x": 0, "y": 0, "id": 89, "height": 4, "width": 2}]'
            )
            self.assertEqual(file.read(), expected)

    def test_save_to_file_squares(self):
        """Test save multiple squares."""
        square1 = Square(10, id=12)
        square2 = Square(5, 3, 4, 89)
        Square.save_to_file([square1, square2])
        with open("Square.json", "r") as file:
            expected = (
                '[{"id": 12, "x": 0, "size": 10, "y": 0}, '
                '{"id": 89, "x": 3, "size": 5, "y": 4}]'
            )
            self.assertEqual(file.read(), expected)

    def test_save_to_file_empty_list(self):
        """Test save empty list of objects."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == "__main__":
    unittest.main()
