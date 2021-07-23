#! /usr/bin/env python3
# coding: utf-8

from typing import List
from share import Share


class Combination:
    def __init__(self, shares: List[Share]):
        self.shares = shares
        self.benefit = sum([share.benefit for share in shares])
        self.cost = sum([share.cost for share in shares])
