#! /usr/bin/env python3
# coding: utf-8

import argparse
from algo.optimized import optimized_algo
# from algo.brute_force import bruteforce


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
    if args.bruteforce:
       print("bruteforce gogogo")
    else:
        print("non je reflechie un peu avant de foncer dans le tas")

main()
