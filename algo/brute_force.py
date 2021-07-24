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


#def make_combinations(number: int, max_invest, working_list: List[Share]) -> List[Combination]:
#    combinations = []
#    if number <= len(working_list):
#        for share in working_list:

#    return [comb for comb in combinations if comb.cost <= max_invest]


def main_bruteforce(path, max_invest, verbose=False):

    gain_rate = 0
    total_invest = 0
    total_earn = 0
    choice_list = []
    length = 0
    last_combination = Combination([])
    best_combination = Combination([])
    working_list = data_cleaner(path, verbose=verbose)

    bruteforce(length, working_list, last_combination, max_invest, best_combination)


def bruteforce(length, working_list, last_combination, max_invest, best_combination):
    if length <= len(working_list):

        for share in working_list:
            print(length)
            print("laster", last_combination)
            current_combination = last_combination + share
            print(current_combination.cost <= max_invest)
            if current_combination.cost <= max_invest:
                last_combination = current_combination
                if last_combination.benefit > best_combination.benefit:
                    best_combination = last_combination

            bruteforce(length + 1, working_list, last_combination, max_invest, best_combination)

