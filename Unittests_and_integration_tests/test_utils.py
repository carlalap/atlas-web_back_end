#!/usr/bin/env python3
"""Unittests"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test Suit AccessNestedMap."""
    """ to test the function for following inputs """

    @parameterized.expand(
        [
            {"a": 1}, path=("a",)
            {"a": {"b": 2}}, path=("a",)
            {"a": {"b": 2}}, path=("a", "b")
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Method to test that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)

    @parameterized.expand([
            ({}, ["a"], KeyError),
            ({"a": 1}, ["a", "b"], KeyError)
        ])
