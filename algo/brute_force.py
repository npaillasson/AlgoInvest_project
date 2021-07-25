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

    length = 0
    last_combination = Combination([])
    best_combination = Combination([])
    working_list = data_cleaner(path, verbose=verbose)
    max_length = len(working_list)

    a = bruteforce(length, working_list, last_combination, max_invest, best_combination, max_length)
    print(a)


def bruteforce(length, working_list, last_combination, max_invest, best_combination, max_length):
    if length <= max_length:

        for share in working_list:
            next_working_list = list(working_list)
            next_working_list.remove(share)
            current_combination = last_combination + share
            if current_combination.cost > max_invest:
                bruteforce(length + 1, next_working_list, last_combination, max_invest,
                           best_combination, max_length)
            else:
                if current_combination.benefit > best_combination.benefit:
                    best_combination = current_combination
                bruteforce(length + 1, next_working_list, last_combination + share,
                           max_invest, best_combination, max_length)

        return best_combination

