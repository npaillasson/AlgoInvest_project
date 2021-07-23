#! /usr/bin/env python3
# coding: utf-8

from operator import attrgetter
from algo.functions_and_classes.classes.action import Share
from algo.functions_and_classes.view import display_results
from algo.functions_and_classes.dataset_cleaner import data_cleaner

def optimized_algo(path, max_invest=500, verbose=False):

    if not max_invest:
        max_invest = 500

    gain_rate = 0
    total_invest = 0
    total_earn = 0
    choice_list = []
    working_list = data_cleaner(path, verbose=verbose)
    working_list = sorted(working_list, key=attrgetter("ratio"), reverse=True)

    for share in working_list:
        new_invest_value = total_invest + share.cost
        if new_invest_value <= max_invest:
            total_invest = new_invest_value
            choice_list.append(share.name)
            total_earn += share.benefit
            gain_rate = ((100 * total_earn) / total_invest)

    display_results(choice_list, total_invest, total_earn, gain_rate)
