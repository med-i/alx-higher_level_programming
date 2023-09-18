"""
This module provides tests for the Rectangle class.
"""

import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Define test cases for the Rectangle class from models.rectangle."""

    def test_id_no_argument(self):
        """Test Rectangle's id assignment when no id argument is passed."""
        Base._Base__nb_objects = 0
        base = Base()
        rect1 = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        self.assertEqual(base.id, 1)
        self.assertEqual(rect1.id, 2)
        self.assertEqual(rect2.id, 3)

    def test_id_with_argument(self):
        """Test Rectangle's id assignment with a specific id."""
        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.id, 12)

    def test_width_getter(self):
        """Test width getter."""
        rect = Rectangle(10, 2)
        self.assertEqual(rect.width, 10)

    def test_height_getter(self):
        """Test height getter."""
        rect = Rectangle(10, 2)
        self.assertEqual(rect.height, 2)

    def test_x_getter(self):
        """Test x getter."""
        rect = Rectangle(10, 2, 5)
        self.assertEqual(rect.x, 5)

    def test_y_getter(self):
        """Test y getter."""
        rect = Rectangle(10, 2, 0, 5)
        self.assertEqual(rect.y, 5)

    def test_width_setter(self):
        """Test width setter."""
        rect = Rectangle(10, 2)
        rect.width = 5
        self.assertEqual(rect.width, 5)

    def test_height_setter(self):
        """Test height setter."""
        rect = Rectangle(10, 2)
        rect.height = 1
        self.assertEqual(rect.height, 1)

    def test_x_setter(self):
        """Test x setter."""
        rect = Rectangle(10, 2, 5)
        rect.x = 1
        self.assertEqual(rect.x, 1)

    def test_y_setter(self):
        """Test y setter."""
        rect = Rectangle(10, 2, 0, 5)
        rect.y = 1
        self.assertEqual(rect.y, 1)

    def test_width_not_integer_value(self):
        """Test width setter with non-integer value."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("str", 2)

    def test_height_not_integer_value(self):
        """Test height setter with non-integer value."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "str")

    def test_x_not_integer_value(self):
        """Test x setter with non-integer value."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "str")

    def test_y_not_integer_value(self):
        """Test y setter with non-integer value."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "str")

    def test_width_negative_value(self):
        """Test width setter with negative value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_width_zero_value(self):
        """Test width setter with zero value."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_height_negative_value(self):
        """Test height setter with negative value."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_height_zero_value(self):
        """Test height setter with zero value."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_x_is_negative(self):
        """Test x setter with negative value."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -2)

    def test_y_is_negative(self):
        """Test y setter with negative value."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -2)

    def test_area_calculation(self):
        """Test Rectangle's area."""
        rect = Rectangle(10, 2)
        self.assertEqual(rect.area(), 20)

    def test_display_square(self):
        """Test print square 2 by 2."""
        rect = Rectangle(2, 2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_single_row(self):
        """Test print a single row."""
        rect = Rectangle(5, 1)
        expected = "#####\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_single_column(self):
        """Test print a single column."""
        rect = Rectangle(1, 5)
        expected = "#\n#\n#\n#\n#\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_x(self):
        """Test print with horizontal offset."""
        rect = Rectangle(3, 2, 1)
        expected = " ###\n ###\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_y(self):
        """Test print with vertical offset."""
        rect = Rectangle(3, 2, 0, 2)
        expected = "\n\n###\n###\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_display_with_x_and_y(self):
        """Test print with horizontal and vertical offsets."""
        rect = Rectangle(3, 2, 2, 2)
        expected = "\n\n  ###\n  ###\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str_without_x_and_y(self):
        """Test __str__ without x and y values."""
        rect = Rectangle(10, 2)
        rect.id = 12
        excepted = "[Rectangle] (12) 0/0 - 10/2"
        self.assertEqual(rect.__str__(), excepted)

    def test_str_with_id_argument(self):
        """Test __str__ with specific id."""
        rect = Rectangle(4, 12, id=5)
        excepted = "[Rectangle] (5) 0/0 - 4/12"
        self.assertEqual(rect.__str__(), excepted)

    def test_str_with_x_and_y(self):
        """Test __str__ with x and y values."""
        rect = Rectangle(7, 7, 3, 4)
        rect.id = 49
        excepted = "[Rectangle] (49) 3/4 - 7/7"
        self.assertEqual(rect.__str__(), excepted)

    def test_update_args_id_attribute(self):
        """Test update args id attribute."""
        rect = Rectangle(10, 2)
        rect.update(89)
        self.assertEqual(rect.id, 89)

    def test_update_args_width_attribute(self):
        """Test update args width attribute."""
        rect = Rectangle(10, 2)
        rect.update(89, 5)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)

    def test_update_args_height_attribute(self):
        """Test update args height attribute."""
        rect = Rectangle(10, 2)
        rect.update(89, 5, 1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)

    def test_update_args_x_attribute(self):
        """Test update args x attribute."""
        rect = Rectangle(10, 2)
        rect.update(89, 5, 1, 4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)

    def test_update_args_y_attribute(self):
        """Test update args y attribute."""
        rect = Rectangle(10, 2)
        rect.update(89, 5, 1, 4, 3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 3)

    def test_update_args_more_than_available(self):
        """Test update more args than available."""
        rect = Rectangle(10, 2)
        rect.update(89, 5, 1, 4, 11, 12, 13)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)

    def test_update_kwargs_id_attribute(self):
        """Test update kwargs id attribute."""
        rect = Rectangle(10, 2)
        rect.update(id=89)
        self.assertEqual(rect.id, 89)

    def test_update_kwargs_width_attribute(self):
        """Test update kwargs width attribute."""
        rect = Rectangle(10, 2)
        rect.update(id=89, width=5)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)

    def test_update_kwargs_height_attribute(self):
        """Test update kwargs height attribute."""
        rect = Rectangle(10, 2)
        rect.update(id=89, width=5, height=1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)

    def test_update_kwargs_x_attribute(self):
        """Test update kwargs x attribute."""
        rect = Rectangle(10, 2)
        rect.update(id=89, width=5, height=1, x=4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)

    def test_update_kwargs_y_attribute(self):
        """Test update kwargs y attribute."""
        rect = Rectangle(10, 2)
        rect.update(id=89, width=5, height=1, x=4, y=3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 3)

    def test_update_kwargs_random_position(self):
        """Test update random position kwargs."""
        rect = Rectangle(10, 2)
        rect.update(y=3, height=1, width=5, id=89, x=4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 3)

    def test_update_kwargs_unknown_attributes(self):
        """Test update unknow kwargs attributes."""
        rect = Rectangle(10, 2)
        rect.update(pos=(4, 5), id=89, width=5, height=1, x=4, y=3, area=20)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 4)

    def test_update_no_args_no_kwargs(self):
        """Test no args or kwargs attributes."""
        rect = Rectangle(10, 2, id=12)
        rect.update()
        self.assertEqual(rect.id, 12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_to_dictionary(self):
        """Test Rectangle to dictionary."""
        rect = Rectangle(10, 2, 1, 9, 12)
        expected = {"x": 1, "y": 9, "id": 12, "height": 2, "width": 10}
        self.assertEqual(rect.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
