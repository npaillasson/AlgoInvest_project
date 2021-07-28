#! /usr/bin/env python3
# coding: utf-8

from .functions_and_classes.classes.combination import Combination
from .functions_and_classes.view import display_results


def main_bruteforce(working_list, max_invest):

    length = 0
    last_combination = Combination([])
    best_combination = Combination([])
    max_length = len(working_list) + 1

    best_combination = bruteforce(length, working_list, last_combination, max_invest, best_combination, max_length)
    best_combination.gain_rate_calc()
    display_results(best_combination.shares, best_combination.cost, best_combination.benefit,
                    best_combination.gain_rate)


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
                best_combination = bruteforce(length + 1, next_working_list, last_combination + share,
                                              max_invest, best_combination, max_length)
            working_list.remove(share)

        return best_combination
