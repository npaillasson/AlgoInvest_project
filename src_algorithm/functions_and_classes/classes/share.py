#! /usr/bin/env python3
# coding: utf-8

class Share:
    def __init__(self, name: str, cost: float, percent: float):
        self.name = name
        self.cost = cost
        self.percent = percent
        self.benefit = self.cost * self.percent / 100

    def __eq__(self, other_share):
        if isinstance(other_share, Share) and self.name == other_share.name:
            return True
        else:
            return False

    def __repr__(self):
        return "name {}, cost {}€, earn {}€".format(self.name, round(self.cost, 2), round(self.benefit, 3))
