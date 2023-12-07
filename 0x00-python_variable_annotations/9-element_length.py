#!/usr/bin/env python3
'''function annotation'''
import typing


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> list[typing.Tuple[typing.Sequence, int]]:
    '''return a tuple'''
    return [(i, len(i)) for i in lst]
