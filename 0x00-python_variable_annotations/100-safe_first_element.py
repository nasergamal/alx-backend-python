#!/usr/bin/env python3
'''function annotation'''
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Union[typing.Any, None]:
    '''return the start of varialbe'''
    if lst:
        return lst[0]
    else:
        return None
