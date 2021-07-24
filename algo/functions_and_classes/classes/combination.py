#! /usr/bin/env python3
# coding: utf-8

from typing import List
from share import Share


class Combination:
    def __init__(self, shares: List[Share]):
        self.shares = shares
        self.benefit = sum([share.benefit for share in shares])
        self.cost = sum([share.cost for share in shares])

    def __add__(self, object_to_add):
        if isinstance(object_to_add, Combination):
            self.shares.extend(object_to_add.shares)
        elif isinstance(object_to_add, Share):
            if object_to_add in self.shares:
                pass
            else:
                self.shares.append(object_to_add)
