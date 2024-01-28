#!/usr/bin/env python3
"""Unittests"""
import unittest
from unitest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test Suit AccessNestedMap."""
    """ to test the function for following inputs """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Method to test that the method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path),
                         expected_result)

    """We use the assertRaises context manager to test that a
    KeyError is raised for the following inputs"""

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expec_except):
        """Method that test that a KeyError is raised according inputs"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(expec_except, error.exception)


class TestGetJson(unittest.TestCase):
    """Class that test get_json funtcion that
    Get JSON from remote URL."""

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Mocking the requests.get method"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.request.get',
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)

            # Ensure that the mocked get method was
            # called exactly once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Test that the output of get_json is equal to test_payload
            self.assertEqual(result, test_payload)
