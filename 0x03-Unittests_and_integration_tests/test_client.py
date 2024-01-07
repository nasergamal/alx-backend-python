#!/usr/bin/env python3
"""tests for client class
"""
from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import requests
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Union
)
import unittest
from unittest.mock import (
    patch,
    Mock,
    MagicMock,
    PropertyMock,
    )
from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    '''unittests for org method'''
    @parameterized.expand([
        ('google', {'login': 'google', 'id': 1342004}),
        ('abc', {'message': 'Not Found'})
        ])
    @patch('client.get_json')
    def test_org(self, org: str, expected: Dict, getJson: MagicMock):
        '''unit test for org method'''
        getJson.return_value = Mock(return_value=expected)
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), expected)
        getJson.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        '''unit test for public_repos_url method'''
        value = {
            'login': 'google', 'id': 1342004,
            'repos_url': 'https://api.github.com/orgs/google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = value
            test = GithubOrgClient('google')
            self.assertEqual(test._public_repos_url, value["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, getJson: MagicMock):
        '''unit test for public_repos method'''
        val = [{
            "id": 1936771,
            "node_id": "MDEwOlJlcG9zaXRvcnkxOTM2Nzcx",
            "name": "truth"},
            {
                "id": 3248507,
                "node_id": "MDEwOlJlcG9zaXRvcnkzMjQ4NTA3",
                "name": "ruby-openid-apps-discovery",
            },
            {
                "id": 3248531,
                "node_id": "MDEwOlJlcG9zaXRvcnkzMjQ4NTMx",
                "name": "autoparse"}
        ]
        names = ['truth', 'ruby-openid-apps-discovery', 'autoparse']
        getJson.return_value = val
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = {
                'login': 'google', 'id': 1342004,
                'repos_url': 'https://api.github.com/orgs/google/repos'}
            test = GithubOrgClient('google')
            self.assertEqual(test.public_repos(), names)

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
            ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         result: bool):
        '''has_license method test'''
        test = GithubOrgClient('something')
        self.assertEqual(test.has_license(repo, license_key), result)


@parameterized_class([
    {'org': TEST_PAYLOAD[0][0], 'repos': TEST_PAYLOAD[0][1],
     'expected_repos': TEST_PAYLOAD[0][2], 'apache2_repos': TEST_PAYLOAD[0][3]}
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''integration test'''

    @classmethod
    def setUpClass(cls):
        '''class set up'''
        error = {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest" +
                                 "/orgs/orgs#get-an-organization"
        }
        urls = {
            'https://api.github.com/orgs/google': cls.org,
            'https://api.github.com/orgs/google/repos': cls.repos,
        }

        def payload(url):
            if url in urls:
                mock = Mock()
                mock.json.return_value = urls[url]
                return mock
            return error
        cls.get_patcher = patch('requests.get', side_effect=payload)
        cls.get_patcher.start

    @classmethod
    def tearDownClass(cls):
        '''tearDown'''
        cls.get_patcher.stop()
