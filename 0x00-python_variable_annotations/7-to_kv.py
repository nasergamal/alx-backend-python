#!/usr/bin/env python3
'''function annotation'''


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    '''return a tuple'''
    return (k, v * v)
