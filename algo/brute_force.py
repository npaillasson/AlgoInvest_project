#! /usr/bin/env python3
# coding: utf-8

from typing import List
from algo.functions_and_classes.dataset_cleaner import data_cleaner
from algo.functions_and_classes.classes.share import Share
from algo.functions_and_classes.classes.combination import Combination

potential_lists = []
record_list = []
record_invest = 0
record_win = 0

input_list = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
]


def make_combinations(number: int, max_invest, share: List[Share]) -> List[Combination]:
    combinations = []

    return [comb for comb in combinations if comb.cost <= max_invest]


def main(path, max_invest, verbose=False):

    gain_rate = 0
    total_invest = 0
    total_earn = 0
    choice_list = []
    working_list = data_cleaner(path, verbose=verbose)

    shares = [Share(share[0], share[1], share[2]) for share in working_list]

    current_best_combination = None

    for number in range(len(shares)):
        number = number + 1
        combinations = make_combinations(number, max_invest, shares)
        for combination in combinations:
            if current_best_combination and current_best_combination.benefit < combination.benefit:
                current_best_combination = combination

