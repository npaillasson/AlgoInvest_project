#! /usr/bin/env python3
# coding: utf-8

from algo.functions_and_classes.classes.action import Action
from algo.functions_and_classes.view import display_results
from algo.functions_and_classes.dataset_cleaner import data_cleaner

input_list = [
    ["Action-1", 20, 5],
    ["Action-2", 30, 10],
    ["Action-3", 50, 15],
    ["Action-4", 70, 20],
    ["Action-5", 60, 17],
    ["Action-6", 80, 25],
    ["Action-7", 22, 7],
    ["Action-8", 26, 11],
    ["Action-9", 48, 13],
    ["Action-10", 34, 27],
    ["Action-11", 42, 17],
    ["Action-12", 110, 9],
    ["Action-13", 38, 23],
    ["Action-14", 14, 1],
    ["Action-15", 18, 3],
    ["Action-16", 8, 8],
    ["Action-17", 4, 12],
    ["Action-18", 10, 14],
    ["Action-19", 24, 21],
    ["Action-20", 114, 18]
]

def optimized_algo(path, max_invest=500, verbose=False):

    if not max_invest:
        max_invest = 500

    total_invest = 0
    total_earn = 0
    choice_list = []
    working_list = data_cleaner(path, verbose=verbose)
    working_list = sorted(working_list, key=lambda action: action.ratio, reverse=True)

    for action in working_list:
        new_invest_value = total_invest + action.cost
        if new_invest_value <= max_invest:
            total_invest = new_invest_value
            choice_list.append(action.name)
            total_earn += action.benefit
            gain_rate = ((100 * total_earn) / total_invest)

    display_results(choice_list, total_invest, total_earn, gain_rate)


