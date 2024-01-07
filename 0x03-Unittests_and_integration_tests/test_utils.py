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
from unittest.mock import (
        Mock,
        patch,
)
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
    def test_get_json(self, url: str, payload: Dict) -> None:
        '''test get_json method'''
        mockreq = Mock()
        mockreq.json.return_value = payload
        with patch('requests.get', return_value=mockreq) as mock:
            self.assertEqual(get_json(url), payload)
            mock.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    '''unittest memoization'''
    def test_memoize(self) -> None:
        '''memoization'''
        class TestClass:
            '''Test class'''
            def a_method(self):
                '''a_method return integer 42'''
                return 42

            @memoize
            def a_property(self):
                '''
                    a_property wrapped to prevent additional calls to a_method
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=Mock(return_value=42)) as mock:
            mem = TestClass()
            first = mem.a_property()
            second = mem.a_property()
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock.assert_called_once()
