#!/usr/bin/env python3
""" Test the utils """
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Class function that test funciton
    A Githib org client """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json", return_value={"organization": True})
    def test_org(self, org_name, mock_get_json):
        """method that test that GithubOrgClient.org
        returns the correct value."""
        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, mock_get_json.return_value)
        mock_get_json.assert_called_once

    def test_public_repos_url(self):
        """Method that unit-test GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock) as patched:
               test_json = {"url": "google",
                            "repos_url": "https://www.atlasschool.com/"}
               patched.return_value = test_json
               github_client = GithubOrgClient(test_json.get("url"))
               response = github_client._public_repos_url
               patched.assert_called_once()
               self.assertEqual(response, test_json.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, get_patch):
         """ Mocking _public_repos_url and specifying its return value"""
         get_patch.return_value = [{"name": "atlas"},
                                  {"name": "abc"}]
         with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_get:
                mock_get.return_value = "http://google.com"   
                github_client = GithubOrgClient("atlas")
                result = github_client.public_repos()
                self.assertEqual(result, ["atlas", "abc"])
                get_patch.assert_called_once()
                mock_get.assert_called_once()
