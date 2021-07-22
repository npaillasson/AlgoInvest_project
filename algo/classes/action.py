#! /usr/bin/env python3
# coding: utf-8

class Action:
    def __init__(self, name: str, cost: float, percent: float):
        self.name = name
        self.cost = cost
        self.percent = percent
        self.benefit = self.cost * self.percent / 100

    def __eq__(self, other_action):
        if isinstance(other_action, Action):
            if self.name == other_action.name:
                return True
            else:
                return False
        else:
            return False




