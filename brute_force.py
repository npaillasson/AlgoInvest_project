#! /usr/bin/env python3
# coding: utf-8

max_invest = 500

invest = 0
choice_list = []
total_invest = 0
total_earn = 0
potential_lists = []

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

test_list = list(input_list)

def bruteforce(potential_lists, input_list, length=1):

    if length < len(input_list):
        for value in input_list:
            new_combination = [value]
            potential_lists.append(new_combination)
            bruteforce(potential_lists, input_list, length + 1)

    return potential_lists

for value in input_list:
    value[2] = ((value[1] * value[2]) / 100)

potential_lists = bruteforce(potential_lists, input_list)
print(potential_lists)

print(choice_list)
print("somme investie: ", total_invest)
print("somme gagnée: ", total_earn)
#print("pourcentage gain: ", ((100 * total_earn) / total_invest))