#!/usr/bin/env python3
""" Test the utils """
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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
        """Method that unit-tests GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient,
                          "org", new_callable=PropertyMock) as patched:
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

    # inputs to parametrize the test
    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected_return):
        """Method to unit-test GithubOrgClient.has_license"""
        github_client = GithubOrgClient("atlas")
        result = github_client.has_license(repo, license_key)
        self.assertEqual(expected_return, result)


@parameterized_class(
    ("org_payload", "repos_payload",
     "expected_repos", "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for github org client"""
    @classmethod
    def setUpClass(cls):
        """Method return example payloads found in the fixtures."""
        cls.get_patcher = patch("request.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """Method to stop patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Method to test GithubOrgClient.public_repos"""
        test_class = GithubOrgClient("atlas")
        assert True

    def test_public_repos_with_license(self):
        """Method to test the public_repos with the argument license"""
        test_class = GithubOrgClient("atlas")
        assert True
