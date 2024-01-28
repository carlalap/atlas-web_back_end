#!/usr/bin/env python3
"""Unittests"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test Suit AccessNestedMap."""


@parameterized.expand(
    [
        {"a": 1}, path=("a",)
        {"a": {"b": 2}}, path=("a",)
        {"a": {"b": 2}}, path=("a", "b")
    ])
def test_access_nested_map(self, nested_map, path, expected_result):
    self.assertEqual(access_nested_map(nested_map, path),
                     expected_result)
