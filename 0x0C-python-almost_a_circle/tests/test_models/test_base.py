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

    def setUp(self):
        """Delete JSON and CSV files, if they exist, to start fresh."""
        files_to_remove = [
            "Rectangle.json",
            "Square.json",
            "Rectangle.csv",
            "Square.csv",
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)

    def tearDown(self):
        """Clean up JSON and CSV files after tests."""
        TestBaseClass.setUp(self)

    def test_0_id_no_argument(self):
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

    def test_save_to_file_empty_list_rectangle(self):
        """Test save empty list of objects using a rectangle."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_none_rectangle(self):
        """Test save none using a rectangle."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list_square(self):
        """Test save empty list of objects using a square."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_none_square(self):
        """Test save none using a square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """Test conversion from JSON string to list."""
        json_str = (
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
            '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        )
        list_output = Base.from_json_string(json_str)
        expected = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0},
        ]
        self.assertEqual(list_output, expected)

    def test_from_empty_json_string(self):
        """Test conversion from an empty JSON string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_create_rectangle(self):
        """Test create Rectangle instance."""
        rect1 = Rectangle(3, 5, 1, id=89)
        dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**dictionary)
        self.assertIsInstance(rect2, Rectangle)
        self.assertNotEqual(rect1, rect2)
        self.assertEqual(rect1.width, rect2.width)
        self.assertEqual(rect1.height, rect2.height)
        self.assertEqual(rect1.x, rect2.x)
        self.assertEqual(rect1.y, rect2.y)
        self.assertEqual(rect1.id, rect2.id)

    def test_create_square(self):
        """Test create Square instance."""
        square1 = Square(5, 1, 2, 89)
        dictionary = square1.to_dictionary()
        square2 = Square.create(**dictionary)
        self.assertIsInstance(square2, Square)
        self.assertNotEqual(square1, square2)
        self.assertEqual(square1.size, square2.size)
        self.assertEqual(square1.width, square2.width)
        self.assertEqual(square1.height, square2.height)
        self.assertEqual(square1.x, square2.x)
        self.assertEqual(square1.y, square2.y)
        self.assertEqual(square1.id, square2.id)

    def test_load_from_non_existent_file(self):
        """Test load from a non-existent file."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles_from_file(self):
        """Test loading rectangles from a file."""
        rect1 = Rectangle(10, 5, id=12)
        rect2 = Rectangle(5, 5, 2, 8, 89)
        list_rectangles = [rect1, rect2]
        Rectangle.save_to_file(list_rectangles)
        loaded_rectangles = Rectangle.load_from_file()

        self.assertEqual(len(loaded_rectangles), 2)
        for original, loaded in zip(list_rectangles, loaded_rectangles):
            self.assertEqual(original.width, loaded.width)
            self.assertEqual(original.height, loaded.height)
            self.assertEqual(original.x, loaded.x)
            self.assertEqual(original.y, loaded.y)
            self.assertEqual(original.id, loaded.id)

    def test_load_squares_from_file(self):
        """Test loading squares from a file."""
        square1 = Square(10, id=12)
        square2 = Square(5, 2, 4, 89)
        list_squares = [square1, square2]
        Square.save_to_file(list_squares)
        loaded_squares = Square.load_from_file()

        self.assertEqual(len(loaded_squares), 2)
        for original, loaded in zip(list_squares, loaded_squares):
            self.assertEqual(original.size, loaded.size)
            self.assertEqual(original.x, loaded.x)
            self.assertEqual(original.y, loaded.y)
            self.assertEqual(original.id, loaded.id)

    def test_rectangle_save_to_csv(self):
        """Test save a rectangle to a CSV file."""
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4)
        list_rectangles = [rect1, rect2]
        Rectangle.save_to_file_csv(list_rectangles)
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_square_save_to_csv(self):
        """Test save a square to a CSV file."""
        s1 = Square(5, 1, 2, 6)
        s2 = Square(7, 2, 3)
        list_squares = [s1, s2]
        Square.save_to_file_csv(list_squares)
        self.assertTrue(os.path.exists("Square.csv"))

    def test_rectangle_load_from_csv(self):
        """Test load a rectangle from a CSV file."""
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4)
        list_rectangles_input = [rect1, rect2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(
            len(list_rectangles_input), len(list_rectangles_output)
        )
        for i in range(len(list_rectangles_input)):
            self.assertEqual(
                list_rectangles_input[i].to_dictionary(),
                list_rectangles_output[i].to_dictionary(),
            )

    def test_square_load_from_csv(self):
        """Test load a square from a CSV file."""
        s1 = Square(5, 1, 2, 6)
        s2 = Square(7, 2, 3)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()

        self.assertEqual(len(list_squares_input), len(list_squares_output))
        for i in range(len(list_squares_input)):
            self.assertEqual(
                list_squares_input[i].to_dictionary(),
                list_squares_output[i].to_dictionary(),
            )


if __name__ == "__main__":
    unittest.main()
