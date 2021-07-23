#! /usr/bin/env python3
# coding: utf-8

class Share:
    def __init__(self, name: str, cost: float, percent: float):
        self.name = name
        self.cost = cost
        self.percent = percent
        self.benefit = self.cost * self.percent / 100
        self.ratio = self.benefit / self.cost

    def __eq__(self, other_share):
        if isinstance(other_share, Share):
            if self.name == other_share.name:
                return True
            else:
                return False
        else:
            return False
