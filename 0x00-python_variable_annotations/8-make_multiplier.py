#!/usr/bin/env python3
'''function annotation'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''return a function'''
    def multi(x):
        return multiplier * x
    return multi
