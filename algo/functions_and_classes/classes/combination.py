#! /usr/bin/env python3
# coding: utf-8

from typing import List
from algo.functions_and_classes.classes.share import Share


class Combination:
    def __init__(self, max_invest, shares: List[Share]):
        self.shares = shares
        self.benefit = self.benefit_calc()
        self.cost = self.cost_calc()
        self.max_invest = max_invest

    def benefit_calc(self):
        self.benefit = sum([share.benefit for share in self.shares])
        return self.benefit

    def cost_calc(self):
        self.cost = sum([share.cost for share in self.shares])
        return self.cost

    def __add__(self, object_to_add):
        if isinstance(object_to_add, Combination):
            self.shares.extend(object_to_add.shares)
            return self
        elif isinstance(object_to_add, Share):
            if object_to_add in self.shares:
                return self
            else:
                self.shares.append(object_to_add)
                self.benefit_calc()
                self.cost_calc()
                return self

    def __repr__(self):
        return "shares {}\ncost {}\nbenefit {}".format(self.shares, self.cost, self.benefit)
