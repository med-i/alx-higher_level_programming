"""
This module provides tests for the Square class.
"""

import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Define test cases for the Square class from models.square."""

    def test_basic_square(self):
        """Test basic square with given size."""
        square = Square(5)
        square.id = 1
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.area(), 25)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 1)

    def test_square_size_is_not_int(self):
        """Test size with non-integer value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_square_x_is_not_int(self):
        """Test x with non-integer value."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_square_y_is_not_int(self):
        """Test y with non-integer value."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_size_zero_value(self):
        """Test size with zero value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_size_negative_value(self):
        """Test size with negative value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_x_negative_value(self):
        """Test size with negative value."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_square_y_negative_value(self):
        """Test y with negative value."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_str(self):
        """Test __str__ method."""
        square = Square(5)
        square.id = 12
        expected = "[Square] (12) 0/0 - 5"
        self.assertEqual(square.__str__(), expected)

    def test_update_args(self):
        """Test updating attributes using *args."""
        square = Square(5)
        square.update(1, 2, 3, 4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.area(), 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_update_kwargs(self):
        """Test updating attributes uisng **kwargs."""
        square = Square(5)
        square.update(x=3, size=2, id=1, y=4)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.width, 2)
        self.assertEqual(square.height, 2)
        self.assertEqual(square.area(), 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_to_dictionary(self):
        """Test to dictionary."""
        square = Square(10, 2, 1, id=89)
        expected = {"id": 89, "x": 2, "size": 10, "y": 1}
        self.assertEqual(square.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
