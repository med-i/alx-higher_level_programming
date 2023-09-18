"""
This module provides tests for the Base class.
"""

import unittest
from models.base import Base


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


if __name__ == "__main__":
    unittest.main()
