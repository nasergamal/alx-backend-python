#!/usr/bin/env python3
"""tests for utilities class
"""
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
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    '''unit tests with parameterized'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", 'b'), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Union[Dict, int]) -> None:
        '''test access_nested_map return'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence, expected: Exception
                                         ) -> None:
        '''test access_nested_map exception'''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''getjson unit tests'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        mockreq = unittest.mock.Mock()
        mockreq.json.return_value = test_payload
        with unittest.mock.patch('requests.get', return_value=mockreq):
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''unittest memoization'''
    def test_memoize(self):
        '''memo'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        mem = TestClass()
        with unittest.mock.patch.object(mem, 'a_method') as mock:
            mock.return_value = 42
            first = mem.a_property
            second = mem.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock.assert_called_once()
