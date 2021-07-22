#! /usr/bin/env python3
# coding: utf-8

import csv
from classes.action import Action

def data_cleaner(file_path):

    with open(cvs_file, "r") as file:
        data_list = csv.reader(file)
        working_list = []
        for line in data_list:
            if line[1] <= 0:
                print("Error: The action '{}' will not be taken into incount because its price is less than 0. ")
            elif line[2] <= 0:
                print("Warning: The action '{}' will not be taken into incount because its return on invest is less"
                      " than 0. ")
            else:
                if
                working_list.append(Action(line[0], line[1], line[2]))

