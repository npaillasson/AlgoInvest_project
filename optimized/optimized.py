#! /usr/bin/env python3
# coding: utf-8

max_invest = 500

invest = 0
choice_list = []
total_invest = 0
total_earn = 0

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

working_list = sorted(working_list, key=lambda action: action.benefit, reverse=True)

for value in input_list:
    new_invest_value = invest + value[1]
    if new_invest_value <= max_invest:
        invest = new_invest_value
        choice_list.append(value)
        total_invest += value[1]
        total_earn += value[2]

print(choice_list)
print("somme investie: ", total_invest)
print("somme gagnée: ", total_earn)
print("pourcentage gain: ", ((100 * total_earn) / total_invest))