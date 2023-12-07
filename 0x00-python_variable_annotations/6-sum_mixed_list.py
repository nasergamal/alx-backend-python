#!/usr/bin/env python3
'''function annotation'''
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    '''return the sum of a list'''
    return sum(mxd_lst)
