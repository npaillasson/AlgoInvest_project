#! /usr/bin/env python3
# coding: utf-8

from typing import List
from action import Action

class Combinaison:
    def __init__(self, actions: List[Action]):
        self.actions = actions
        self.benefit = sum([action.benefit for action in list_actions])
        self.cost = sum([action.cost for action in actions])

#algo.functions_and_classes.classes.