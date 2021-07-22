#! /usr/bin/env python3
# coding: utf-8

class Action:
    def __init__(self, name: str, cost: float, percentage: float):
        self.name = name
        self.cost = cost
        self.percentage = percentage
        self.benefit = self.cost * self.percent / 100

    def __eq__(self, other_action):
        if other_action is isinstance(Action)



