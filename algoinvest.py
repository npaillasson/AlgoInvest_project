#! /usr/bin/env python3
# coding: utf-8

import argparse
from algo.optimized import main_optimized_algo
from algo.brute_force import main_bruteforce
from algo.functions_and_classes.dataset_cleaner import data_cleaner

DEFAULT_MAX_INVEST = 500

def max_invest_amount(args):
    if not args.max_invest:
        max_invest = DEFAULT_MAX_INVEST
    else:
        max_invest = args.max_invest

    return max_invest

def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the path to the csv file to be analyzed")
    parser.add_argument("-v", "--verbose", action="store_true", help="display errors and warnings in the csv file")
    parser.add_argument("-m", "--max-invest", type=int, help="allows you to modify the maximum amount to "
                                                             "invest (500€ by default)")
    parser.add_argument("--bruteforce", action="store_true", help="allows to launch the algorithm in bruteforce mode")

    return parser.parse_args()


def main():
    args = parse_argument()
    print(args)
    working_list = data_cleaner(args.file, verbose=args.verbose)
    if args.bruteforce:
        print("Warning")
        main_bruteforce(working_list, max_invest=max_invest_amount(args))
    else:
        main_optimized_algo(working_list, max_invest=max_invest_amount(args))


if __name__ == "__main__":
    main()
