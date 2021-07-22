#! /usr/bin/env python3
# coding: utf-8

import csv
from classes.action import Action


def data_cleaner(file_path):

    with open(file_path, "r") as file:
        data_list = csv.reader(file)
        working_list = []
        for index, line in enumerate(data_list[1:]):
            try:
                line[1], line[2] = float(line[1]), float(line[2])
            except ValueError:
                print("Error: (line {} action {}) the price of an action and the profit can only contain"
                      " numbers ! The action will not be taken into account".format(index, line[0]))
                continue
            if line[1] <= 0:
                print("Error: (line {}) The action '{}' will not"
                      " be taken into account because its price is less than 0. ".format(index, line[0]))
            elif line[2] <= 0:
                print("Warning: (line {}) The action '{}' will not be taken"
                      " into account because its return on invest is less than 0. ".format(index, line[0]))
            else:
                new_action = Action(line[0], line[1], line[2])
                if new_action in working_list:
                    print("Error: (line {}) The action '{}' exists at least twice."
                          " Only the first occurrence will be taken into account ! ".format(index, line[0]))
                else:
                    working_list.append(new_action)

        return working_list
