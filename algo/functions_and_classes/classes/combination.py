#! /usr/bin/env python3
# coding: utf-8

from typing import List
from algo.functions_and_classes.classes.share import Share


class Combination:
    def __init__(self, shares: List[Share]):
        self.shares = shares
        self.benefit = self.benefit_calc()
        self.cost = self.cost_calc()
        self.gain_rate = self.gain_rate_calc()

    def benefit_calc(self):
        self.benefit = sum([share.benefit for share in self.shares])
        return self.benefit

    def cost_calc(self):
        self.cost = sum([share.cost for share in self.shares])
        return self.cost

    def gain_rate_calc(self):
        try:
            self.gain_rate = (self.benefit * 100) / self.cost
        except ZeroDivisionError:
            self.gain_rate = 0
        return self.gain_rate

    def calc_all(self):
        self.benefit_calc()
        self.cost_calc()

    def __add__(self, object_to_add):
        if isinstance(object_to_add, Combination):
            self.shares.extend(object_to_add.shares)
            return self
        elif isinstance(object_to_add, Share):
            new_combination = Combination([],)
            if object_to_add in self.shares:
                return self
            else:
                new_combination.shares = list(self.shares)
                new_combination.shares.append(object_to_add)
                new_combination.calc_all()
                return new_combination

    def __repr__(self):
        return "shares {}\ncost {}\nbenefit {}".format(self.shares, self.cost, self.benefit)
