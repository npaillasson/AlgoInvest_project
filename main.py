#! /usr/bin/env python3
# coding: utf-8

max_invest = 19

invest = 0
choice_list = []

input_list = [["value1", 12, 15], ["value2", 4, 9], ["value3", 15, 20], ["value4", 8, 10]]

for value in input_list:
    value[2] = ((value[1] * value[2]) / 100)

input_list = sorted(input_list, key=lambda columns: columns[2], reverse=True)

for value in input_list:
    new_invest_value = invest + value[1]
    if new_invest_value <= max_invest:
        invest = new_invest_value
        choice_list.append(value)

print(choice_list)