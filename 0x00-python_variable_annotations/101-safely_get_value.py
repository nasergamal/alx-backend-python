#!/usr/bin/env python3
'''function annotation'''
import typing
T = typing.TypeVar('T', int, float, str)


def safely_get_value(dct: typing.Mapping, key: typing.Any,
                     default: typing.Union[T, None] = None
                     ) -> typing.Union[typing.Any, T]:
    '''TypeVar'''
    if key in dct:
        return dct[key]
    else:
        return default
