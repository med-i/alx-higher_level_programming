#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ascending_list(self):
        """Tests a list of ascending integers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_descending_list(self):
        """Tests a list of descending integers."""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_mixed_list(self):
        """Tests a mixed list of integers."""
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_negative_list(self):
        """Tests a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_one_element(self):
        """Tests a list with a single integer."""
        self.assertEqual(max_integer([5]), 5)

    def test_2_elements(self):
        """Tests a list with two integers."""
        self.assertEqual(max_integer([2, 3]), 3)
        self.assertEqual(max_integer([3, 2]), 3)

    def test_all_neg_elements(self):
        """Tests a list with all negative integers."""
        self.assertEqual(max_integer([-2, -5, -1]), -1)

    def test_all_neg_with_0(self):
        """Tests a list with all negative integers and a zero."""
        self.assertEqual(max_integer([-2, -5, 0]), 0)

    def test_mixed_elements(self):
        """Tests a list with mixed positive and negative integers."""
        self.assertEqual(max_integer([-2, 5, 0, 3, -1]), 5)

    def test_same_elements_not_max(self):
        """Tests a list with the same repeated integer that is not max."""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_same_elements_max(self):
        """Tests a list with the same repeated integer that is max."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_all_0(self):
        """Tests a list with all zeros."""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_large_numbers(self):
        """Tests a list with large numbers."""
        self.assertEqual(max_integer([10**6, 10**5, 10**4]), 10**6)

    def test_many_elements(self):
        """Tests a list with many elements."""
        self.assertEqual(max_integer([i for i in range(1000)]), 999)

    def test_empty_list(self):
        """Tests an empty list."""
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
