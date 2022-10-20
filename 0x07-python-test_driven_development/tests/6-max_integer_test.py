#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """
    TextMaxInt a class to test the max_integer modulue

    testing against:
    """

    def test_max_integer(self):
        """Positive integers"""
        result = max_integer([1, 2, 3, 4])
        counter = max([1, 2, 3, 4])
        self.assertEqual(result, counter)

    def test_max_integer1(self):
        """Negative integers"""
        result = max_integer([-1, -2, -3, -4])
        counter = max([-1, -2, -3, -4])
        self.assertEqual(result, counter)

    def test_max_integer2(self):
        """A mixture of positive and negative integers"""
        result = max_integer([-1, 2, 3, -4])
        counter = max([-1, 2, 3, -4])
        self.assertEqual(result, counter)

    def test_max_integer3(self):
        """Positive floats"""
        result = max_integer([1.4, 2.2, 3.5, 4.7])
        counter = max([1.4, 2.2, 3.5, 4.7])
        self.assertEqual(result, counter)

    def test_max_integer4(self):
        """Negative floats"""
        result = max_integer([-1.4, -2.2, -3.5, -4.7])
        counter = max([-1.4, -2.2, -3.5, -4.7])
        self.assertEqual(result, counter)

    def test_max_integer5(self):
        """Positive and negative floats and integers"""
        result = max_integer([-1.5, 2, 3, -4.6])
        counter = max([-1.5, 2, 3, -4.6])
        self.assertEqual(result, counter)

    def test_matrix_integer6(self):
        result = max_integer([1])
        counter max([1])
        self.assertEqual(result, counter)

    def test_matrix_integer6(self):
        result = max_integer([])
        counter max([])
        self.assertEqual(result, counter)
