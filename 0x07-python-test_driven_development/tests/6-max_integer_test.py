#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordere list - max at end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with empty list - should return None"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_number(self):
        """Test with mixed positive and negative"""
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_same_number(self):
        """Test with all same values"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()