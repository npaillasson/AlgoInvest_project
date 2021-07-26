#! /usr/bin/env python3
# coding: utf-8

import csv
import sys
from algo.functions_and_classes.classes.share import Share


def data_cleaner(file_path, verbose=False):

    with open(file_path, "r") as file:
        data_list = csv.reader(file)
        next(data_list)
        working_list = []
        for index, line in enumerate(data_list):
            try:
                line[1], line[2] = float(line[1]), float(line[2])
                index += 2
            except ValueError:
                if verbose:
                    print("Error: (line {} action {}) the price of an action and the profit can only contain"
                          " numbers ! The action will not be taken into account".format(index, line[0]))
                continue
            except IndexError:
                print("The CSV file seems incorrect... for more information, please refer to the README.md file.")
                exit()
            if line[1] <= 0:
                if verbose:
                    print("Error: (line {}) The action '{}' will not"
                          " be taken into account because its price is less than 0. ".format(index, line[0]))
            elif line[2] <= 0:
                if verbose:
                    print("Warning: (line {}) The action '{}' will not be taken"
                          " into account because its return on invest is less than 0. ".format(index, line[0]))
            else:
                new_share = Share(line[0], line[1], line[2])
                if new_share in working_list:
                    if verbose:
                        print("Error: (line {}) The action '{}' exists at least twice in the csv file."
                              " Only the first occurrence will be taken into account ! ".format(index, line[0]))
                else:
                    working_list.append(new_share)

        return working_list
