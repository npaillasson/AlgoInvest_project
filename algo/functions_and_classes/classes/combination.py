#! /usr/bin/env python3
# coding: utf-8

from typing import List
from share import Share

class Combinaison:
    def __init__(self, shares: List[Share]):
        self.shares = shares
        self.benefit = sum([action.benefit for action in list_shares])
        self.cost = sum([share.cost for share in shares])

#algo.functions_and_classes.classes.