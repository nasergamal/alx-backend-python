#!/usr/bin/env python3
'''function annotation'''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    '''return a tuple'''
    return (k, v * v)
